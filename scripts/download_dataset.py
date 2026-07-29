"""Download the RVL-CDIP test dataset from Kaggle via kagglehub."""

import sys

import kagglehub


def main() -> int:
    try:
        # Download latest version
        path = kagglehub.dataset_download("pdavpoojan/the-rvlcdip-dataset-test")
    except Exception as e:
        print(f"Error: dataset download failed: {type(e).__name__}: {e}")
        print("Check your Kaggle credentials (KAGGLE_USERNAME/KAGGLE_KEY or ~/.kaggle/kaggle.json).")
        return 1

    print("Path to dataset files:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
