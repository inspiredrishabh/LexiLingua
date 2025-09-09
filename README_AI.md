# ⚖️ AI-Powered Legal Document Analyzer

**Hackathon Project: Demystifying Legal Documents with AI**

A comprehensive AI-powered tool that helps people understand complex legal documents by providing clear, accessible explanations in plain language. This project combines advanced text extraction with Google's Gemini AI to break down legal jargon and empower informed decision-making.

## 🚀 Project Overview

Legal documents are often filled with complex, impenetrable jargon that creates information asymmetry. Our solution bridges this gap by:

- **Extracting text** from any document format (PDF, images, handwritten)
- **Analyzing content** with AI to identify key terms, risks, and obligations
- **Providing explanations** in simple, understandable language
- **Answering questions** about specific clauses or terms
- **Protecting privacy** with a process-and-forget architecture

## ✨ Key Features

### 🔍 Advanced Text Extraction

- **📷 Multi-format Support**: PDF, PNG, JPG, TIFF, handwritten documents
- **✍️ Handwritten Recognition**: Advanced OCR for handwritten content
- **🌍 Multi-language**: Supports documents in various languages
- **🎯 Dual OCR Engines**: Tesseract + EasyOCR for maximum accuracy

### 🧠 AI-Powered Analysis

- **📋 Document Classification**: Automatically identifies document types
- **🔑 Key Terms Simplified**: Breaks down complex legal language
- **🚨 Risk Identification**: Highlights potential red flags and concerns
- **💰 Financial Analysis**: Identifies costs, fees, and obligations
- **❓ Interactive Q&A**: Ask specific questions about your document
- **🌐 Multi-language Support**: Analysis in your preferred language

### 🔒 Privacy-First Design

- **✅ No Data Storage**: Documents processed and immediately deleted
- **✅ Local Processing**: Text extraction happens on your device
- **✅ Encrypted Communication**: Secure API calls to Gemini
- **✅ User Control**: You manage your own API key
- **✅ Transparent Code**: Open-source for full transparency

## 🛠️ Installation & Setup

### 1. Clone & Install Dependencies

```bash
# Clone the repository
git clone <repository-url>
cd "Demystifying Legal Documents"

# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install Python packages
pip install -r requirements.txt
```

### 2. Get Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a free API key
3. Keep it secure - you'll enter it in the app

### 3. Install Tesseract OCR (Optional but Recommended)

**Windows:**

- Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- Install to default location

**Linux:**

```bash
sudo apt-get install tesseract-ocr libtesseract-dev
```

**macOS:**

```bash
brew install tesseract
```

## 🚀 How to Use

### 1. Web Interface (Recommended)

Launch the beautiful AI-powered web interface:

```bash
streamlit run legal_app.py
```

**Features:**

- 🔑 Secure API key input
- 📁 Drag & drop document upload
- 🧠 Complete AI analysis with detailed reports
- ❓ Interactive Q&A about your document
- 🌍 Multi-language support
- 📊 Document statistics and insights
- 💾 Download analysis reports

### 2. Command Line Interface

For power users and automation:

```bash
# Complete AI analysis
python legal_cli.py contract.pdf --api-key YOUR_GEMINI_KEY

# Specify language
python legal_cli.py lease.jpg --api-key YOUR_KEY --language Spanish

# Ask specific questions
python legal_cli.py terms.pdf --api-key YOUR_KEY --question "What are the cancellation terms?"

# Extract text only (no AI)
python legal_cli.py document.pdf --api-key YOUR_KEY --extract-only

# Save results to file
python legal_cli.py contract.pdf --api-key YOUR_KEY --output report.md
```

### 3. Demo Mode

Try the demo to see all capabilities:

```bash
python demo.py
```

### 4. Original Text Extractor

For basic text extraction without AI:

```bash
streamlit run app.py
```

## 📁 Project Structure

```
Demystifying Legal Documents/
├── legal_document_analyzer.py  # Core AI analysis engine
├── legal_app.py               # AI-powered Streamlit app
├── legal_cli.py               # AI-powered command line
├── text_extractor.py          # Text extraction engine
├── app.py                     # Original text extractor GUI
├── cli_extractor.py           # Original CLI extractor
├── demo.py                    # Interactive demo
├── requirements.txt           # Python dependencies
├── install.bat               # Windows installation script
└── README.md                 # This file
```

## 🎯 How It Works

### 1. Text Extraction Pipeline

```
Document Input → Image Processing → OCR (Tesseract + EasyOCR) → Clean Text
```

### 2. AI Analysis Pipeline

```
Extracted Text → Language Detection → Gemini AI Analysis → Structured Report
```

### 3. Privacy Protection

```
Upload → Process → Analyze → Return Results → Delete All Data
```

## 📊 Analysis Features

### Document Understanding

- **Document Type**: Rental agreement, loan contract, terms of service, etc.
- **Key Parties**: Identifies all involved parties
- **Main Purpose**: What the document is for
- **Important Dates**: Deadlines, expiration dates, renewal dates

### Risk Analysis

- **Red Flags**: Potentially problematic clauses
- **Hidden Costs**: Fees, penalties, additional charges
- **Exit Clauses**: How to terminate or cancel the agreement
- **Your Rights**: What you're entitled to
- **Your Obligations**: What you must do

### Financial Breakdown

- **Payment Schedules**: When and how much to pay
- **Penalties**: Late fees, cancellation costs
- **Deposits**: Security deposits, advance payments
- **Consequences**: What happens if you don't comply

### Interactive Q&A

Ask questions like:

- "What happens if I break this contract?"
- "How much will this cost me in total?"
- "Can I cancel this agreement?"
- "What are my rights if something goes wrong?"

## 🌍 Multi-Language Support

### Supported Languages

- 🇺🇸 English
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇩🇪 German
- 🇮🇹 Italian
- 🇵🇹 Portuguese
- 🇮🇳 Hindi
- 🇨🇳 Chinese
- 🇯🇵 Japanese
- 🇰🇷 Korean
- 🇸🇦 Arabic

### Language Features

- **Auto-Detection**: Automatically detects document language
- **Translation**: Can translate documents for analysis
- **Localized Output**: Analysis provided in your preferred language
- **Cultural Context**: AI considers local legal contexts

## 💡 Use Cases

### For Individuals

- **Rental Agreements**: Understand your lease terms and obligations
- **Loan Contracts**: Identify hidden fees and payment schedules
- **Terms of Service**: Know what you're agreeing to online
- **Insurance Policies**: Understand coverage and exclusions
- **Employment Contracts**: Know your rights and responsibilities

### For Small Businesses

- **Vendor Contracts**: Analyze supplier agreements
- **Service Agreements**: Understand client contracts
- **Software Licenses**: Know usage rights and restrictions
- **Partnership Agreements**: Understand profit sharing and obligations

### For Students & Researchers

- **Legal Education**: Learn how legal documents work
- **Research Projects**: Analyze legal document patterns
- **Comparative Studies**: Compare legal terms across documents

## 🔧 Troubleshooting

### Common Issues

**1. "API Key Invalid" Error:**

- Check your Gemini API key is correct
- Ensure you have an active Google Cloud account
- Verify API usage limits aren't exceeded

**2. Text Extraction Issues:**

- Ensure document image is clear and well-lit
- Try different image formats (PDF usually works best)
- Check that text is clearly visible in the document

**3. AI Analysis Errors:**

- Verify internet connection
- Check if document contains readable text
- Try with a simpler document first

**4. Installation Problems:**

- Update pip: `python -m pip install --upgrade pip`
- Use virtual environment
- Install packages individually if batch fails

### Performance Tips

- **High-Quality Documents**: Use clear, high-resolution scans
- **Internet Speed**: Faster internet = quicker AI analysis
- **Document Size**: Large documents may take longer to process
- **API Limits**: Be aware of Gemini API rate limits

## 🎯 Hackathon Goals Achieved

### ✅ Challenge Requirements Met

- **Simplifies complex legal documents** ✓
- **Makes legal information accessible** ✓
- **Empowers informed decision-making** ✓
- **Uses Google Cloud generative AI** ✓
- **Provides clear summaries and explanations** ✓
- **Answers user queries in practical manner** ✓

### 🏆 Innovation Highlights

- **Privacy-first architecture** - No data storage
- **Multi-modal input** - Text, images, handwriting
- **Interactive Q&A** - Real-time document queries
- **Multi-language support** - Global accessibility
- **Risk identification** - Proactive user protection
- **Plain language output** - Truly accessible explanations

## 📈 Future Enhancements

### Planned Features

- **Document Comparison**: Compare multiple contracts side-by-side
- **Template Library**: Pre-built analysis for common document types
- **Legal Dictionary**: Interactive glossary of legal terms
- **Negotiation Tips**: Suggestions for contract improvements
- **Mobile App**: iOS/Android versions
- **Offline Mode**: Local AI models for complete privacy

### Technical Improvements

- **Faster Processing**: Optimize OCR and AI pipelines
- **Better Accuracy**: Enhanced text extraction algorithms
- **More Languages**: Expand language support
- **Custom Models**: Fine-tuned AI for specific legal domains

## 🤝 Contributing

We welcome contributions to make legal documents more accessible!

### Ways to Contribute

1. **Report Issues**: Found a bug? Let us know!
2. **Feature Requests**: Suggest new capabilities
3. **Code Contributions**: Submit pull requests
4. **Documentation**: Help improve guides and examples
5. **Testing**: Test with different document types
6. **Translation**: Help add more languages

### Development Setup

```bash
# Fork the repository
git clone <your-fork-url>
cd "Demystifying Legal Documents"

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and test
python demo.py

# Submit pull request
```

## 📄 Legal Disclaimer

**⚠️ Important Notice**: This tool provides AI-generated analysis for informational purposes only. It is NOT a substitute for professional legal advice. Always consult with a qualified attorney for legal matters, especially before signing important documents.

The AI analysis is based on pattern recognition and may not capture all nuances of legal language or jurisdiction-specific laws.

## 🙏 Acknowledgments

### Technologies Used

- **Google Gemini AI**: Advanced language understanding
- **Tesseract OCR**: Google's OCR engine
- **EasyOCR**: JaidedAI's handwriting recognition
- **Streamlit**: Beautiful web interface framework
- **OpenCV**: Computer vision processing
- **PyMuPDF**: PDF text extraction

### Inspiration

This project was inspired by the need to democratize legal information and empower individuals to understand their rights and obligations in legal agreements.

## 📞 Support & Contact

### Getting Help

1. **Check Documentation**: Review this README thoroughly
2. **Run Demo**: Try `python demo.py` to test functionality
3. **Check Issues**: Look for similar problems in GitHub issues
4. **Create Issue**: Report bugs with detailed information

### Project Information

- **Hackathon**: Generative AI for Demystifying Legal Documents
- **Team**: [Your Team Name]
- **Technologies**: Python, Streamlit, Google Gemini AI, OCR
- **License**: MIT License

---

## 🎉 Get Started Now!

1. **Install**: `pip install -r requirements.txt`
2. **Get API Key**: [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Launch**: `streamlit run legal_app.py`
4. **Upload Document**: Drag and drop your legal document
5. **Get Analysis**: Understand your document in plain language!

**Empower yourself with AI-driven legal document understanding! ⚖️✨**
