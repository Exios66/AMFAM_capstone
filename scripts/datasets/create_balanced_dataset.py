"""
Create a balanced dataset with 50 random images per class from RVL-CDIP dataset
"""

import os
import shutil
import sys
from pathlib import Path
import random
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.cli_utils import print_header

class BalancedDatasetCreator:
    """Create a balanced dataset by sampling random images from each class"""
    
    def __init__(self, source_path: str, output_path: str, samples_per_class: int = 50):
        self.source_path = Path(source_path)
        self.output_path = Path(output_path)
        self.samples_per_class = samples_per_class
        self.classes = sorted([d.name for d in self.source_path.iterdir() if d.is_dir()])
        
        # Create output directory
        self.output_path.mkdir(parents=True, exist_ok=True)
        
    def sample_images(self):
        """Sample random images from each class"""
        print_header("CREATING BALANCED DATASET")
        print(f"Source: {self.source_path}")
        print(f"Output: {self.output_path}")
        print(f"Samples per class: {self.samples_per_class}")
        print(f"Total classes: {len(self.classes)}")
        print(f"Expected total images: {len(self.classes) * self.samples_per_class}")
        print()
        
        sampling_log = []
        
        for class_name in self.classes:
            class_source = self.source_path / class_name
            class_output = self.output_path / class_name
            class_output.mkdir(exist_ok=True)
            
            # Get all image files
            image_files = list(class_source.glob("*.tif"))
            total_available = len(image_files)
            
            print(f"Processing class: {class_name}")
            print(f"  Available images: {total_available}")
            
            # Sample random images
            if total_available >= self.samples_per_class:
                sampled_files = random.sample(image_files, self.samples_per_class)
            else:
                print(f"  Warning: Only {total_available} images available (less than {self.samples_per_class})")
                sampled_files = image_files
            
            # Copy sampled images
            copied_count = 0
            for img_path in sampled_files:
                dest_path = class_output / img_path.name
                shutil.copy2(img_path, dest_path)
                copied_count += 1
            
            print(f"  Copied: {copied_count} images")
            
            sampling_log.append({
                'class': class_name,
                'available': total_available,
                'sampled': copied_count,
                'percentage': (copied_count / total_available) * 100 if total_available > 0 else 0
            })
        
        # Save sampling log
        log_path = self.output_path / "sampling_log.json"
        with open(log_path, 'w') as f:
            json.dump(sampling_log, f, indent=2)
        
        print()
        print_header("SAMPLING COMPLETE")
        
        # Summary
        total_copied = sum(item['sampled'] for item in sampling_log)
        print(f"Total images copied: {total_copied}")
        print(f"Sampling log saved: {log_path}")
        
        return sampling_log
    
    def verify_dataset(self):
        """Verify the created balanced dataset"""
        print()
        print_header("VERIFYING BALANCED DATASET")
        
        verification_log = []
        
        for class_name in self.classes:
            class_path = self.output_path / class_name
            if class_path.exists():
                image_count = len(list(class_path.glob("*.tif")))
                verification_log.append({
                    'class': class_name,
                    'count': image_count,
                    'status': 'OK' if image_count == self.samples_per_class else 'MISMATCH'
                })
                print(f"{class_name:25s}: {image_count:3d} images")
            else:
                verification_log.append({
                    'class': class_name,
                    'count': 0,
                    'status': 'MISSING'
                })
                print(f"{class_name:25s}: MISSING")
        
        # Save verification log
        verify_path = self.output_path / "verification_log.json"
        with open(verify_path, 'w') as f:
            json.dump(verification_log, f, indent=2)
        
        print()
        print(f"Verification log saved: {verify_path}")
        
        return verification_log


def main():
    # Configuration
    SOURCE_PATH = r"c:\Users\grant\AMFAM\rvlcdip_dataset\test"
    OUTPUT_PATH = r"c:\Users\grant\AMFAM\rvlcdip_dataset\balanced_50_per_class"
    SAMPLES_PER_CLASS = 50
    
    # Create balanced dataset
    creator = BalancedDatasetCreator(SOURCE_PATH, OUTPUT_PATH, SAMPLES_PER_CLASS)
    
    # Sample images
    sampling_log = creator.sample_images()
    
    # Verify dataset
    verification_log = creator.verify_dataset()
    
    print()
    print("Balanced dataset creation complete!")


if __name__ == "__main__":
    main()
