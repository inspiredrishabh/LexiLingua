"""
Enhanced Legal Document Analyzer with Gemini AI Integration
Privacy-first approach - no data storage, process and forget
"""

import google.generativeai as genai
import os
from typing import List, Dict, Any
import json
import tempfile
from text_extractor import TextExtractor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LegalDocumentAnalyzer:
    def __init__(self, gemini_api_key: str = None):
        """
        Initialize the Legal Document Analyzer with Gemini API
        
        Args:
            gemini_api_key: Optional Google Gemini API key. If not provided, will use GEMINI_API_KEY from environment
        """
        # Use provided API key or get from environment
        api_key = gemini_api_key or os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable or provide api_key parameter.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name
        self.text_extractor = TextExtractor()
        
    def extract_text_from_document(self, file_path: str) -> str:
        """
        Extract text from legal document (PDF/Image)
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Extracted text content
        """
        try:
            # Use our existing text extractor
            extracted_text = self.text_extractor.extract_text(file_path)
            return extracted_text
        except Exception as e:
            return f"Error extracting text: {str(e)}"
    
    def detect_document_type(self, document_text: str) -> str:
        """
        Quickly detect if this is a legal document or not
        """
        try:
            prompt = f"""
            Is the following text a legal document that requires legal analysis? 
            Legal documents include: contracts, agreements, terms of service, privacy policies, leases, loan agreements, etc.
            
            Text: {document_text[:500]}
            
            Respond with only: "LEGAL" or "NOT_LEGAL"
            """
            
            response = self.model.generate_content(prompt)
            return response.text.strip().upper()
        except:
            return "LEGAL"  # Default to legal if unsure
    
    def simplify_legal_document(self, document_text: str, user_language: str = "English") -> Dict[str, Any]:
        """
        Simplify legal document using Gemini AI
        
        Args:
            document_text: The extracted text from legal document
            user_language: Preferred language for explanation
            
        Returns:
            Dictionary containing simplified analysis
        """
        
        # Check if text extraction was poor
        if len(document_text.strip()) < 20 or "No readable text" in document_text or "extraction quality is poor" in document_text.lower():
            return {
                "error": "Poor text extraction quality",
                "message": "The text could not be extracted clearly from the document. Please try with a higher quality image or PDF.",
                "suggestions": [
                    "Use a higher resolution scan (300 DPI or higher)",
                    "Ensure good lighting and contrast",
                    "Make sure the text is clearly visible and not blurry",
                    "Try straightening the document if it's rotated",
                    "Use a PDF format if available instead of an image"
                ]
            }
        
        # Check if this is actually a legal document
        doc_type = self.detect_document_type(document_text)
        if doc_type == "NOT_LEGAL":
            return {
                "error": "Not a legal document",
                "message": "This appears to be a non-legal document (like a resume, invoice, personal letter, etc.) that does not require legal analysis.",
                "document_type": "Non-legal document"
            }
        
        prompt = f"""
        You are a legal expert AI assistant helping people understand complex legal documents. 
        
        FIRST: Determine if this is actually a legal document that requires legal analysis. 
        Legal documents include: contracts, agreements, terms of service, privacy policies, leases, loan agreements, etc.
        NON-legal documents include: resumes, letters, reports, articles, etc.
        
        Document Text:
        {document_text}
        
        If this is NOT a legal document, respond with:
        {{
            "error": "Not a legal document",
            "document_type": "[actual document type]",
            "message": "This appears to be [document type], not a legal document requiring legal analysis."
        }}
        
        If this IS a legal document, analyze it and respond in {user_language} language with the following JSON format:
        {{
            "document_type": "Type of legal document (e.g., Rental Agreement, Loan Contract, Terms of Service)",
            "key_parties": ["List of main parties involved"],
            "main_purpose": "Brief explanation of what this document is for",
            "key_terms_simplified": [
                {{
                    "original_clause": "Original complex legal text",
                    "simplified_explanation": "Easy-to-understand explanation",
                    "importance_level": "High/Medium/Low",
                    "potential_risk": "What could go wrong if you don't understand this"
                }}
            ],
            "important_dates": ["Any important deadlines or dates"],
            "financial_obligations": [
                {{
                    "description": "What you need to pay",
                    "amount": "How much",
                    "when": "When it's due",
                    "consequences": "What happens if you don't pay"
                }}
            ],
            "rights_and_responsibilities": {{
                "your_rights": ["What you can do"],
                "your_responsibilities": ["What you must do"],
                "other_party_rights": ["What they can do"],
                "other_party_responsibilities": ["What they must do"]
            }},
            "red_flags": ["Potentially problematic clauses or terms to be careful about"],
            "exit_clauses": ["How to get out of this agreement if needed"],
            "summary": "3-sentence summary of the entire document in simple terms",
            "recommendation": "Should you sign this? What should you negotiate?",
            "questions_to_ask": ["Important questions you should ask before signing"]
        }}
        
        Make sure your explanations are:
        - Written in simple, everyday language
        - Avoid legal jargon
        - Explain potential consequences clearly
        - Highlight any risks or red flags
        - Be helpful and protective of the user's interests
        """
        
        try:
            response = self.model.generate_content(prompt)
            
            # Try to parse as JSON, if fails return structured text
            try:
                return json.loads(response.text)
            except json.JSONDecodeError:
                return {
                    "analysis": response.text,
                    "note": "Analysis provided in text format due to formatting issues"
                }
                
        except Exception as e:
            return {
                "error": f"Failed to analyze document: {str(e)}",
                "fallback_advice": "Please consult with a qualified legal professional for accurate legal advice."
            }
    
    def ask_question_about_document(self, document_text: str, question: str, user_language: str = "English") -> str:
        """
        Answer specific questions about the legal document
        
        Args:
            document_text: The extracted text from legal document
            question: User's specific question
            user_language: Preferred language for response
            
        Returns:
            Answer to the user's question
        """
        
        prompt = f"""
        You are a legal expert helping someone understand their legal document. 
        Answer their question in simple, clear terms in {user_language}.
        
        Document Text:
        {document_text}
        
        User's Question: {question}
        
        Please provide:
        1. A direct answer to their question
        2. Any relevant warnings or things to be careful about
        3. Practical advice if applicable
        4. Suggestion to consult a lawyer if the matter is complex
        
        Keep your response helpful, protective of the user's interests, and easy to understand.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"I'm sorry, I couldn't process your question due to: {str(e)}. Please consult with a qualified legal professional."
    
    def detect_language(self, text: str) -> str:
        """
        Detect the language of the document text
        
        Args:
            text: Text to analyze
            
        Returns:
            Detected language
        """
        
        prompt = f"""
        Detect the language of the following text and respond with just the language name in English:
        
        {text[:500]}  # Only send first 500 characters for efficiency
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return "Unknown"
    
    def translate_document(self, document_text: str, target_language: str = "English") -> str:
        """
        Translate document to specified language
        
        Args:
            document_text: Text to translate
            target_language: Target language for translation
            
        Returns:
            Translated text
        """
        
        prompt = f"""
        Translate the following legal document text to {target_language}. 
        Maintain the legal meaning and structure while making it readable:
        
        {document_text}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Translation failed: {str(e)}"
    
    def generate_summary_report(self, analysis: Dict[str, Any], user_language: str = "English") -> str:
        """
        Generate a user-friendly summary report
        
        Args:
            analysis: The analysis dictionary from simplify_legal_document
            user_language: Language for the report
            
        Returns:
            Formatted summary report
        """
        
        if "error" in analysis:
            if "suggestions" in analysis:
                report = f"⚠️ TEXT EXTRACTION ISSUE\n\n"
                report += f"{analysis.get('message', 'Unknown error')}\n\n"
                report += "💡 SUGGESTIONS TO IMPROVE TEXT EXTRACTION:\n"
                for suggestion in analysis.get('suggestions', []):
                    report += f"• {suggestion}\n"
                return report
            else:
                return f"⚠️  Analysis Error: {analysis['error']}"
        
        if "analysis" in analysis and "note" in analysis:
            return analysis["analysis"]
        
        try:
            report = "📋 LEGAL DOCUMENT ANALYSIS REPORT\n"
            report += "=" * 50 + "\n\n"
            
            # Document Type
            if analysis.get('document_type'):
                report += f"📄 DOCUMENT TYPE:\n{analysis['document_type']}\n\n"
            
            # Main Purpose
            if analysis.get('main_purpose'):
                report += f"🎯 MAIN PURPOSE:\n{analysis['main_purpose']}\n\n"
            
            # Key Parties
            if analysis.get('key_parties'):
                report += f"👥 KEY PARTIES:\n"
                for party in analysis['key_parties']:
                    report += f"• {party}\n"
                report += "\n"
            
            # Important Dates
            if analysis.get('important_dates'):
                report += f"📅 IMPORTANT DATES:\n"
                for date in analysis['important_dates']:
                    report += f"• {date}\n"
                report += "\n"
            
            # Financial Obligations
            if analysis.get('financial_obligations') and analysis['financial_obligations']:
                report += f"💰 FINANCIAL OBLIGATIONS:\n"
                for obligation in analysis['financial_obligations']:
                    if obligation.get('description'):
                        report += f"• {obligation['description']}"
                        if obligation.get('amount'):
                            report += f" - {obligation['amount']}"
                        if obligation.get('when'):
                            report += f" (Due: {obligation['when']})"
                        report += "\n"
                        if obligation.get('consequences'):
                            report += f"  ⚠️ Risk: {obligation['consequences']}\n"
                report += "\n"
            
            # Key Terms Simplified
            if analysis.get('key_terms_simplified'):
                report += f"🔑 KEY TERMS EXPLAINED:\n"
                for i, term in enumerate(analysis['key_terms_simplified'], 1):
                    if term.get('simplified_explanation'):
                        report += f"{i}. {term['simplified_explanation']}\n"
                        if term.get('potential_risk'):
                            report += f"   ⚠️ Risk: {term['potential_risk']}\n"
                report += "\n"
            
            # Red Flags
            if analysis.get('red_flags') and analysis['red_flags']:
                report += f"🚨 RED FLAGS TO WATCH OUT FOR:\n"
                for flag in analysis['red_flags']:
                    report += f"• {flag}\n"
                report += "\n"
            
            # Rights and Responsibilities
            if analysis.get('rights_and_responsibilities'):
                rights = analysis['rights_and_responsibilities']
                
                if rights.get('your_rights'):
                    report += f"✅ YOUR RIGHTS:\n"
                    for right in rights['your_rights']:
                        report += f"• {right}\n"
                    report += "\n"
                
                if rights.get('your_responsibilities'):
                    report += f"📋 YOUR RESPONSIBILITIES:\n"
                    for resp in rights['your_responsibilities']:
                        report += f"• {resp}\n"
                    report += "\n"
            
            # Summary
            if analysis.get('summary'):
                report += f"📖 SUMMARY:\n{analysis['summary']}\n\n"
            
            # Recommendation
            if analysis.get('recommendation'):
                report += f"💡 RECOMMENDATION:\n{analysis['recommendation']}\n\n"
            
            # Questions to Ask
            if analysis.get('questions_to_ask'):
                report += f"❓ QUESTIONS TO ASK:\n"
                for question in analysis['questions_to_ask']:
                    report += f"• {question}\n"
                report += "\n"
            
            # Exit Clauses
            if analysis.get('exit_clauses') and analysis['exit_clauses']:
                report += f"🚪 HOW TO EXIT THIS AGREEMENT:\n"
                for clause in analysis['exit_clauses']:
                    report += f"• {clause}\n"
                report += "\n"
            
            report += "=" * 50 + "\n"
            report += "⚖️  IMPORTANT: This is AI-generated analysis for informational purposes only.\n"
            report += "Always consult with a qualified legal professional before making important legal decisions."
            
            return report
            
        except Exception as e:
            return f"Error generating report: {str(e)}"

    def process_document_complete(self, file_path: str, user_language: str = "English") -> Dict[str, Any]:
        """
        Complete document processing pipeline - extract, analyze, and report
        Privacy-first: processes and returns results without storing anything
        
        Args:
            file_path: Path to the document file
            user_language: Preferred language for analysis
            
        Returns:
            Complete analysis package
        """
        
        # Step 1: Extract text
        print("🔍 Extracting text from document...")
        extracted_text = self.extract_text_from_document(file_path)
        
        if "Error extracting text" in extracted_text:
            return {"error": extracted_text}
        
        # Step 2: Detect language
        print("🌐 Detecting document language...")
        detected_language = self.detect_language(extracted_text)
        
        # Step 3: Translate if needed (for better analysis)
        analysis_text = extracted_text
        if detected_language.lower() != "english" and user_language.lower() == "english":
            print(f"🔄 Translating from {detected_language} to English for analysis...")
            analysis_text = self.translate_document(extracted_text, "English")
        
        # Step 4: Analyze document
        print("🧠 Analyzing document with AI...")
        analysis = self.simplify_legal_document(analysis_text, user_language)
        
        # Handle non-legal documents
        if "error" in analysis and analysis.get("error") == "Not a legal document":
            return {
                "error": "Not a legal document",
                "message": analysis.get("message", "This is not a legal document."),
                "document_type": analysis.get("document_type", "Non-legal document"),
                "extracted_text": extracted_text,
                "detected_language": detected_language
            }
        
        # Step 5: Generate report (only for legal documents)
        print("📊 Generating summary report...")
        summary_report = self.generate_summary_report(analysis, user_language)
        
        return {
            "original_text": extracted_text,
            "detected_language": detected_language,
            "analysis": analysis,
            "summary_report": summary_report,
            "processing_complete": True
        }

# Example usage and testing
if __name__ == "__main__":
    try:
        analyzer = LegalDocumentAnalyzer()  # Will automatically use environment variable
        print("🚀 Legal Document Analyzer Ready!")
        print("API key loaded from environment variables.")
        print("Place your legal document (PDF/Image) in the current directory and specify the filename.")
    except ValueError as e:
        print(f"⚠️  {str(e)}")
        print("You can get your API key from: https://makersuite.google.com/app/apikey")
        print("Then add it to your .env file: GEMINI_API_KEY=your_key_here")
