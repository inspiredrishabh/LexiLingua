import cv2
import numpy as np
from PIL import Image
import pytesseract
import easyocr
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import os
import logging
from typing import List, Dict, Union, Optional
import json

class TextExtractor:
    """
    A comprehensive text extraction tool that can extract text from images and PDFs,
    including handwritten content using multiple OCR engines.
    """
    
    def __init__(self):
        """Initialize the TextExtractor with OCR engines."""
        self.setup_logging()
        
        # Initialize EasyOCR reader (supports handwritten text better)
        try:
            self.easyocr_reader = easyocr.Reader(['en'])
            self.logger.info("EasyOCR initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize EasyOCR: {e}")
            self.easyocr_reader = None
        
        # Set Tesseract path (you may need to adjust this based on your installation)
        # For Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
        try:
            # Common Windows paths for Tesseract
            possible_paths = [
                r'C:\Program Files\Tesseract-OCR\tesseract.exe',
                r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
                r'C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME'))
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    pytesseract.pytesseract.tesseract_cmd = path
                    break
            
            # Test Tesseract
            pytesseract.get_tesseract_version()
            self.logger.info("Tesseract initialized successfully")
        except Exception as e:
            self.logger.warning(f"Tesseract setup issue: {e}")
    
    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def preprocess_image(self, image: np.ndarray) -> List[np.ndarray]:
        """
        Preprocess image to improve OCR accuracy.
        Returns multiple versions of the processed image.
        """
        processed_images = []
        
        # Original image
        processed_images.append(image)
        
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        processed_images.append(gray)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        processed_images.append(blurred)
        
        # Apply threshold to get binary image
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        processed_images.append(thresh)
        
        # Morphological operations to clean up the image
        kernel = np.ones((2, 2), np.uint8)
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        processed_images.append(morph)
        
        # Enhance contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        processed_images.append(enhanced)
        
        return processed_images
    
    def extract_text_tesseract(self, image: np.ndarray, config: str = '') -> Dict[str, str]:
        """Extract text using Tesseract OCR with different configurations."""
        results = {}
        
        # Default configuration
        try:
            text = pytesseract.image_to_string(image, config=config)
            results['default'] = text.strip()
        except Exception as e:
            self.logger.error(f"Tesseract default extraction failed: {e}")
            results['default'] = ""
        
        # Configuration for better handwriting recognition
        try:
            handwriting_config = '--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
            text = pytesseract.image_to_string(image, config=handwriting_config)
            results['handwriting'] = text.strip()
        except Exception as e:
            self.logger.error(f"Tesseract handwriting extraction failed: {e}")
            results['handwriting'] = ""
        
        return results
    
    def extract_text_easyocr(self, image: np.ndarray) -> str:
        """Extract text using EasyOCR (better for handwritten text)."""
        if self.easyocr_reader is None:
            return ""
        
        try:
            results = self.easyocr_reader.readtext(image)
            text_parts = []
            for (bbox, text, confidence) in results:
                if confidence > 0.1:  # Only include results with reasonable confidence
                    text_parts.append(text)
            return ' '.join(text_parts)
        except Exception as e:
            self.logger.error(f"EasyOCR extraction failed: {e}")
            return ""
    
    def extract_from_image(self, image_path: str) -> Dict[str, str]:
        """
        Extract text from an image file using multiple methods.
        """
        self.logger.info(f"Processing image: {image_path}")
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        # Preprocess image
        processed_images = self.preprocess_image(image)
        
        results = {
            'file_path': image_path,
            'tesseract_results': {},
            'easyocr_results': {},
            'combined_text': ''
        }
        
        best_texts = []
        
        # Try Tesseract on different processed versions
        for i, proc_img in enumerate(processed_images):
            tesseract_result = self.extract_text_tesseract(proc_img)
            results['tesseract_results'][f'version_{i}'] = tesseract_result
            
            # Collect non-empty results
            for method, text in tesseract_result.items():
                if text and len(text.strip()) > 0:
                    best_texts.append(text)
        
        # Try EasyOCR on original and best processed versions
        for i, proc_img in enumerate([processed_images[0], processed_images[3]]):  # original and threshold
            easyocr_result = self.extract_text_easyocr(proc_img)
            results['easyocr_results'][f'version_{i}'] = easyocr_result
            
            if easyocr_result and len(easyocr_result.strip()) > 0:
                best_texts.append(easyocr_result)
        
        # Combine results (choose the longest meaningful text)
        if best_texts:
            # Filter out very short or garbage texts
            valid_texts = [text for text in best_texts if len(text.strip()) > 15 and self._is_meaningful_text(text)]
            if valid_texts:
                # Sort by length and take the longest result
                valid_texts.sort(key=len, reverse=True)
                results['combined_text'] = self._clean_extracted_text(valid_texts[0])
            else:
                # If no valid texts, try with original texts but warn
                best_texts.sort(key=len, reverse=True)
                results['combined_text'] = f"Text extraction quality is poor. Extracted: {best_texts[0][:100]}..."
        else:
            results['combined_text'] = "No readable text could be extracted from this image. Please ensure the image is clear, well-lit, and contains readable text."
        
        return results
    
    def _is_meaningful_text(self, text: str) -> bool:
        """Check if extracted text appears to be meaningful."""
        if not text or len(text.strip()) < 10:
            return False
        
        # Count alphanumeric characters vs special characters
        alphanumeric = sum(c.isalnum() or c.isspace() for c in text)
        total = len(text)
        
        # If more than 70% is alphanumeric/space, consider it meaningful
        return (alphanumeric / total) > 0.7
    
    def _clean_extracted_text(self, text: str) -> str:
        """Clean and normalize extracted text."""
        if not text:
            return "No text extracted"
        
        # Remove excessive whitespace and clean up
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 1:  # Filter out very short lines
                cleaned_lines.append(line)
        
        cleaned_text = '\n'.join(cleaned_lines)
        
        # If still too short, return appropriate message
        if len(cleaned_text.strip()) < 15:
            return "The extracted text appears to be incomplete or unclear. Please try with a higher quality image."
        
        return cleaned_text
    
    def extract_from_pdf(self, pdf_path: str, use_ocr: bool = True) -> Dict[str, Union[str, List[Dict]]]:
        """
        Extract text from PDF file.
        First tries direct text extraction, then OCR if needed.
        """
        self.logger.info(f"Processing PDF: {pdf_path}")
        
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        results = {
            'file_path': pdf_path,
            'direct_text': '',
            'ocr_text': '',
            'page_results': [],
            'combined_text': ''
        }
        
        try:
            # Open PDF
            doc = fitz.open(pdf_path)
            
            direct_text_parts = []
            ocr_text_parts = []
            
            for page_num in range(doc.page_count):
                page = doc[page_num]
                page_result = {
                    'page_number': page_num + 1,
                    'direct_text': '',
                    'ocr_text': ''
                }
                
                # Try direct text extraction first
                direct_text = page.get_text()
                page_result['direct_text'] = direct_text
                direct_text_parts.append(direct_text)
                
                # If direct extraction yields little text and OCR is enabled, use OCR
                if use_ocr and (not direct_text or len(direct_text.strip()) < 50):
                    try:
                        # Convert PDF page to image
                        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
                        img_data = pix.tobytes("png")
                        
                        # Convert to numpy array
                        nparr = np.frombuffer(img_data, np.uint8)
                        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                        
                        # Extract text using OCR
                        ocr_result = self.extract_from_image_array(image)
                        page_result['ocr_text'] = ocr_result['combined_text']
                        ocr_text_parts.append(ocr_result['combined_text'])
                        
                    except Exception as e:
                        self.logger.error(f"OCR failed for page {page_num + 1}: {e}")
                        page_result['ocr_text'] = ""
                
                results['page_results'].append(page_result)
            
            doc.close()
            
            # Combine results
            results['direct_text'] = '\n'.join(direct_text_parts)
            results['ocr_text'] = '\n'.join(ocr_text_parts)
            
            # Choose the best result
            if results['direct_text'].strip():
                results['combined_text'] = results['direct_text']
            else:
                results['combined_text'] = results['ocr_text']
                
        except Exception as e:
            self.logger.error(f"PDF processing failed: {e}")
            raise
        
        return results
    
    def extract_from_image_array(self, image: np.ndarray) -> Dict[str, str]:
        """Extract text from numpy image array."""
        processed_images = self.preprocess_image(image)
        
        results = {
            'tesseract_results': {},
            'easyocr_results': {},
            'combined_text': ''
        }
        
        best_texts = []
        
        # Try Tesseract
        for i, proc_img in enumerate(processed_images):
            tesseract_result = self.extract_text_tesseract(proc_img)
            results['tesseract_results'][f'version_{i}'] = tesseract_result
            
            for method, text in tesseract_result.items():
                if text and len(text.strip()) > 0:
                    best_texts.append(text)
        
        # Try EasyOCR
        for i, proc_img in enumerate([processed_images[0], processed_images[3]]):
            easyocr_result = self.extract_text_easyocr(proc_img)
            results['easyocr_results'][f'version_{i}'] = easyocr_result
            
            if easyocr_result and len(easyocr_result.strip()) > 0:
                best_texts.append(easyocr_result)
        
        # Choose the best result
        if best_texts:
            best_texts.sort(key=len, reverse=True)
            results['combined_text'] = best_texts[0]
        
        return results
    
    def extract_text(self, file_path: str, output_format: str = 'text') -> Union[str, Dict]:
        """
        Main method to extract text from either image or PDF.
        
        Args:
            file_path: Path to the file
            output_format: 'text' for plain text, 'detailed' for detailed results
        
        Returns:
            Extracted text or detailed results dictionary
        """
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif']:
            results = self.extract_from_image(file_path)
        elif file_ext == '.pdf':
            results = self.extract_from_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
        
        if output_format == 'text':
            return results['combined_text']
        else:
            return results
    
    def save_results(self, results: Dict, output_path: str):
        """Save extraction results to a JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        self.logger.info(f"Results saved to: {output_path}")


def main():
    """Example usage of the TextExtractor."""
    extractor = TextExtractor()
    
    # Example usage
    print("Text Extraction Tool")
    print("=" * 50)
    
    file_path = input("Enter the path to your image or PDF file: ").strip()
    
    if not file_path:
        print("No file path provided. Exiting.")
        return
    
    try:
        # Extract text
        print("\nExtracting text...")
        detailed_results = extractor.extract_text(file_path, output_format='detailed')
        
        # Display results
        print("\n" + "=" * 50)
        print("EXTRACTED TEXT:")
        print("=" * 50)
        print(detailed_results['combined_text'])
        
        # Save detailed results
        output_file = f"extraction_results_{os.path.basename(file_path)}.json"
        extractor.save_results(detailed_results, output_file)
        
        print(f"\nDetailed results saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
