# ⚖️ LexiLingua: The Extraction Engine

This is the core text extraction engine powering our hackathon project, **LexiLingua**. This powerful Python tool is engineered to extract clean, usable text from a wide range of legal documents, including scanned contracts, digital PDFs, and even files with **handwritten notes and signatures**.

LexiLingua's extraction engine uses a multi-layered approach, combining Tesseract and EasyOCR, to ensure the highest possible accuracy. This forms the foundational first step of our legal analysis pipeline.

## ✨ Core Features

- **📷 Extract from Scanned Contracts & Evidence**: Supports PNG, JPG, JPEG, and other image formats.
- **📄 Process Digital & Scanned Legal Files**: Handles both native text and image-based (scanned) PDFs.
- **✍️ Decipher Handwritten Notes & Signatures**: Advanced OCR specifically optimized for handwritten content.
- **🎯 Multi-Engine Accuracy**: Intelligently combines multiple OCR engines for superior results on diverse documents.
- **🖼️ Automatic Image Preprocessing**: Enhances scans and photos of documents for optimal OCR accuracy.
- **🎨 User-Friendly GUI**: A clean Streamlit interface for quick testing and demonstration.
- **⌨️ Powerful Command Line Interface**: Designed for batch processing multiple legal files.
- **📊 Detailed JSON Output**: Provides confidence scores and methods used for analysis traceability.

## 🛠️ Installation

### Quick Setup (Windows)

1.  **Run the installation script:**
    ```cmd
    install.bat
    ```

### Manual Installation

1.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Install Tesseract OCR:**
    - **Windows:** Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki) and install to the default location.
    - **Linux:** `sudo apt-get install tesseract-ocr`
    - **macOS:** `brew install tesseract`

## 🚀 Usage

### 1. GUI Version (for Demonstration)

Launch the Streamlit web interface to easily upload and process a document.

```bash
streamlit run app.py
```

# Extract text from a rental agreement to the console

python cli_extractor.py "path/to/your/rental_agreement.pdf"

# Save text from a scanned contract to a file

python cli_extractor.py "scanned_contract.jpg" -o "contract_text.txt"

# Get detailed JSON results for a loan application

python cli_extractor.py "loan_application.pdf" -f json -o "loan_results.json"

# Use verbose output for a handwritten note

python cli_extractor.py "handwritten_note.png" -v

3. Python API (for Integration)
   from text_extractor import TextExtractor

# Initialize the extractor

extractor = TextExtractor()

# Extract text from a PDF

extracted_text = extractor.extract_text("terms_of_service.pdf")
print(extracted_text)

# Get detailed results from a scanned image

results = extractor.extract_text("affidavit.jpg", output_format='detailed')
print(results['combined_text'])

# Access analysis from a specific engine

print(results['easyocr_results'])

# 📁 Project Structure

LexiLingua/
├── text_extractor.py # The main extraction engine
├── app.py # Streamlit GUI for demonstration
├── cli_extractor.py # Command Line Interface
├── requirements.txt # Python dependencies
├── install.bat # Windows installation script
└── README.md # This file

# 🎯 How It Works

To handle the diverse quality of legal documents—from crisp digital PDFs to old, scanned, handwritten notes—this engine uses a multi-layered approach.

Direct Text Extraction: For native PDFs, text is pulled directly for perfect accuracy.

Tesseract OCR: Excellent for clean, printed text commonly found in official documents.

EasyOCR: Specialized for challenging, noisy, or handwritten text.

Intelligent Combination: The engine processes the file with multiple methods and selects the most coherent and complete text as the final output.

# 💡 Tips for Best Results

For Scanned Legal Documents
High Resolution: Scan documents at 300 DPI or higher.

Good Contrast: Ensure text is dark and the background is light and clean.

Straight Alignment: Avoid skewed or rotated pages.

For Handwritten Affidavits & Notes
Clear Writing: Neat, legible handwriting yields the best results.

Good Spacing: Avoid overlapping letters and words.

Dark Ink: Use a dark pen on light, unlined paper if possible.

# 🔧 Troubleshooting

Common Issues

1. "Tesseract not found" error:

Ensure Tesseract OCR is installed correctly and its location is in your system's PATH.

2. Poor extraction quality:

Check the source document's quality. A better scan or photo will dramatically improve results.

3. Memory issues with large multi-page PDFs:

Our engine processes page by page, but extremely high-resolution files can be memory intensive. Consider down-sampling if necessary.

# 🤝 Contributing

This is a hackathon project, but contributions are welcome! Feel free to report bugs or suggest improvements by creating an issue.

# 📄 License

This project is licensed under the MIT License.
