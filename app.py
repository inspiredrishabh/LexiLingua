import streamlit as st
import os
import tempfile
from text_extractor import TextExtractor
import json
from PIL import Image
import base64

def main():
    st.set_page_config(
        page_title="Advanced Text Extractor",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🔍 Advanced Text Extractor")
    st.markdown("**Extract text from images and PDFs with support for handwritten content**")
    
    # Sidebar for options
    st.sidebar.title("⚙️ Settings")
    
    # Initialize the text extractor
    @st.cache_resource
    def load_extractor():
        return TextExtractor()
    
    try:
        extractor = load_extractor()
        st.sidebar.success("✅ OCR engines loaded successfully!")
    except Exception as e:
        st.sidebar.error(f"❌ Error loading OCR engines: {e}")
        st.error("Please install the required dependencies. See installation instructions below.")
        return
    
    # File upload options
    st.sidebar.subheader("📁 Upload Options")
    output_format = st.sidebar.selectbox(
        "Output Format",
        ["Simple Text", "Detailed Results"],
        help="Choose between simple text output or detailed analysis"
    )
    
    save_results = st.sidebar.checkbox(
        "Save Results to File", 
        value=True,
        help="Save extraction results as JSON file"
    )
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Your File")
        uploaded_file = st.file_uploader(
            "Choose an image or PDF file",
            type=['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'pdf'],
            help="Supported formats: PNG, JPG, JPEG, BMP, TIFF, GIF, PDF"
        )
        
        if uploaded_file is not None:
            # Display file info
            st.info(f"**File:** {uploaded_file.name}")
            st.info(f"**Size:** {uploaded_file.size / 1024:.1f} KB")
            st.info(f"**Type:** {uploaded_file.type}")
            
            # Show preview for images
            if uploaded_file.type.startswith('image/'):
                try:
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Preview", use_column_width=True)
                except Exception as e:
                    st.error(f"Error displaying image: {e}")
    
    with col2:
        st.subheader("🎯 Extraction Results")
        
        if uploaded_file is not None:
            # Process button
            if st.button("🚀 Extract Text", type="primary"):
                with st.spinner("Processing... This may take a few moments for complex documents."):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_file_path = tmp_file.name
                        
                        # Extract text
                        if output_format == "Simple Text":
                            result = extractor.extract_text(tmp_file_path, output_format='text')
                            
                            if result.strip():
                                st.success("✅ Text extraction completed!")
                                st.text_area("Extracted Text:", value=result, height=300)
                                
                                # Download button for text
                                st.download_button(
                                    label="📥 Download Text",
                                    data=result,
                                    file_name=f"extracted_text_{uploaded_file.name}.txt",
                                    mime="text/plain"
                                )
                            else:
                                st.warning("⚠️ No text was detected in the file. Try with a different image or check if the text is clearly visible.")
                        
                        else:  # Detailed Results
                            result = extractor.extract_text(tmp_file_path, output_format='detailed')
                            
                            if result['combined_text'].strip():
                                st.success("✅ Text extraction completed!")
                                
                                # Display main result
                                st.subheader("📝 Final Extracted Text")
                                st.text_area("", value=result['combined_text'], height=200)
                                
                                # Show detailed analysis
                                with st.expander("🔍 Detailed Analysis"):
                                    st.json(result)
                                
                                # Download buttons
                                col_a, col_b = st.columns(2)
                                with col_a:
                                    st.download_button(
                                        label="📥 Download Text",
                                        data=result['combined_text'],
                                        file_name=f"extracted_text_{uploaded_file.name}.txt",
                                        mime="text/plain"
                                    )
                                
                                with col_b:
                                    st.download_button(
                                        label="📥 Download JSON",
                                        data=json.dumps(result, indent=2),
                                        file_name=f"detailed_results_{uploaded_file.name}.json",
                                        mime="application/json"
                                    )
                            else:
                                st.warning("⚠️ No text was detected in the file.")
                        
                        # Clean up temporary file
                        os.unlink(tmp_file_path)
                        
                    except Exception as e:
                        st.error(f"❌ Error during text extraction: {e}")
                        if 'tmp_file_path' in locals():
                            try:
                                os.unlink(tmp_file_path)
                            except:
                                pass
        else:
            st.info("👆 Please upload a file to begin text extraction")
    
    # Instructions and tips
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📋 Instructions")
        st.markdown("""
        1. **Upload** your image or PDF file
        2. **Choose** output format in sidebar
        3. **Click** 'Extract Text' button
        4. **Download** results if needed
        """)
    
    with col2:
        st.subheader("💡 Tips for Better Results")
        st.markdown("""
        - Use **high-resolution** images
        - Ensure **good contrast** between text and background
        - **Straighten** rotated documents
        - Use **clear, well-lit** photos
        """)
    
    with col3:
        st.subheader("🎯 Supported Features")
        st.markdown("""
        - **Printed text** recognition
        - **Handwritten text** detection
        - **Multiple languages** support
        - **PDF** processing
        - **Image preprocessing** for better accuracy
        """)
    
    # Installation instructions
    with st.expander("🛠️ Installation Instructions"):
        st.markdown("""
        ### Required Dependencies
        
        Install the required packages using pip:
        
        ```bash
        pip install -r requirements.txt
        ```
        
        ### Additional Requirements
        
        **For Windows users:**
        1. **Tesseract OCR**: Download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
        2. **Visual C++ Redistributable**: May be required for some packages
        
        **For Linux users:**
        ```bash
        sudo apt-get install tesseract-ocr
        sudo apt-get install libtesseract-dev
        ```
        
        **For macOS users:**
        ```bash
        brew install tesseract
        ```
        """)

if __name__ == "__main__":
    main()
