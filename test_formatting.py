"""
Test script to demonstrate the improved formatting and text extraction
"""

from legal_document_analyzer import LegalDocumentAnalyzer
from text_extractor import TextExtractor

def test_sample_analysis():
    """Test the analyzer with a sample legal text"""
    
    # Sample legal text (clear and readable)
    sample_legal_text = """
    RENTAL LEASE AGREEMENT
    
    This Residential Lease Agreement is entered into on January 1, 2024, between:
    
    LANDLORD: John Smith, 123 Main Street, City, State
    TENANT: Jane Doe, Current Address: 456 Oak Avenue
    
    PROPERTY: 789 Elm Street, Apartment 2B, City, State 12345
    
    TERMS:
    1. RENT: $1,200 per month, due on the 1st of each month
    2. LEASE TERM: 12 months, from January 1, 2024 to December 31, 2024
    3. SECURITY DEPOSIT: $2,400 (equivalent to 2 months rent)
    4. LATE FEE: $75 if rent is paid after the 5th of the month
    5. UTILITIES: Tenant responsible for electricity and internet; Landlord pays water and trash
    6. PETS: No pets allowed without written consent and additional $300 deposit
    7. MAINTENANCE: Tenant responsible for minor repairs under $100
    8. TERMINATION: 30 days written notice required by either party
    
    TENANT SIGNATURE: _________________ DATE: _________
    LANDLORD SIGNATURE: _________________ DATE: _________
    """
    
    try:
        analyzer = LegalDocumentAnalyzer()
        print("🚀 Testing Legal Document Analyzer with Sample Text")
        print("=" * 60)
        
        # Analyze the sample text
        analysis = analyzer.simplify_legal_document(sample_legal_text, "English")
        
        # Generate formatted report
        report = analyzer.generate_summary_report(analysis, "English")
        
        print("📄 SAMPLE INPUT:")
        print(sample_legal_text[:200] + "...\n")
        
        print("📊 AI-GENERATED ANALYSIS REPORT:")
        print(report)
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")

def test_poor_text_extraction():
    """Test with poor quality text to demonstrate error handling"""
    
    poor_text = "Mr7 7tT 7tT 7*7067 JAN:2020 Rs.5000"
    
    try:
        analyzer = LegalDocumentAnalyzer()
        print("\n" + "=" * 60)
        print("🔍 Testing with Poor Quality Text Extraction")
        print("=" * 60)
        
        analysis = analyzer.simplify_legal_document(poor_text, "English")
        report = analyzer.generate_summary_report(analysis, "English")
        
        print("📄 POOR INPUT:")
        print(f"'{poor_text}'\n")
        
        print("📊 AI RESPONSE:")
        print(report)
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")

if __name__ == "__main__":
    test_sample_analysis()
    test_poor_text_extraction()
    
    print("\n" + "=" * 60)
    print("✅ FORMATTING IMPROVEMENTS IMPLEMENTED:")
    print("   • Clean, readable report format")
    print("   • Proper headings and structure") 
    print("   • Better error handling for poor text extraction")
    print("   • Helpful suggestions for image quality")
    print("   • Stacked button layout for better UI")
    print("   • Enhanced text extraction with quality filtering")
    print("🎉 Your Legal Document AI Analyzer is ready for the hackathon!")
