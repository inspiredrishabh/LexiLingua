"""
Enhanced CLI Legal Document Analyzer with Gemini AI
Privacy-first command-line tool for legal document analysis
"""

import argparse
import os
from legal_document_analyzer import LegalDocumentAnalyzer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Legal Document Analyzer - Demystify Legal Documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python legal_cli.py contract.pdf --api-key YOUR_KEY
  python legal_cli.py lease.jpg --api-key YOUR_KEY --language Spanish
  python legal_cli.py terms.pdf --api-key YOUR_KEY --question "What are the cancellation terms?"

Privacy Notice:
  - Your documents are processed locally and securely
  - No data is stored on our servers
  - API calls to Gemini are encrypted
  - Temporary files are automatically deleted
        """
    )
    
    parser.add_argument(
        "document", 
        help="Path to the legal document (PDF or image file)"
    )
    
    parser.add_argument(
        "--api-key", 
        help="Your Gemini API key (optional, will use GEMINI_API_KEY from environment if not provided)"
    )
    
    parser.add_argument(
        "--language", 
        default="English",
        choices=["English", "Spanish", "French", "German", "Italian", "Portuguese", "Hindi", "Chinese", "Japanese", "Korean", "Arabic"],
        help="Language for the analysis (default: English)"
    )
    
    parser.add_argument(
        "--question", 
        help="Ask a specific question about the document"
    )
    
    parser.add_argument(
        "--output", 
        help="Output file to save the analysis report"
    )
    
    parser.add_argument(
        "--extract-only", 
        action="store_true",
        help="Only extract text, skip AI analysis"
    )

    args = parser.parse_args()
    
    # Check if document exists
    if not os.path.exists(args.document):
        print(f"❌ Error: Document '{args.document}' not found.")
        return
    
    print("⚖️  Legal Document AI Analyzer")
    print("="*50)
    print(f"📄 Document: {args.document}")
    print(f"🌍 Language: {args.language}")
    print("🔒 Privacy: Document processed securely, not stored")
    print("="*50)
    
    try:
        # Initialize analyzer
        print("🔧 Initializing AI analyzer...")
        analyzer = LegalDocumentAnalyzer(args.api_key)  # Will use env var if args.api_key is None
        
        if args.extract_only:
            # Extract text only
            print("🔍 Extracting text from document...")
            text = analyzer.extract_text_from_document(args.document)
            
            if text.strip():
                print("\n📝 EXTRACTED TEXT:")
                print("-" * 30)
                print(text)
                
                if args.output:
                    with open(args.output, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f"\n💾 Text saved to: {args.output}")
            else:
                print("⚠️  No text was extracted from the document.")
        
        elif args.question:
            # Extract text first
            print("🔍 Extracting text from document...")
            text = analyzer.extract_text_from_document(args.document)
            
            if not text.strip():
                print("❌ Error: Could not extract text from document.")
                return
            
            # Answer specific question
            print(f"🤔 Analyzing question: '{args.question}'")
            answer = analyzer.ask_question_about_document(text, args.question, args.language)
            
            print("\n💬 AI ANSWER:")
            print("-" * 30)
            print(answer)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(f"Question: {args.question}\n\n")
                    f.write(f"Answer:\n{answer}")
                print(f"\n💾 Answer saved to: {args.output}")
        
        else:
            # Complete analysis
            print("🧠 Performing complete AI analysis...")
            result = analyzer.process_document_complete(args.document, args.language)
            
            if "error" in result:
                print(f"❌ Analysis failed: {result['error']}")
                return
            
            # Display results
            print("\n" + "="*60)
            print("📊 AI ANALYSIS REPORT")
            print("="*60)
            
            if 'summary_report' in result:
                print(result['summary_report'])
            
            # Save to file if requested
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write("LEGAL DOCUMENT AI ANALYSIS REPORT\n")
                    f.write("="*50 + "\n\n")
                    f.write(f"Document: {args.document}\n")
                    f.write(f"Language: {args.language}\n")
                    f.write(f"Detected Language: {result.get('detected_language', 'Unknown')}\n\n")
                    
                    if 'summary_report' in result:
                        f.write(result['summary_report'])
                    
                    f.write("\n\nORIGINAL EXTRACTED TEXT:\n")
                    f.write("-" * 30 + "\n")
                    f.write(result.get('original_text', 'No text extracted'))
                
                print(f"\n💾 Full report saved to: {args.output}")
            
            print(f"\n📊 Document Statistics:")
            original_text = result.get('original_text', '')
            if original_text:
                print(f"   Characters: {len(original_text):,}")
                print(f"   Words: {len(original_text.split()):,}")
                print(f"   Lines: {len(original_text.split(chr(10))):,}")
        
        print("\n✅ Analysis completed successfully!")
        print("🗑️  Temporary files securely deleted")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check your Gemini API key")
        print("2. Ensure the document file is readable")
        print("3. Check your internet connection")
        print("4. Try with a different document format")

if __name__ == "__main__":
    main()
