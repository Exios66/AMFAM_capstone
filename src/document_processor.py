"""
Document Intelligence Pipeline - Data Preparation Module with File Output
Accepts PDF files and outputs 300 DPI optimized images + JSON with spatial coordinates
for downstream LLM processing.
"""

import io
import sys
import time
import json
import shutil
from pathlib import Path
from typing import Union, List, Dict, Any, Optional
import logging

from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Tesseract path for Windows
# Update this path if Tesseract is installed in a different location
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if Path(TESSERACT_PATH).is_file():
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
elif shutil.which(pytesseract.pytesseract.tesseract_cmd) is None:
    logger.warning(
        f"Tesseract not found at {TESSERACT_PATH} nor on PATH as "
        f"'{pytesseract.pytesseract.tesseract_cmd}'. OCR calls will fail until it is installed "
        f"or TESSERACT_PATH is updated."
    )


class DocumentProcessingError(Exception):
    """Raised when a document cannot be converted, OCR'd, or written to disk."""


class DocumentProcessor:
    """
    Document processor that saves 300 DPI images and JSON with spatial coordinates.
    Supports both local files and byte streams.
    """
    
    def __init__(self, output_dir: Union[str, Path], dpi: int = 300):
        """
        Initialize the document processor.
        
        Args:
            output_dir: Directory to save processed images and JSON files
            dpi: Target DPI for image conversion (default: 300)
        """
        self.output_dir = Path(output_dir)
        self.dpi = dpi
        
        # Create output directories
        self.images_dir = self.output_dir / "images"
        self.json_dir = self.output_dir / "json"
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.json_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"DocumentProcessor initialized")
        logger.info(f"Output directory: {self.output_dir}")
        logger.info(f"Target DPI: {dpi}")
    
    def _convert_pdf_to_images(
        self, 
        pdf_input: Union[str, Path, bytes],
        is_bytes: bool = False
    ) -> List[Image.Image]:
        """
        Convert PDF to images at specified DPI.
        
        Args:
            pdf_input: Either file path (str/Path) or bytes
            is_bytes: True if input is bytes, False if file path
            
        Returns:
            List of PIL Image objects
        """
        start_time = time.time()
        
        try:
            if is_bytes:
                logger.info("Converting PDF from bytes to images")
                images = convert_from_bytes(
                    pdf_input,
                    dpi=self.dpi,
                    thread_count=4
                )
            else:
                logger.info(f"Converting PDF from path to images: {pdf_input}")
                images = convert_from_path(
                    pdf_input,
                    dpi=self.dpi,
                    thread_count=4
                )
            
            conversion_time = time.time() - start_time
            logger.info(f"Converted {len(images)} pages in {conversion_time:.2f}s")
            return images
            
        except Exception:
            logger.exception("PDF conversion failed")
            raise
    
    def _load_tiff_image(self, image_path: Union[str, Path]) -> Image.Image:
        """
        Load TIFF image directly.
        
        Args:
            image_path: Path to TIFF file
            
        Returns:
            PIL Image object
        """
        logger.info(f"Loading TIFF image: {image_path}")
        try:
            return Image.open(image_path)
        except (OSError, ValueError) as e:
            raise DocumentProcessingError(f"Could not open TIFF image {image_path}: {e}") from e
    
    def _optimize_image(self, image: Image.Image) -> Image.Image:
        """
        Optimize image: convert to grayscale and resize to target DPI.
        
        Args:
            image: PIL Image object
            
        Returns:
            Optimized grayscale PIL Image at target DPI
        """
        # Convert to grayscale
        grayscale_image = image.convert('L')
        
        # Get current DPI or assume default
        current_dpi = None
        if hasattr(image, 'info') and 'dpi' in image.info:
            dpi_info = image.info['dpi']
            current_dpi = dpi_info[0] if isinstance(dpi_info, tuple) else dpi_info
        
        # If DPI metadata is missing or unusable, assume 72 DPI (common default)
        if not isinstance(current_dpi, (int, float)) or current_dpi <= 0:
            if current_dpi is not None:
                logger.warning(f"Ignoring invalid DPI metadata {current_dpi!r}")
            current_dpi = 72
            logger.info(f"No DPI metadata found, assuming {current_dpi} DPI")
        
        # Resize to target DPI
        if current_dpi != self.dpi:
            # Calculate scaling factor
            scale_factor = self.dpi / current_dpi
            new_width = int(image.width * scale_factor)
            new_height = int(image.height * scale_factor)
            
            # Resize image
            grayscale_image = grayscale_image.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            logger.info(f"Resized image from {current_dpi} DPI to {self.dpi} DPI: {image.width}x{image.height} -> {new_width}x{new_height}")
        
        return grayscale_image
    
    def _save_image(self, image: Image.Image, document_name: str, page_num: int) -> Path:
        """
        Save optimized image to disk at 300 DPI.
        
        Args:
            image: PIL Image object
            document_name: Base name for the document
            page_num: Page number
            
        Returns:
            Path to saved image
        """
        image_filename = f"{document_name}_page_{page_num:04d}.png"
        image_path = self.images_dir / image_filename
        
        # Save with DPI metadata
        try:
            image.save(image_path, dpi=(self.dpi, self.dpi))
        except OSError as e:
            raise DocumentProcessingError(f"Could not save image to {image_path}: {e}") from e
        logger.debug(f"Saved image: {image_path}")
        
        return image_path
    
    def _extract_ocr_with_bounding_boxes(
        self, 
        image: Image.Image
    ) -> List[Dict[str, Any]]:
        """
        Extract text and bounding boxes using PyTesseract.
        
        Args:
            image: PIL Image object (grayscale)
            
        Returns:
            List of word objects with text and bounding boxes
            Format: [{"text": "word", "bounding_box": [x, y, x1, y1]}]
        """
        # Get OCR data with spatial information
        try:
            ocr_data = pytesseract.image_to_data(
                image,
                output_type=pytesseract.Output.DICT,
                config='--psm 6'
            )
        except pytesseract.TesseractNotFoundError as e:
            raise DocumentProcessingError(
                "Tesseract executable not found. Install Tesseract OCR or update TESSERACT_PATH "
                f"in {__name__}."
            ) from e
        except pytesseract.TesseractError as e:
            raise DocumentProcessingError(f"Tesseract failed to process image: {e}") from e
        
        words_with_boxes = []
        n_boxes = len(ocr_data['text'])
        
        for i in range(n_boxes):
            text = ocr_data['text'][i].strip()
            if text:  # Skip empty entries
                x = int(ocr_data['left'][i])
                y = int(ocr_data['top'][i])
                width = int(ocr_data['width'][i])
                height = int(ocr_data['height'][i])
                
                # Convert to [x, y, x1, y1] format
                bounding_box = [x, y, x + width, y + height]
                
                word_obj = {
                    "text": text,
                    "bounding_box": bounding_box
                }
                words_with_boxes.append(word_obj)
        
        return words_with_boxes
    
    def _save_json(self, data: Dict[str, Any], document_name: str) -> Path:
        """
        Save JSON results to disk.
        
        Args:
            data: Dictionary with OCR results
            document_name: Base name for the document
            
        Returns:
            Path to saved JSON file
        """
        json_filename = f"{document_name}_ocr_results.json"
        json_path = self.json_dir / json_filename
        
        try:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except OSError as e:
            raise DocumentProcessingError(f"Could not write JSON to {json_path}: {e}") from e
        
        logger.info(f"Saved JSON: {json_path}")
        return json_path
    
    def process_pdf(
        self,
        pdf_input: Union[str, Path, bytes],
        document_name: Optional[str] = None,
        is_bytes: bool = False
    ) -> Dict[str, Any]:
        """
        Process PDF document, save images and JSON with spatial coordinates.
        
        Args:
            pdf_input: Either file path (str/Path) or bytes
            document_name: Base name for output files (auto-generated if None)
            is_bytes: True if input is bytes, False if file path
            
        Returns:
            Dictionary with processing summary and file paths
        """
        start_time = time.time()
        logger.info("="*60)
        logger.info("Starting PDF processing with file output")
        logger.info("="*60)
        
        try:
            # Generate document name if not provided
            if document_name is None:
                if is_bytes:
                    document_name = f"document_{int(time.time())}"
                else:
                    document_name = Path(pdf_input).stem
            
            # Step 1: Convert PDF to images
            images = self._convert_pdf_to_images(pdf_input, is_bytes)
            
            # Step 2 & 3: Optimize images, save them, and extract OCR data
            pages_data = []
            saved_images = []
            
            for page_num, image in enumerate(images, start=1):
                page_start = time.time()
                
                # Optimize image
                optimized_image = self._optimize_image(image)
                
                # Save optimized image at 300 DPI
                image_path = self._save_image(optimized_image, document_name, page_num)
                saved_images.append(str(image_path))
                
                # Extract OCR with bounding boxes
                words = self._extract_ocr_with_bounding_boxes(optimized_image)
                
                page_data = {
                    "page_number": page_num,
                    "image_path": str(image_path),
                    "words": words
                }
                pages_data.append(page_data)
                
                page_time = time.time() - page_start
                logger.info(f"Page {page_num}: {len(words)} words extracted in {page_time:.2f}s")
            
            # Step 4: Structure and save JSON output
            total_time = time.time() - start_time
            
            result_data = {
                "document_info": {
                    "document_name": document_name,
                    "total_pages": len(images),
                    "dpi": self.dpi,
                    "processing_time_seconds": round(total_time, 2),
                    "total_words_extracted": sum(len(page["words"]) for page in pages_data)
                },
                "pages": pages_data
            }
            
            # Save JSON to file
            json_path = self._save_json(result_data, document_name)
            
            # Return summary
            summary = {
                "status": "success",
                "document_name": document_name,
                "total_pages": len(images),
                "total_words": result_data["document_info"]["total_words_extracted"],
                "processing_time_seconds": round(total_time, 2),
                "images_directory": str(self.images_dir),
                "json_file": str(json_path),
                "saved_images": saved_images
            }
            
            logger.info(f"Processing complete: {total_time:.2f}s total")
            logger.info(f"Images saved to: {self.images_dir}")
            logger.info(f"JSON saved to: {json_path}")
            
            return summary
            
        except Exception:
            logger.exception(f"PDF processing failed for {document_name or pdf_input!r}")
            raise
    
    def process_tiff(
        self,
        tiff_path: Union[str, Path],
        document_name: Optional[str] = None,
        class_label: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process TIFF image, save optimized image and JSON with spatial coordinates.
        
        Args:
            tiff_path: Path to TIFF file
            document_name: Base name for output files (auto-generated if None)
            class_label: Optional class label for the document
            
        Returns:
            Dictionary with processing summary and file paths
        """
        start_time = time.time()
        logger.info("="*60)
        logger.info("Starting TIFF processing with file output")
        logger.info("="*60)
        
        try:
            # Generate document name if not provided
            if document_name is None:
                document_name = Path(tiff_path).stem
            
            # Step 1: Load TIFF image
            image = self._load_tiff_image(tiff_path)
            
            # Step 2: Optimize image
            optimized_image = self._optimize_image(image)
            
            # Step 3: Save optimized image
            image_path = self._save_image(optimized_image, document_name, 1)
            
            # Step 4: Extract OCR with bounding boxes
            words = self._extract_ocr_with_bounding_boxes(optimized_image)
            
            # Step 5: Structure and save JSON output
            total_time = time.time() - start_time
            
            page_data = {
                "page_number": 1,
                "image_path": str(image_path),
                "words": words
            }
            
            result_data = {
                "document_info": {
                    "document_name": document_name,
                    "class_label": class_label,
                    "total_pages": 1,
                    "dpi": self.dpi,
                    "processing_time_seconds": round(total_time, 2),
                    "total_words_extracted": len(words)
                },
                "pages": [page_data]
            }
            
            # Save JSON to file
            json_path = self._save_json(result_data, document_name)
            
            # Return summary
            summary = {
                "status": "success",
                "document_name": document_name,
                "class_label": class_label,
                "total_pages": 1,
                "total_words": len(words),
                "processing_time_seconds": round(total_time, 2),
                "images_directory": str(self.images_dir),
                "json_file": str(json_path),
                "saved_images": [str(image_path)]
            }
            
            logger.info(f"Processing complete: {total_time:.2f}s total")
            logger.info(f"Words extracted: {len(words)}")
            logger.info(f"Image saved to: {image_path}")
            logger.info(f"JSON saved to: {json_path}")
            
            return summary
            
        except Exception:
            logger.exception(f"TIFF processing failed for {tiff_path}")
            raise


class BatchProcessor:
    """
    Batch processor for multiple PDF documents.
    """
    
    def __init__(self, input_dir: Union[str, Path], output_dir: Union[str, Path], dpi: int = 300):
        """
        Initialize batch processor.
        
        Args:
            input_dir: Directory containing PDF files
            output_dir: Directory to save processed files
            dpi: Target DPI for image conversion
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.dpi = dpi
        
        # Create processor instance
        self.processor = DocumentProcessor(output_dir, dpi)
        
        logger.info(f"BatchProcessor initialized")
        logger.info(f"Input directory: {self.input_dir}")
        logger.info(f"Output directory: {self.output_dir}")
    
    def process_batch(self) -> List[Dict[str, Any]]:
        """
        Process all PDF files in the input directory.
        
        Returns:
            List of processing summaries for each document
        """
        logger.info("="*60)
        logger.info("Starting batch processing")
        logger.info("="*60)
        
        # Find all PDF files
        pdf_files = list(self.input_dir.glob("*.pdf"))
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {self.input_dir}")
            return []
        
        logger.info(f"Found {len(pdf_files)} PDF files to process")
        
        results = []
        for pdf_path in pdf_files:
            try:
                result = self.processor.process_pdf(pdf_path, document_name=pdf_path.stem)
                results.append(result)
            except Exception as e:
                logger.exception(f"Error processing {pdf_path.name}")
                results.append({
                    "status": "error",
                    "document_name": pdf_path.stem,
                    "error_type": type(e).__name__,
                    "error": str(e)
                })
        
        # Log summary
        successful = sum(1 for r in results if r['status'] == 'success')
        failed = len(results) - successful
        
        logger.info(f"Batch processing complete: {successful} successful, {failed} failed")
        if failed:
            logger.warning(f"{failed} of {len(results)} documents failed; see 'error' entries in results")
        
        return results


class ClassOrganizedBatchProcessor:
    """
    Batch processor for class-organized TIFF directories.
    Processes TIFF images organized in class subdirectories.
    """
    
    def __init__(self, input_dir: Union[str, Path], output_dir: Union[str, Path], dpi: int = 300):
        """
        Initialize class-organized batch processor.
        
        Args:
            input_dir: Directory containing class subdirectories with TIFF files
            output_dir: Directory to save processed files
            dpi: Target DPI for image processing
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.dpi = dpi
        
        # Create processor instance
        self.processor = DocumentProcessor(output_dir, dpi)
        
        logger.info(f"ClassOrganizedBatchProcessor initialized")
        logger.info(f"Input directory: {self.input_dir}")
        logger.info(f"Output directory: {self.output_dir}")
    
    def process_batch(self) -> List[Dict[str, Any]]:
        """
        Process all TIFF files in class-organized subdirectories.
        
        Returns:
            List of processing summaries for each document
        """
        logger.info("="*60)
        logger.info("Starting class-organized batch processing")
        logger.info("="*60)
        
        # Find all class subdirectories
        class_dirs = [d for d in self.input_dir.iterdir() if d.is_dir()]
        
        if not class_dirs:
            logger.warning(f"No class subdirectories found in {self.input_dir}")
            return []
        
        logger.info(f"Found {len(class_dirs)} class directories")
        
        results = []
        total_files = 0
        
        for class_dir in sorted(class_dirs):
            class_name = class_dir.name
            logger.info(f"\nProcessing class: {class_name}")
            
            # Find all TIFF files in class directory
            tiff_files = list(class_dir.glob("*.tif")) + list(class_dir.glob("*.tiff"))
            
            if not tiff_files:
                logger.warning(f"No TIFF files found in {class_dir}")
                continue
            
            logger.info(f"Found {len(tiff_files)} TIFF files in {class_name}")
            total_files += len(tiff_files)
            
            for tiff_path in tiff_files:
                try:
                    # Create unique document name including class
                    document_name = f"{class_name}_{tiff_path.stem}"
                    
                    result = self.processor.process_tiff(
                        tiff_path,
                        document_name=document_name,
                        class_label=class_name
                    )
                    results.append(result)
                    
                except Exception as e:
                    logger.exception(f"Error processing {tiff_path.name}")
                    results.append({
                        "status": "error",
                        "document_name": tiff_path.stem,
                        "class_label": class_name,
                        "error_type": type(e).__name__,
                        "error": str(e)
                    })
        
        # Log summary
        successful = sum(1 for r in results if r['status'] == 'success')
        failed = len(results) - successful
        
        logger.info("="*60)
        logger.info(f"Batch processing complete")
        logger.info(f"Total files processed: {total_files}")
        logger.info(f"Successful: {successful}, Failed: {failed}")
        logger.info("="*60)
        if failed:
            logger.warning(f"{failed} of {len(results)} documents failed; see 'error' entries in results")
        
        return results


# Convenience functions
def process_pdf_file(
    file_path: Union[str, Path],
    output_dir: Union[str, Path],
    dpi: int = 300
) -> Dict[str, Any]:
    """
    Process PDF from file path and save outputs.
    
    Args:
        file_path: Path to PDF file
        output_dir: Directory to save processed files
        dpi: Target DPI (default: 300)
        
    Returns:
        Processing summary
    """
    processor = DocumentProcessor(output_dir, dpi)
    return processor.process_pdf(file_path, is_bytes=False)


def process_pdf_bytes(
    pdf_bytes: bytes,
    document_name: str,
    output_dir: Union[str, Path],
    dpi: int = 300
) -> Dict[str, Any]:
    """
    Process PDF from bytes and save outputs.
    
    Args:
        pdf_bytes: PDF file as bytes
        document_name: Base name for output files
        output_dir: Directory to save processed files
        dpi: Target DPI (default: 300)
        
    Returns:
        Processing summary
    """
    processor = DocumentProcessor(output_dir, dpi)
    return processor.process_pdf(pdf_bytes, document_name=document_name, is_bytes=True)


def main() -> int:
    """Run the example single-file and batch workflows, returning a process exit code."""
    exit_code = 0

    # Single file processing
    print("Example: Process single PDF file")
    print("="*60)

    try:
        result = process_pdf_file(
            file_path=r"./input_documents/sample.pdf",
            output_dir=r"./processed_documents"
        )
        print(json.dumps(result, indent=2))
    except Exception:
        logger.exception("Single-file processing failed")
        exit_code = 1

    # Batch processing
    print("\nExample: Batch process directory")
    print("="*60)

    try:
        batch_processor = BatchProcessor(
            input_dir=r"./input_documents",
            output_dir=r"./processed_documents"
        )
        results = batch_processor.process_batch()
        print(f"Processed {len(results)} documents")
        if any(r["status"] != "success" for r in results):
            exit_code = 1
    except Exception:
        logger.exception("Batch processing failed")
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
