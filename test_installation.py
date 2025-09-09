#!/usr/bin/env python3
"""
Test script to verify the text extractor installation and functionality.
"""

import sys
import os
import tempfile
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_test_image():
    """Create a simple test image with text."""
    # Create a white image
    img = Image.new('RGB', (600, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        # This might not work on all systems
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        try:
            font = ImageFont.load_default()
        except:
            font = None
    
    # Add text to image
    text = "This is a test image for OCR.\nHello World! 123456789"
    draw.text((50, 50), text, fill='black', font=font)
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    img.save(temp_file.name)
    return temp_file.name

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    modules = [
        ('cv2', 'OpenCV'),
        ('numpy', 'NumPy'),
        ('PIL', 'Pillow'),
        ('pytesseract', 'PyTesseract'),
        ('easyocr', 'EasyOCR'),
        ('fitz', 'PyMuPDF'),
        ('pdf2image', 'PDF2Image'),
        ('streamlit', 'Streamlit')
    ]
    
    failed_imports = []
    
    for module, name in modules:
        try:
            __import__(module)
            print(f"✅ {name}: OK")
        except ImportError as e:
            print(f"❌ {name}: FAILED - {e}")
            failed_imports.append(name)
    
    return failed_imports

def test_extractor():
    """Test the text extractor functionality."""
    print("\nTesting TextExtractor...")
    
    try:
        from text_extractor import TextExtractor
        print("✅ TextExtractor imported successfully")
        
        # Initialize extractor
        extractor = TextExtractor()
        print("✅ TextExtractor initialized")
        
        # Create test image
        test_image_path = create_test_image()
        print(f"✅ Test image created: {test_image_path}")
        
        # Test text extraction
        result = extractor.extract_text(test_image_path, output_format='text')
        print(f"✅ Text extraction completed")
        print(f"📝 Extracted text: '{result.strip()}'")
        
        # Test detailed extraction
        detailed_result = extractor.extract_text(test_image_path, output_format='detailed')
        print("✅ Detailed extraction completed")
        
        # Clean up
        os.unlink(test_image_path)
        print("✅ Test image cleaned up")
        
        return True
        
    except Exception as e:
        print(f"❌ TextExtractor test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_tesseract():
    """Test Tesseract installation."""
    print("\nTesting Tesseract...")
    
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract version: {version}")
        return True
    except Exception as e:
        print(f"❌ Tesseract test failed: {e}")
        print("   Please install Tesseract OCR:")
        print("   Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        print("   Linux: sudo apt-get install tesseract-ocr")
        print("   macOS: brew install tesseract")
        return False

def test_easyocr():
    """Test EasyOCR installation."""
    print("\nTesting EasyOCR...")
    
    try:
        import easyocr
        reader = easyocr.Reader(['en'], verbose=False)
        print("✅ EasyOCR initialized successfully")
        return True
    except Exception as e:
        print(f"❌ EasyOCR test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Text Extractor Installation Test")
    print("=" * 50)
    
    # Test imports
    failed_imports = test_imports()
    
    if failed_imports:
        print(f"\n❌ Failed imports: {', '.join(failed_imports)}")
        print("Please install missing packages with: pip install -r requirements.txt")
        return False
    
    # Test Tesseract
    tesseract_ok = test_tesseract()
    
    # Test EasyOCR
    easyocr_ok = test_easyocr()
    
    # Test main functionality
    if tesseract_ok or easyocr_ok:  # At least one OCR engine should work
        extractor_ok = test_extractor()
    else:
        print("\n❌ No OCR engines available, skipping extractor test")
        extractor_ok = False
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    if not failed_imports and (tesseract_ok or easyocr_ok) and extractor_ok:
        print("🎉 ALL TESTS PASSED!")
        print("Your text extractor is ready to use!")
        print("\nNext steps:")
        print("1. GUI version: streamlit run app.py")
        print("2. CLI version: python cli_extractor.py <file>")
        print("3. Interactive: python text_extractor.py")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        print("Please check the error messages above and install missing dependencies.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
