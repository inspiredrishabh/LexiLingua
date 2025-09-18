# LexiLingua - AI-Powered Legal Document Analyzer

LexiLingua is a modern web application that uses artificial intelligence to analyze legal documents, providing comprehensive insights, jargon explanations, risk assessments, and intelligent Q&A capabilities.

## 🌟 Features

- **Document Analysis**: Extract and analyze text from PDFs, Word docs, and images
- **Jargon Explanation**: Break down complex legal terms into plain language
- **Risk Assessment**: Identify potential risks and red flags in documents
- **AI Q&A**: Ask questions about your document and get instant answers
- **Modern UI**: Professional React frontend with shadcn/ui components
- **Privacy-First**: Documents are processed and not stored

## 🛠 Technology Stack

### Frontend

- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **shadcn/ui** component library
- **Lucide React** for icons

### Backend

- **FastAPI** (Python)
- **Google Gemini AI** for document analysis
- **PyMuPDF** for PDF processing
- **Tesseract OCR** for image text extraction
- **python-docx** for Word document processing

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (3.8 or higher)
- **npm** or **yarn**
- **pip** (Python package installer)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-Powered-Legal-Document-Analyzer
```

### 2. Set Up the Backend

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.template .env

# Edit .env file and add your Google Gemini API key
# GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Get Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key to your `.env` file

### 4. Set Up the Frontend

```bash
# Navigate to frontend directory
cd ../frontend

# Install Node.js dependencies
npm install
```

### 5. Run the Application

#### Start the Backend Server

```bash
# From the backend directory
cd backend
python main.py
```

The backend will be available at `http://localhost:8000`

#### Start the Frontend Development Server

```bash
# From the frontend directory (in a new terminal)
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

## 📁 Project Structure

```
AI-Powered-Legal-Document-Analyzer/
├── frontend/                          # React TypeScript frontend
│   ├── public/                        # Static assets
│   ├── src/
│   │   ├── components/ui/             # shadcn/ui components
│   │   ├── lib/                       # Utility functions
│   │   ├── App.tsx                    # Main application component
│   │   └── index.tsx                  # Application entry point
│   ├── package.json                   # Frontend dependencies
│   ├── tailwind.config.js            # Tailwind CSS configuration
│   └── components.json               # shadcn/ui configuration
├── backend/                           # Python FastAPI backend
│   ├── legal_document_analyzer.py    # Main AI analysis logic
│   ├── text_extractor.py            # Text extraction utilities
│   ├── main.py                       # FastAPI application
│   ├── requirements.txt              # Python dependencies
│   └── .env.template                 # Environment variables template
└── README.md                         # Project documentation
```

## 🔧 Configuration

### Backend Configuration

The backend uses environment variables for configuration. Copy `.env.template` to `.env` and configure:

```env
# Google Gemini API Key (Required)
GEMINI_API_KEY=your_gemini_api_key_here

# Development Settings
DEBUG=True
ENVIRONMENT=development
```

### Frontend Configuration

The frontend is pre-configured to connect to the backend at `http://localhost:8000`. If you need to change this, update the API URLs in `src/App.tsx`.

## 📋 API Endpoints

### Backend API

- `GET /` - Health check
- `POST /analyze` - Analyze a legal document
- `POST /explain-jargon` - Explain legal jargon in text
- `POST /assess-risks` - Assess risks in a document
- `POST /qa` - Ask questions about a document

### Example API Usage

```bash
# Analyze a document
curl -X POST "http://localhost:8000/analyze" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your-document.pdf"

# Ask a question
curl -X POST "http://localhost:8000/qa" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the payment terms?",
    "document_text": "Your document text here..."
  }'
```

## 📄 Supported File Formats

- **PDF files** (.pdf)
- **Word documents** (.docx)
- **Images** (.jpg, .jpeg, .png) - processed with OCR

## 🧪 Development

### Running Tests

```bash
# Backend tests (if available)
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Code Formatting

```bash
# Frontend
cd frontend
npm run lint

# Backend (install black first: pip install black)
cd backend
black *.py
```

## 🚀 Deployment

### Frontend Deployment

```bash
cd frontend
npm run build
# Deploy the 'build' folder to your hosting service
```

### Backend Deployment

The backend can be deployed to any platform that supports Python applications:

- **Heroku**
- **AWS Lambda**
- **Google Cloud Run**
- **Railway**
- **Render**

Make sure to set the `GEMINI_API_KEY` environment variable in your deployment environment.

## ⚠️ Important Notes

1. **API Key Security**: Never commit your `.env` file or expose your Gemini API key
2. **Privacy**: Documents are processed in memory and not stored permanently
3. **Rate Limits**: Google Gemini API has rate limits - consider implementing request throttling for production
4. **Legal Disclaimer**: This tool provides AI-generated analysis for informational purposes only. Always consult qualified legal professionals for important legal decisions.

## 🐛 Troubleshooting

### Common Issues

1. **Backend won't start**: Check if Python dependencies are installed and API key is set
2. **Frontend can't connect**: Ensure backend is running on port 8000
3. **OCR not working**: Install Tesseract OCR system dependency
4. **PDF processing fails**: Ensure PyMuPDF is properly installed

### Error Messages

- **"Import fastapi could not be resolved"**: Install backend dependencies with `pip install -r requirements.txt`
- **"GEMINI_API_KEY not found"**: Set up your `.env` file with a valid API key
- **"CORS error"**: Ensure backend CORS settings allow frontend origin

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful document analysis capabilities
- **shadcn/ui** for beautiful React components
- **FastAPI** for the excellent Python web framework
- **Tailwind CSS** for utility-first styling

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information
4. For urgent matters, contact the development team

---

**⚖️ Legal Disclaimer**: LexiLingua provides AI-generated analysis for informational purposes only. This tool is not a substitute for professional legal advice. Always consult with qualified legal professionals before making important legal decisions.
