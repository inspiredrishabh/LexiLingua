# 🔍 Advanced Text Extractor

A powerful Python-based text extraction tool that can extract text from images and PDFs, including **handwritten content**. This tool uses multiple OCR engines (Tesseract and EasyOCR) to provide the best possible text extraction results.

## ✨ Features

- **📷 Image Text Extraction**: Supports PNG, JPG, JPEG, BMP, TIFF, GIF
- **📄 PDF Text Extraction**: Direct text extraction + OCR for scanned PDFs
- **✍️ Handwritten Text Recognition**: Advanced OCR for handwritten content
- **🎯 Multiple OCR Engines**: Combines Tesseract and EasyOCR for best results
- **🖼️ Image Preprocessing**: Automatic image enhancement for better accuracy
- **🎨 User-Friendly GUI**: Beautiful Streamlit web interface
- **⌨️ Command Line Interface**: Simple CLI for batch processing
- **📊 Detailed Analysis**: JSON output with confidence scores and methods used

## 🛠️ Installation

### Quick Setup (Windows)

1. **Run the installation script:**
   ```cmd
   install.bat
   ```

### Manual Installation

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Install Tesseract OCR:**

   **Windows:**

   - Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install to default location (usually `C:\Program Files\Tesseract-OCR\`)

   **Linux:**

   ```bash
   sudo apt-get install tesseract-ocr libtesseract-dev
   ```

   **macOS:**

   ```bash
   brew install tesseract
   ```

## 🚀 Usage

### 1. GUI Version (Recommended)

Launch the beautiful web interface:

```bash
streamlit run app.py
```

Features:

- Drag & drop file upload
- Real-time preview
- Multiple output formats
- Download results
- Detailed analysis

### 2. Command Line Interface

For batch processing or scripting:

```bash
# Extract text to console
python cli_extractor.py "path/to/your/file.pdf"

# Save text to file
python cli_extractor.py "input.jpg" -o "output.txt"

# Get detailed JSON results
python cli_extractor.py "document.pdf" -f json -o "results.json"

# Verbose output
python cli_extractor.py "image.png" -v
```

### 3. Interactive Python

```bash
python text_extractor.py
```

### 4. Python API

```python
from text_extractor import TextExtractor

# Initialize extractor
extractor = TextExtractor()

# Extract text (simple)
text = extractor.extract_text("document.pdf")
print(text)

# Extract with detailed results
results = extractor.extract_text("image.jpg", output_format='detailed')
print(results['combined_text'])

# Access detailed analysis
print(results['tesseract_results'])
print(results['easyocr_results'])
```

## 📁 Project Structure

```
Demystifying Legal Documents/
├── text_extractor.py     # Main extraction engine
├── app.py               # Streamlit GUI application
├── cli_extractor.py     # Command line interface
├── requirements.txt     # Python dependencies
├── install.bat         # Windows installation script
└── README.md           # This file
```

## 🎯 How It Works

### Multi-Engine Approach

1. **Tesseract OCR**: Great for printed text, multiple configurations
2. **EasyOCR**: Excellent for handwritten text and complex layouts
3. **Image Preprocessing**: Multiple enhancement techniques
4. **Smart Combination**: Automatically selects best results

### Image Preprocessing Pipeline

1. Grayscale conversion
2. Noise reduction (Gaussian blur)
3. Binary thresholding (OTSU)
4. Morphological operations
5. Contrast enhancement (CLAHE)

### PDF Processing

1. **Direct Text Extraction**: Fast extraction of selectable text
2. **OCR Fallback**: For scanned PDFs or images within PDFs
3. **Page-by-Page Analysis**: Detailed results for each page

## 📊 Output Formats

### Simple Text Output

```
This is the extracted text from your document...
```

### Detailed JSON Output

```json
{
  "file_path": "document.pdf",
  "combined_text": "Final extracted text...",
  "tesseract_results": {
    "version_0": { "default": "text1", "handwriting": "text2" },
    "version_1": { "default": "text3", "handwriting": "text4" }
  },
  "easyocr_results": {
    "version_0": "easyocr text 1",
    "version_1": "easyocr text 2"
  }
}
```

## 💡 Tips for Better Results

### Image Quality

- **High Resolution**: Use images with at least 300 DPI
- **Good Contrast**: Dark text on light background works best
- **Proper Lighting**: Avoid shadows and glare
- **Straight Alignment**: Keep text horizontal

### Handwritten Text

- **Clear Writing**: Neat, legible handwriting
- **Good Spacing**: Avoid overlapping characters
- **Dark Ink**: Use dark pen on light paper
- **Single Language**: Better results with consistent language

### PDF Documents

- **Original PDFs**: Best results with native PDF text
- **Scanned Quality**: High-resolution scans (300+ DPI)
- **Clean Pages**: Remove artifacts and noise

## 🔧 Troubleshooting

### Common Issues

**1. "Tesseract not found" error:**

- Install Tesseract OCR from the official source
- Ensure it's in your system PATH
- Check the installation path in `text_extractor.py`

**2. Poor text extraction quality:**

- Try different image preprocessing options
- Ensure good image quality and lighting
- Use higher resolution images
- Check if text is clearly visible

**3. Memory issues with large files:**

- Process files in smaller chunks
- Reduce image resolution if too high
- Close other applications to free memory

**4. Installation errors:**

- Update pip: `python -m pip install --upgrade pip`
- Use virtual environment
- Install packages one by one if batch install fails

### Performance Optimization

- **GPU Acceleration**: EasyOCR can use GPU for faster processing
- **Batch Processing**: Process multiple files together
- **Image Resizing**: Resize very large images to optimal size
- **Format Selection**: Use appropriate output format for your needs

## 🤝 Contributing

Contributions are welcome! Here are ways you can help:

1. **Report Bugs**: Create issues for any problems you encounter
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with enhancements
4. **Documentation**: Help improve documentation and examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Tesseract OCR**: Google's OCR engine
- **EasyOCR**: JaidedAI's OCR library
- **OpenCV**: Computer vision library
- **Streamlit**: Web app framework
- **PyMuPDF**: PDF processing library

## 📞 Support

If you encounter any issues or need help:

1. Check the troubleshooting section above
2. Review the installation requirements
3. Create an issue with detailed error information
4. Include your system information and file types

---

**Happy Text Extracting! 🎉**
