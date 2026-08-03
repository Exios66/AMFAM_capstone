"""
Exploratory Data Analysis (EDA) for RVL-CDIP Document Image Dataset
Analyzes class distribution, image properties, and generates visualizations
"""

import os
import sys
import json
from pathlib import Path
from collections import defaultdict
import random

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.cli_utils import print_header

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "reports"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from tqdm import tqdm

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class DocumentDatasetEDA:
    """Comprehensive EDA for document image datasets"""
    
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)
        self.classes = sorted([d.name for d in self.dataset_path.iterdir() if d.is_dir()])
        self.image_data = []
        self.class_stats = defaultdict(dict)
        
    def collect_image_data(self, sample_size=None):
        """
        Collect image data from all classes.
        Args:
            sample_size: If specified, only sample this many images per class (for faster analysis)
        """
        print("Collecting image data...")
        
        for class_name in self.classes:
            class_path = self.dataset_path / class_name
            image_files = list(class_path.glob("*.tif"))
            
            # Sample if needed
            if sample_size and len(image_files) > sample_size:
                image_files = random.sample(image_files, sample_size)
            
            print(f"Processing class: {class_name} ({len(image_files)} images)")
            
            for img_path in tqdm(image_files, desc=f"  {class_name}"):
                try:
                    img = Image.open(img_path)
                    self.image_data.append({
                        'class': class_name,
                        'filename': img_path.name,
                        'width': img.width,
                        'height': img.height,
                        'mode': img.mode,
                        'format': img.format,
                        'size_bytes': img_path.stat().st_size,
                        'aspect_ratio': img.width / img.height
                    })
                    img.close()
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")
        
        self.df = pd.DataFrame(self.image_data)
        print(f"Collected data for {len(self.df)} images")
        
    def analyze_class_distribution(self):
        """Analyze and visualize class distribution"""
        print()
        print_header("CLASS DISTRIBUTION ANALYSIS")
        
        class_counts = self.df['class'].value_counts().sort_values(ascending=False)
        
        print(f"\nTotal classes: {len(class_counts)}")
        print(f"Total images: {len(self.df)}")
        print(f"\nImages per class:")
        for class_name, count in class_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {class_name:25s}: {count:6d} ({percentage:5.2f}%)")
        
        # Calculate imbalance metrics
        max_count = class_counts.max()
        min_count = class_counts.min()
        imbalance_ratio = max_count / min_count
        
        print(f"\nImbalance ratio (max/min): {imbalance_ratio:.2f}")
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Bar plot
        class_counts.plot(kind='bar', ax=ax1, color='steelblue')
        ax1.set_title('Class Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Document Class', fontsize=12)
        ax1.set_ylabel('Number of Images', fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        
        # Pie chart
        class_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Class Distribution (Percentage)', fontsize=14, fontweight='bold')
        ax2.set_ylabel('')
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "class_distribution.png", dpi=300, bbox_inches='tight')
        print(f"\nSaved: class_distribution.png")
        plt.close()
        
        return class_counts
    
    def analyze_image_dimensions(self):
        """Analyze image dimensions and aspect ratios"""
        print()
        print_header("IMAGE DIMENSIONS ANALYSIS")
        
        # Width statistics
        print(f"\nWidth Statistics:")
        print(f"  Mean: {self.df['width'].mean():.2f}")
        print(f"  Median: {self.df['width'].median():.2f}")
        print(f"  Min: {self.df['width'].min()}")
        print(f"  Max: {self.df['width'].max()}")
        print(f"  Std: {self.df['width'].std():.2f}")
        
        # Height statistics
        print(f"\nHeight Statistics:")
        print(f"  Mean: {self.df['height'].mean():.2f}")
        print(f"  Median: {self.df['height'].median():.2f}")
        print(f"  Min: {self.df['height'].min()}")
        print(f"  Max: {self.df['height'].max()}")
        print(f"  Std: {self.df['height'].std():.2f}")
        
        # Aspect ratio statistics
        print(f"\nAspect Ratio Statistics:")
        print(f"  Mean: {self.df['aspect_ratio'].mean():.3f}")
        print(f"  Median: {self.df['aspect_ratio'].median():.3f}")
        print(f"  Min: {self.df['aspect_ratio'].min():.3f}")
        print(f"  Max: {self.df['aspect_ratio'].max():.3f}")
        
        # Visualization
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Width distribution
        self.df['width'].hist(bins=50, ax=axes[0, 0], color='steelblue', edgecolor='black')
        axes[0, 0].set_title('Width Distribution', fontsize=12, fontweight='bold')
        axes[0, 0].set_xlabel('Width (pixels)')
        axes[0, 0].set_ylabel('Frequency')
        
        # Height distribution
        self.df['height'].hist(bins=50, ax=axes[0, 1], color='coral', edgecolor='black')
        axes[0, 1].set_title('Height Distribution', fontsize=12, fontweight='bold')
        axes[0, 1].set_xlabel('Height (pixels)')
        axes[0, 1].set_ylabel('Frequency')
        
        # Scatter plot width vs height
        axes[1, 0].scatter(self.df['width'], self.df['height'], alpha=0.5, s=1)
        axes[1, 0].set_title('Width vs Height', fontsize=12, fontweight='bold')
        axes[1, 0].set_xlabel('Width (pixels)')
        axes[1, 0].set_ylabel('Height (pixels)')
        
        # Aspect ratio distribution
        self.df['aspect_ratio'].hist(bins=50, ax=axes[1, 1], color='lightgreen', edgecolor='black')
        axes[1, 1].set_title('Aspect Ratio Distribution', fontsize=12, fontweight='bold')
        axes[1, 1].set_xlabel('Aspect Ratio (width/height)')
        axes[1, 1].set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "image_dimensions.png", dpi=300, bbox_inches='tight')
        print(f"\nSaved: image_dimensions.png")
        plt.close()
        
        # Dimensions by class
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        for class_name in self.classes:
            class_data = self.df[self.df['class'] == class_name]
            axes[0].scatter(class_data['width'], class_data['height'], 
                          alpha=0.5, label=class_name, s=2)
        
        axes[0].set_title('Image Dimensions by Class', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Width (pixels)')
        axes[0].set_ylabel('Height (pixels)')
        axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
        
        # Box plot of aspect ratios by class
        self.df.boxplot(column='aspect_ratio', by='class', ax=axes[1])
        axes[1].set_title('Aspect Ratio by Class', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Document Class')
        axes[1].set_ylabel('Aspect Ratio')
        plt.suptitle('')  # Remove automatic title
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "dimensions_by_class.png", dpi=300, bbox_inches='tight')
        print(f"Saved: dimensions_by_class.png")
        plt.close()
    
    def analyze_file_sizes(self):
        """Analyze file size distribution"""
        print()
        print_header("FILE SIZE ANALYSIS")
        
        # Convert to MB
        self.df['size_mb'] = self.df['size_bytes'] / (1024 * 1024)
        
        print(f"\nFile Size Statistics (MB):")
        print(f"  Mean: {self.df['size_mb'].mean():.3f}")
        print(f"  Median: {self.df['size_mb'].median():.3f}")
        print(f"  Min: {self.df['size_mb'].min():.3f}")
        print(f"  Max: {self.df['size_mb'].max():.3f}")
        print(f"  Total: {self.df['size_mb'].sum():.2f} MB")
        
        # Visualization
        fig, ax = plt.subplots(figsize=(12, 6))
        
        self.df['size_mb'].hist(bins=50, ax=ax, color='steelblue', edgecolor='black')
        ax.set_title('File Size Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('File Size (MB)')
        ax.set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "file_sizes.png", dpi=300, bbox_inches='tight')
        print(f"\nSaved: file_sizes.png")
        plt.close()
    
    def analyze_image_modes(self):
        """Analyze image color modes"""
        print()
        print_header("IMAGE MODE ANALYSIS")
        
        mode_counts = self.df['mode'].value_counts()
        
        print(f"\nImage Modes:")
        for mode, count in mode_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"  {mode:10s}: {count:6d} ({percentage:5.2f}%)")
        
        # Visualization
        fig, ax = plt.subplots(figsize=(10, 6))
        
        mode_counts.plot(kind='bar', ax=ax, color='coral')
        ax.set_title('Image Mode Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('Image Mode', fontsize=12)
        ax.set_ylabel('Number of Images', fontsize=12)
        ax.tick_params(axis='x', rotation=0)
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "image_modes.png", dpi=300, bbox_inches='tight')
        print(f"\nSaved: image_modes.png")
        plt.close()
    
    def visualize_sample_images(self, samples_per_class=3):
        """Visualize sample images from each class"""
        print()
        print_header("SAMPLE IMAGE VISUALIZATION")
        
        fig, axes = plt.subplots(len(self.classes), samples_per_class, 
                                figsize=(samples_per_class * 3, len(self.classes) * 3))
        
        for i, class_name in enumerate(self.classes):
            class_data = self.df[self.df['class'] == class_name]
            sample_images = class_data.sample(n=min(samples_per_class, len(class_data)))
            
            for j, (_, row) in enumerate(sample_images.iterrows()):
                img_path = self.dataset_path / class_name / row['filename']
                try:
                    img = Image.open(img_path)
                    if len(self.classes) == 1:
                        ax = axes[j]
                    else:
                        ax = axes[i, j]
                    ax.imshow(img, cmap='gray' if img.mode == 'L' else None)
                    ax.set_title(f"{class_name}", fontsize=8)
                    ax.axis('off')
                    img.close()
                except Exception as e:
                    print(f"Error loading {img_path}: {e}")
        
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "sample_images.png", dpi=300, bbox_inches='tight')
        print(f"\nSaved: sample_images.png")
        plt.close()
    
    def generate_summary_report(self):
        """Generate comprehensive summary report"""
        print()
        print_header("EDA SUMMARY REPORT")
        
        report = {
            'dataset_path': str(self.dataset_path),
            'total_images': len(self.df),
            'total_classes': len(self.classes),
            'classes': self.classes,
            'class_distribution': self.df['class'].value_counts().to_dict(),
            'image_statistics': {
                'width': {
                    'mean': float(self.df['width'].mean()),
                    'median': float(self.df['width'].median()),
                    'min': int(self.df['width'].min()),
                    'max': int(self.df['width'].max()),
                    'std': float(self.df['width'].std())
                },
                'height': {
                    'mean': float(self.df['height'].mean()),
                    'median': float(self.df['height'].median()),
                    'min': int(self.df['height'].min()),
                    'max': int(self.df['height'].max()),
                    'std': float(self.df['height'].std())
                },
                'aspect_ratio': {
                    'mean': float(self.df['aspect_ratio'].mean()),
                    'median': float(self.df['aspect_ratio'].median()),
                    'min': float(self.df['aspect_ratio'].min()),
                    'max': float(self.df['aspect_ratio'].max())
                }
            },
            'file_size_mb': {
                'mean': float(self.df['size_mb'].mean()),
                'median': float(self.df['size_mb'].median()),
                'total': float(self.df['size_mb'].sum())
            },
            'image_modes': self.df['mode'].value_counts().to_dict()
        }
        
        # Save report
        with open(OUTPUT_DIR / "eda_report.json", "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"\nSaved: eda_report.json")
        
        # Print key findings
        print(f"\nKEY FINDINGS:")
        print(f"  - Dataset contains {len(self.df)} images across {len(self.classes)} classes")
        print(f"  - Average image dimensions: {report['image_statistics']['width']['mean']:.0f}x{report['image_statistics']['height']['mean']:.0f} pixels")
        print(f"  - Total dataset size: {report['file_size_mb']['total']:.2f} MB")
        print(f"  - Most common image mode: {max(report['image_modes'], key=report['image_modes'].get)}")
        
        return report
    
    def run_full_eda(self, sample_size=None):
        """Run complete EDA pipeline"""
        print_header("STARTING EXPLORATORY DATA ANALYSIS")
        
        # Collect data
        self.collect_image_data(sample_size=sample_size)
        
        # Run analyses
        self.analyze_class_distribution()
        self.analyze_image_dimensions()
        self.analyze_file_sizes()
        self.analyze_image_modes()
        
        # Visualize samples (limited to avoid memory issues)
        if len(self.df) < 10000:  # Only if dataset is manageable
            self.visualize_sample_images(samples_per_class=2)
        
        # Generate report
        report = self.generate_summary_report()
        
        print()
        print_header("EDA COMPLETE - All visualizations and reports saved")
        
        return report


def main():
    # Configuration
    DATASET_PATH = r"c:\Users\grant\AMFAM\rvlcdip_dataset\test"
    
    # Run EDA (sample_size=None for full dataset, or set a number for faster analysis)
    eda = DocumentDatasetEDA(r"c:\Users\grant\AMFAM\rvlcdip_dataset\test")
    
    # For full dataset analysis (may take time with 40k images)
    report = eda.run_full_eda(sample_size=None)
    
    print("\nEDA Analysis Complete!")


if __name__ == "__main__":
    main()
