"""
Run document processor on balanced_50_per_class TIFF dataset
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.cli_utils import print_header
from src.document_processor import ClassOrganizedBatchProcessor

def main():
    # Configuration
    INPUT_DIR = r"c:\Users\grant\AMFAM\rvlcdip_dataset\balanced_50_per_class"
    OUTPUT_DIR = r"c:\Users\grant\AMFAM\processed_balanced_dataset"
    
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
    summary_path = f"{OUTPUT_DIR}/processing_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2)
    
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

if __name__ == "__main__":
    main()
