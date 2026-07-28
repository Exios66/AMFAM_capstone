"""
Resize images to a fixed target size.

Provides two workflows:
- create_fixed_size_dataset: resize every image in one input directory.
- create_sampled_fixed_size_dataset: sample N images from multiple datasets,
  preserve aspect ratio with padding, and resize to a fixed square.
"""

import json
import random
from pathlib import Path

from PIL import Image

CLASS_NAMES = (
    "advertisement",
    "budget",
    "email",
    "file_folder",
    "form",
    "handwritten",
    "invoice",
    "letter",
    "memo",
    "news_article",
    "presentation",
    "questionnaire",
    "resume",
    "scientific_publication",
    "scientific_report",
    "specification",
)


def create_fixed_size_dataset(input_dir: str, output_dir: str, target_size: tuple[int, int]):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_images_dir = output_dir / "images"
    output_images_dir.mkdir(parents=True, exist_ok=True)

    image_paths = sorted(
        list(input_dir.glob("*.png"))
        + list(input_dir.glob("*.jpg"))
        + list(input_dir.glob("*.jpeg"))
        + list(input_dir.glob("*.tif"))
        + list(input_dir.glob("*.tiff"))
        + list(input_dir.glob("*.bmp"))
    )

    print("=" * 60)
    print("CREATING FIXED-SIZE DATASET")
    print("=" * 60)
    print(f"Input:  {input_dir}")
    print(f"Output: {output_images_dir}")
    print(f"Target size: {target_size}")
    print(f"Images to process: {len(image_paths)}")
    print()

    log = []
    for img_path in image_paths:
        try:
            with Image.open(img_path) as img:
                original_size = img.size
                resized = img.resize(target_size, Image.Resampling.LANCZOS)
                dest_path = output_images_dir / img_path.name
                resized.save(dest_path)

                log.append({
                    "file": img_path.name,
                    "status": "success",
                    "original_size": original_size,
                    "new_size": resized.size,
                })
                print(f"Resized {img_path.name}: {original_size} -> {resized.size}")
        except Exception as e:
            log.append({
                "file": img_path.name,
                "status": "error",
                "error": str(e),
            })
            print(f"Error resizing {img_path.name}: {e}")

    successful = sum(1 for entry in log if entry["status"] == "success")
    failed = sum(1 for entry in log if entry["status"] == "error")

    summary = {
        "target_size": target_size,
        "total": len(log),
        "successful": successful,
        "failed": failed,
        "details": log,
    }
    summary_path = output_dir / "resize_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print()
    print("=" * 60)
    print("FIXED-SIZE DATASET CREATION COMPLETE")
    print("=" * 60)
    print(f"Total: {len(log)} | Successful: {successful} | Failed: {failed}")
    print(f"Summary saved: {summary_path}")


def _pad_color_for_mode(mode: str, fill: int | tuple[int, ...]) -> int | tuple[int, ...]:
    if mode == "L":
        return fill if isinstance(fill, int) else fill[0]
    if mode == "1":
        return 1 if fill else 0
    if mode == "RGBA":
        return fill if isinstance(fill, tuple) else (fill, fill, fill, fill)
    # RGB or any fallback converted to RGB
    return fill if isinstance(fill, tuple) else (fill, fill, fill)


def resize_with_padding(
    img: Image.Image,
    target_size: tuple[int, int],
    fill: int | tuple[int, ...] = 255,
) -> Image.Image:
    """Scale image to fit inside target_size, then center-pad to the exact size."""
    target_w, target_h = target_size

    scale = min(target_w / img.width, target_h / img.height)
    new_w = max(1, int(img.width * scale))
    new_h = max(1, int(img.height * scale))
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Convert palette/other modes to RGB so a solid fill always works
    if resized.mode not in ("L", "1", "RGB", "RGBA"):
        resized = resized.convert("RGB")

    bg_fill = _pad_color_for_mode(resized.mode, fill)
    background = Image.new(resized.mode, target_size, bg_fill)

    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    if resized.mode == "RGBA":
        background.paste(resized, (x, y), resized)
    else:
        background.paste(resized, (x, y))

    return background


def _collect_class_images(
    input_dir: Path,
    class_names: tuple[str, ...],
    extensions: tuple[str, ...],
) -> dict[str, list[Path]]:
    """Group images in a dataset by class, either from subdirs or filename prefixes."""
    class_images: dict[str, list[Path]] = {c: [] for c in class_names}

    # If class subdirectories exist, use them
    if any((input_dir / c).is_dir() for c in class_names):
        for class_name in class_names:
            class_dir = input_dir / class_name
            if not class_dir.is_dir():
                continue
            for ext in extensions:
                class_images[class_name].extend(class_dir.rglob(ext))
        return class_images

    # Otherwise, infer class from the filename prefix
    all_images: list[Path] = []
    for ext in extensions:
        all_images.extend(input_dir.rglob(ext))

    for img_path in all_images:
        name_lower = img_path.name.lower()
        for class_name in class_names:
            if name_lower.startswith(f"{class_name}_"):
                class_images[class_name].append(img_path)
                break

    return class_images


def create_sampled_fixed_size_dataset(
    datasets: dict[str, str],
    output_dir: str,
    target_size: tuple[int, int],
    samples_per_class: int = 10,
    seed: int | None = 42,
    fill: int | tuple[int, int, int] = 255,
):
    """Sample images from each class across datasets and resize them to a fixed padded square."""
    output_dir = Path(output_dir)
    output_images_dir = output_dir / "images"
    output_images_dir.mkdir(parents=True, exist_ok=True)

    extensions = ("*.png", "*.jpg", "*.jpeg", "*.tif", "*.tiff", "*.bmp")

    print("=" * 60)
    print("CREATING SAMPLED FIXED-SIZE DATASET")
    print("=" * 60)
    print(f"Output: {output_images_dir}")
    print(f"Target size: {target_size}")
    print(f"Samples per class: {samples_per_class}")
    print(f"Random seed: {seed}")
    print()

    if seed is not None:
        random.seed(seed)

    log: list[dict] = []
    total_successful = 0
    total_failed = 0

    for dataset_name, input_dir_str in datasets.items():
        input_dir = Path(input_dir_str)
        if not input_dir.exists():
            print(f"Warning: dataset '{dataset_name}' path does not exist: {input_dir}")
            log.append({
                "dataset": dataset_name,
                "input_dir": str(input_dir),
                "status": "skipped",
                "reason": "path does not exist",
            })
            continue

        class_images = _collect_class_images(input_dir, CLASS_NAMES, extensions)

        for class_name, image_paths in class_images.items():
            available = len(image_paths)
            if available == 0:
                continue

            sample_count = min(samples_per_class, available)
            if sample_count < samples_per_class:
                print(
                    f"Warning: {dataset_name}/{class_name} has only {available} image(s); "
                    f"sampling all {sample_count}."
                )

            sampled_paths = random.sample(image_paths, sample_count)

            dataset_success = 0
            dataset_failed = 0
            for img_path in sampled_paths:
                try:
                    with Image.open(img_path) as img:
                        original_size = img.size
                        padded = resize_with_padding(img, target_size, fill)

                        dest_name = f"{dataset_name}__{class_name}__{img_path.stem}.png"
                        dest_path = output_images_dir / dest_name
                        padded.save(dest_path)

                        log.append({
                            "dataset": dataset_name,
                            "class": class_name,
                            "source_file": img_path.name,
                            "source_path": str(img_path),
                            "output_file": dest_name,
                            "status": "success",
                            "original_size": original_size,
                            "new_size": padded.size,
                        })
                        dataset_success += 1
                        print(
                            f"Resized {dataset_name}/{class_name}/{img_path.name}: "
                            f"{original_size} -> {padded.size}"
                        )
                except Exception as e:
                    log.append({
                        "dataset": dataset_name,
                        "class": class_name,
                        "source_file": img_path.name,
                        "source_path": str(img_path),
                        "status": "error",
                        "error": str(e),
                    })
                    dataset_failed += 1
                    print(f"Error resizing {dataset_name}/{class_name}/{img_path.name}: {e}")

            total_successful += dataset_success
            total_failed += dataset_failed

    summary = {
        "target_size": target_size,
        "samples_per_class": samples_per_class,
        "random_seed": seed,
        "total_datasets": len(datasets),
        "total_classes": len(CLASS_NAMES),
        "total_successful": total_successful,
        "total_failed": total_failed,
        "details": log,
    }
    summary_path = output_dir / "resize_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print()
    print("=" * 60)
    print("SAMPLED FIXED-SIZE DATASET CREATION COMPLETE")
    print("=" * 60)
    print(f"Total: {total_successful + total_failed} | Successful: {total_successful} | Failed: {total_failed}")
    print(f"Summary saved: {summary_path}")


def main():
    DATASETS = {
        "processed_balanced": r"c:\Users\grant\AMFAM\50perclass_800\images",
    }

    # Define all dataset configurations to build
    configs = [
        {
            "output_dir": r"c:\Users\grant\AMFAM\2550x3300_50perclass_800",
            "target_size": (2550, 3300),  # 300 DPI US Letter (8.5" x 11")
            "samples_per_class": 50,
        },
        {
            "output_dir": r"c:\Users\grant\AMFAM\2550x3300_10perclass_160",
            "target_size": (2550, 3300),
            "samples_per_class": 10,
        },
        {
            "output_dir": r"c:\Users\grant\AMFAM\1024x1024_50perclass_800",
            "target_size": (1024, 1024),
            "samples_per_class": 50,
        },
        {
            "output_dir": r"c:\Users\grant\AMFAM\1024x1024_10perclass_160",
            "target_size": (1024, 1024),
            "samples_per_class": 10,
        },
    ]

    for cfg in configs:
        output_dir = Path(cfg["output_dir"])
        images_dir = output_dir / "images"

        # Skip if already exists
        if images_dir.exists() and any(images_dir.iterdir()):
            print(f"Skipping '{output_dir.name}' — already exists with images.")
            continue

        print(f"\nBuilding: {output_dir.name}")
        create_sampled_fixed_size_dataset(
            DATASETS,
            str(output_dir),
            cfg["target_size"],
            samples_per_class=cfg["samples_per_class"],
            seed=42,
        )


if __name__ == "__main__":
    main()
