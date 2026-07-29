"""
Compute average image dimensions across all image datasets in the project.
"""

import json
import sys
from pathlib import Path
import statistics
from PIL import Image


DATASETS = {
    "rvlcdip_test": r"c:\Users\grant\AMFAM\rvlcdip_dataset\test",
    "balanced_50_per_class": r"c:\Users\grant\AMFAM\rvlcdip_dataset\balanced_50_per_class",
    "processed_balanced": r"c:\Users\grant\AMFAM\processed_balanced_dataset\images",
    "processed_documents": r"c:\Users\grant\AMFAM\processed_documents\images",
}

IMAGE_EXTENSIONS = (".tif", ".tiff", ".png", ".jpg", ".jpeg", ".bmp")


def collect_dimensions(dataset_path: str):
    root = Path(dataset_path)
    widths, heights, aspect_ratios = [], [], []
    unreadable: list[dict[str, str]] = []

    if not root.exists():
        return None, f"Path does not exist: {root}"

    for ext in IMAGE_EXTENSIONS:
        for img_path in root.rglob(f"*{ext}"):
            try:
                with Image.open(img_path) as img:
                    w, h = img.size
                    widths.append(w)
                    heights.append(h)
                    aspect_ratios.append(w / h if h else 0)
            except (OSError, ValueError) as e:
                unreadable.append({"path": str(img_path), "error": f"{type(e).__name__}: {e}"})
                print(f"  Warning: could not read {img_path}: {e}")

    skipped = len(unreadable)
    n = len(widths)
    if n == 0:
        return {"count": 0, "skipped": skipped, "unreadable": unreadable}, None

    def stats(values):
        return {
            "mean": round(statistics.mean(values), 2),
            "median": round(statistics.median(values), 2),
            "min": int(min(values)),
            "max": int(max(values)),
            "std": round(statistics.stdev(values), 2) if len(values) > 1 else 0.0,
        }

    return {
        "count": n,
        "skipped": skipped,
        "unreadable": unreadable,
        "width": stats(widths),
        "height": stats(heights),
        "aspect_ratio": stats(aspect_ratios),
    }, None


def main() -> int:
    results = {}
    overall_widths, overall_heights = [], []
    errors: list[str] = []
    total_skipped = 0

    print("=" * 60)
    print("IMAGE DIMENSION EDA")
    print("=" * 60)

    for name, path in DATASETS.items():
        print(f"\nAnalyzing {name}: {path}")
        data, error = collect_dimensions(path)

        if error:
            results[name] = {"error": error}
            errors.append(f"{name}: {error}")
            print(f"  {error}")
            continue

        results[name] = data
        total_skipped += data["skipped"]
        print(f"  Images: {data['count']}, Skipped: {data['skipped']}")
        if data["count"]:
            print(f"  Width  - mean: {data['width']['mean']}, median: {data['width']['median']}")
            print(f"  Height - mean: {data['height']['mean']}, median: {data['height']['median']}")
            print(f"  Avg dimensions: {data['width']['mean']:.0f} x {data['height']['mean']:.0f}")

            overall_widths.extend([data["width"]["mean"]] * data["count"])
            overall_heights.extend([data["height"]["mean"]] * data["count"])

    if overall_widths and overall_heights:
        results["overall"] = {
            "count": len(overall_widths),
            "width_mean": round(statistics.mean(overall_widths), 2),
            "height_mean": round(statistics.mean(overall_heights), 2),
        }
        print(f"\nOverall average dimensions across all images: "
              f"{results['overall']['width_mean']:.0f} x {results['overall']['height_mean']:.0f}")

    output_path = Path(r"c:\Users\grant\AMFAM\dimensions_summary.json")
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)
    except OSError as e:
        print(f"Error: could not write summary to {output_path}: {e}")
        return 1

    print(f"\nSummary saved: {output_path}")

    if errors:
        print(f"\n{len(errors)} dataset(s) could not be analyzed:")
        for message in errors:
            print(f"  - {message}")
    if total_skipped:
        print(f"{total_skipped} image(s) were unreadable; see 'unreadable' entries in the summary.")

    return 1 if errors or total_skipped else 0


if __name__ == "__main__":
    sys.exit(main())
