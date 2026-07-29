"""
Run document processor on balanced_50_per_class TIFF dataset
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.cli_utils import print_header
from src.document_processor import ClassOrganizedBatchProcessor

def main() -> int:
    # Configuration
    INPUT_DIR = r"c:\Users\grant\AMFAM\rvlcdip_dataset\balanced_50_per_class"
    OUTPUT_DIR = r"c:\Users\grant\AMFAM\processed_balanced_dataset"
    
    if not Path(INPUT_DIR).is_dir():
        print(f"Error: input directory does not exist: {INPUT_DIR}")
        return 1

    print_header("Processing Balanced TIFF Dataset")
    print(f"Input: {INPUT_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print()
    
    # Initialize processor
    processor = ClassOrganizedBatchProcessor(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
        dpi=300
    )
    
    # Process all TIFF files
    results = processor.process_batch()
    
    # Save processing summary
    summary_path = Path(OUTPUT_DIR) / "processing_summary.json"
    try:
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        with open(summary_path, 'w') as f:
            json.dump(results, f, indent=2)
    except OSError as e:
        print(f"Error: could not write processing summary to {summary_path}: {e}")
        return 1
    
    print()
    print_header("Processing Summary")
    
    successful = sum(1 for r in results if r['status'] == 'success')
    failed = len(results) - successful
    
    print(f"Total documents: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Summary saved to: {summary_path}")
    
    # Show class breakdown
    class_counts = {}
    for result in results:
        if result['status'] == 'success':
            class_label = result.get('class_label', 'unknown')
            class_counts[class_label] = class_counts.get(class_label, 0) + 1
    
    print()
    print("Documents per class:")
    for class_name, count in sorted(class_counts.items()):
        print(f"  {class_name}: {count}")
    
    if failed:
        print()
        print(f"{failed} document(s) failed. First failures:")
        for result in [r for r in results if r['status'] != 'success'][:10]:
            print(f"  {result['document_name']}: {result.get('error_type', 'Error')}: {result.get('error', '')}")
        return 1
    if not results:
        print("Error: no documents were processed.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
