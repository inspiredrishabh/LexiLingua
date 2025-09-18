from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile
from text_extractor import TextExtractor
from legal_document_analyzer import LegalDocumentAnalyzer

app = FastAPI(title="LexiLingua API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
text_extractor = TextExtractor()
legal_analyzer = LegalDocumentAnalyzer()

@app.get("/")
async def root():
    return {"message": "LexiLingua API is running"}

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    """
    Analyze a legal document and return comprehensive analysis
    """
    try:
        # Validate file type
        allowed_extensions = ['.pdf', '.docx', '.jpg', '.jpeg', '.png']
        file_extension = os.path.splitext(file.filename)[1].lower()
        
        if file_extension not in allowed_extensions:
            raise HTTPException(
                status_code=400, 
                detail="Unsupported file type. Please upload PDF, DOCX, JPG, JPEG, or PNG files."
            )
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_file_path = tmp_file.name
        
        try:
            # Extract text from the document
            extracted_text = text_extractor.extract_text(tmp_file_path)
            
            if not extracted_text.strip():
                raise HTTPException(
                    status_code=400,
                    detail="Could not extract text from the document. Please ensure the file is readable."
                )
            
            # Analyze the document
            analysis_result = legal_analyzer.analyze_document(extracted_text)
            
            return JSONResponse(content={
                "status": "success",
                "filename": file.filename,
                "analysis": analysis_result,
                "extracted_text_length": len(extracted_text)
            })
            
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
                
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/explain-jargon")
async def explain_jargon(text: str):
    """
    Explain legal jargon in the provided text
    """
    try:
        jargon_explanation = legal_analyzer.explain_jargon(text)
        return JSONResponse(content={
            "status": "success",
            "jargon_explanation": jargon_explanation
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/assess-risks")
async def assess_risks(text: str):
    """
    Assess risks in the legal document
    """
    try:
        risk_assessment = legal_analyzer.assess_risks(text)
        return JSONResponse(content={
            "status": "success",
            "risk_assessment": risk_assessment
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/qa")
async def document_qa(question: str, document_text: str):
    """
    Answer questions about the document using AI
    """
    try:
        answer = legal_analyzer.answer_question(question, document_text)
        return JSONResponse(content={
            "status": "success",
            "question": question,
            "answer": answer
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)