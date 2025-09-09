import streamlit as st
from text_extractor import TextExtractor
from legal_document_analyzer import LegalDocumentAnalyzer
import tempfile
import os
from PIL import Image
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="Legal Document AI Analyzer",
        page_icon="⚖️",
        layout="wide"
    )
    
    st.title("⚖️ AI-Powered Legal Document Analyzer")
    st.markdown("🚀 **Demystifying Legal Documents with AI** - Extract, Analyze, and Understand Legal Documents in Plain Language")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("🌍 Language Settings")
        user_language = st.selectbox(
            "Preferred Language for Analysis",
            ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Hindi", "Chinese", "Japanese", "Korean", "Arabic"]
        )
        
        st.header("📖 Instructions")
        st.markdown("""
        ### How to Use:
        1. **Upload** your legal document (PDF/Image)
        2. **Get AI Analysis** in plain language
        3. **Ask Questions** about specific clauses
        4. **Download Reports** for your records
        
        ### For Best Results:
        - 📷 Use **high-quality images** (300 DPI+)
        - 💡 Ensure **good lighting** and contrast
        - 📐 Keep document **straight** and unfolded
        - 🔍 Make sure text is **clearly readable**
        - 📄 **PDF format preferred** over images
        
        ### Privacy First:
        - ✅ No data stored on servers
        - ✅ Process and delete immediately
        - ✅ Your documents stay private
        - ✅ API calls are encrypted
        - ✅ AI processing powered by secure API
        
        ### Supported Formats:
        - PDF documents
        - Images (PNG, JPG, JPEG, TIFF, BMP)
        - Handwritten documents
        - Multi-language documents
        """)
    
    # Initialize analyzers
    try:
        extractor = TextExtractor()
        analyzer = LegalDocumentAnalyzer()  # Uses environment variable
        st.success("✅ AI Analyzer Ready! Powered by Gemini AI")
    except ValueError as e:
        st.error("❌ AI Service Configuration Error")
        st.info("The AI analysis service is currently unavailable. Please try the text extraction feature instead.")
        
        # Still allow text extraction
        extractor = TextExtractor()
        analyzer = None
    except Exception as e:
        st.error(f"❌ Failed to initialize services: {str(e)}")
        return
    
    # File upload
    uploaded_file = st.file_uploader(
        "📁 Upload Your Legal Document", 
        type=['pdf', 'png', 'jpg', 'jpeg', 'tiff', 'bmp'],
        help="Upload a legal document (PDF or image) for AI analysis"
    )
    
    if uploaded_file is not None:
        # Display file info
        st.info(f"📄 File: {uploaded_file.name} ({uploaded_file.size:,} bytes)")
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_path = tmp_file.name
        
        try:
            # Show preview for images
            if uploaded_file.type.startswith('image/'):
                with st.expander("📸 Document Preview"):
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Document", use_column_width=True)
            
            # Processing options
            if st.button("🔍 Extract Text Only", use_container_width=True):
                with st.spinner("Extracting text..."):
                    extracted_text = extractor.extract_text(temp_path)
                
                if extracted_text.strip():
                    st.subheader("📝 Extracted Text")
                    st.text_area("Raw Text", extracted_text, height=300)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Text",
                        data=extracted_text,
                        file_name=f"extracted_{uploaded_file.name}.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("⚠️ No text found in document")
            
            st.markdown("---")  # Visual separator
            
            if st.button("🧠 AI Analysis (Full Report)", use_container_width=True, type="primary"):
                    if analyzer is None:
                        st.error("❌ AI Analysis service is currently unavailable. Please use text extraction instead.")
                    else:
                        with st.spinner("🔄 Processing document with AI... This may take a moment."):
                            # Privacy notice
                            st.info("🔒 **Privacy Notice**: Your document is being processed securely and will not be stored.")
                            
                            # Complete analysis
                            result = analyzer.process_document_complete(temp_path, user_language)
                        
                        if "error" in result:
                            # Check if it's a non-legal document
                            if result.get("error") == "Not a legal document":
                                st.warning("📄 **Document Type Detected**")
                                st.info(f"ℹ️ {result.get('message', 'This is not a legal document.')}")
                                st.markdown("### 📝 Extracted Text")
                                extracted_text = result.get('extracted_text', 'Text extraction failed.')
                                st.text_area("", extracted_text, height=300)
                                return
                            else:
                                st.error(f"❌ Analysis failed: {result['error']}")
                                if "suggestions" in result:
                                    st.info("💡 **Suggestions to improve text extraction:**")
                                    for suggestion in result["suggestions"]:
                                        st.write(f"• {suggestion}")
                                return
                        else:
                            # Display results in tabs
                            tab1, tab2, tab3, tab4 = st.tabs(["📊 Summary Report", "📋 Detailed Analysis", "📝 Original Text", "❓ Ask Questions"])
                            
                        with tab1:
                            st.markdown("### 📊 AI Summary Report")
                            
                            # Display the formatted report in a text area for better readability
                            summary_report = result.get('summary_report', 'No summary available')
                            st.text_area("", summary_report, height=600, key="summary_display")
                            
                            # Download report
                            st.download_button(
                                label="📥 Download Full Report",
                                data=summary_report,
                                file_name=f"legal_analysis_{uploaded_file.name}.txt",
                                mime="text/plain"
                            )
                        
                        with tab2:
                            st.markdown("### 📋 Detailed AI Analysis")
                            analysis = result.get('analysis', {})
                            
                            if isinstance(analysis, dict) and 'error' not in analysis:
                                # Document info
                                if 'document_type' in analysis:
                                    st.info(f"📄 **Document Type**: {analysis['document_type']}")
                                
                                if 'main_purpose' in analysis:
                                    st.write(f"🎯 **Purpose**: {analysis['main_purpose']}")
                                
                                # Key terms
                                if 'key_terms_simplified' in analysis:
                                    st.subheader("🔑 Key Terms Explained")
                                    for term in analysis['key_terms_simplified']:
                                        with st.expander(f"📝 {term.get('original_clause', 'Term')[:100]}..."):
                                            st.write(f"**Simplified**: {term.get('simplified_explanation', '')}")
                                            st.write(f"**Importance**: {term.get('importance_level', 'Unknown')}")
                                            if term.get('potential_risk'):
                                                st.warning(f"⚠️ **Risk**: {term['potential_risk']}")
                                
                                # Red flags
                                if 'red_flags' in analysis and analysis['red_flags']:
                                    st.subheader("🚨 Red Flags")
                                    for flag in analysis['red_flags']:
                                        st.error(f"⚠️ {flag}")
                                
                                # Financial obligations
                                if 'financial_obligations' in analysis:
                                    st.subheader("💰 Financial Obligations")
                                    for obligation in analysis['financial_obligations']:
                                        st.write(f"💵 **{obligation.get('description', '')}**")
                                        st.write(f"Amount: {obligation.get('amount', 'Not specified')}")
                                        st.write(f"Due: {obligation.get('when', 'Not specified')}")
                                        if obligation.get('consequences'):
                                            st.warning(f"Consequences: {obligation['consequences']}")
                                        st.divider()
                            else:
                                st.json(analysis)
                        
                        with tab3:
                            st.markdown("### 📝 Original Extracted Text")
                            original_text = result.get('original_text', '')
                            detected_lang = result.get('detected_language', 'Unknown')
                            st.info(f"🌐 Detected Language: {detected_lang}")
                            st.text_area("Original Text", original_text, height=400)
                        
                        with tab4:
                            st.markdown("### ❓ Ask Questions About This Document")
                            st.info("💡 Ask specific questions about clauses, terms, or anything you don't understand.")
                            
                            question = st.text_input("Your question:", placeholder="e.g., What happens if I break this contract?")
                            
                            if st.button("🤔 Get Answer") and question:
                                with st.spinner("🧠 AI is analyzing your question..."):
                                    answer = analyzer.ask_question_about_document(
                                        result.get('original_text', ''), 
                                        question, 
                                        user_language
                                    )
                                
                                st.markdown("### 💬 AI Response")
                                st.markdown(answer)
                        
                        # Statistics
                        with st.sidebar:
                            st.subheader("📊 Document Stats")
                            original_text = result.get('original_text', '')
                            if original_text:
                                st.metric("Characters", f"{len(original_text):,}")
                                st.metric("Words", f"{len(original_text.split()):,}")
                                st.metric("Lines", f"{len(original_text.split(chr(10))):,}")
        
        except Exception as e:
            st.error(f"❌ Error processing document: {str(e)}")
        
        finally:
            # Clean up temporary file (Privacy First!)
            if os.path.exists(temp_path):
                os.unlink(temp_path)
                st.success("🗑️ Temporary file securely deleted")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        ⚖️ <strong>Legal Document AI Analyzer</strong> - Hackathon Project for Demystifying Legal Documents<br>
        🔒 Privacy-First • 🧠 AI-Powered • 📄 Multi-Format • 🌍 Multi-Language<br>
        <em>⚠️ This tool provides AI-generated analysis for informational purposes only. Always consult a qualified legal professional for legal advice.</em>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
