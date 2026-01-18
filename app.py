import streamlit as st
from parser import extract_functions, generate_class_docstring
from generator import generate_docstring, insert_docstrings
from readme_generator import generate_readme
import tempfile
import os

st.set_page_config(page_title="AI Code Doc Generator", page_icon="🤖", layout="wide")

st.title("🤖 AI Code Documentation Generator")
st.caption("Upload Python files → Get instant docstrings, class docs & README powered by Gemini 2.5 Flash")

# Sidebar options
st.sidebar.header("⚙️ Options")
doc_style = st.sidebar.selectbox("Docstring Style", ["Google", "NumPy", "Sphinx"])
generate_readme_opt = st.sidebar.checkbox("Generate README", value=True)

uploaded_file = st.file_uploader("Upload a Python file", type=['py'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w') as tmp:
        tmp.write(uploaded_file.getvalue().decode('utf-8'))
        tmp_path = tmp.name
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📄 Original Code")
        original_code = uploaded_file.getvalue().decode('utf-8')
        st.code(original_code, language='python')
    
    with col2:
        st.subheader("📊 Analysis")
        functions, classes = extract_functions(tmp_path)
        st.metric("Functions Found", len(functions))
        st.metric("Classes Found", len(classes))
    
    # Generate documentation
    if st.button("✨ Generate Documentation", type="primary"):
        with st.spinner("Analyzing code with Gemini 2.5 Flash..."):
            
            # Document functions
            functions_with_docs = []
            for func in functions:
                docstring = generate_docstring(func)
                func['docstring'] = docstring
                functions_with_docs.append(func)
            
            # Document classes
            classes_with_docs = []
            for cls in classes:
                docstring = generate_class_docstring(cls)
                cls['docstring'] = docstring
                classes_with_docs.append(cls)
            
            # Insert docstrings into code
            documented_code = insert_docstrings(tmp_path, functions_with_docs + classes_with_docs)
            
            st.success("✅ Documentation generated!")
            
            # Show documented code
            st.subheader("📝 Documented Code")
            st.code(documented_code, language='python')
            
            # Download button
            st.download_button(
                label="⬇️ Download Documented File",
                data=documented_code,
                file_name=f"documented_{uploaded_file.name}",
                mime="text/plain"
            )
            
            # Generate README
            if generate_readme_opt:
                with st.spinner("Generating README..."):
                    readme_content = generate_readme(
                        uploaded_file.name.replace('.py', ''),
                        functions,
                        classes,
                        original_code
                    )
                    
                    st.subheader("📖 Generated README")
                    st.markdown(readme_content)
                    
                    st.download_button(
                        label="⬇️ Download README.md",
                        data=readme_content,
                        file_name="README.md",
                        mime="text/markdown"
                    )
    
    os.unlink(tmp_path)

st.sidebar.markdown("---")
st.sidebar.markdown("**Built with Gemini 2.5 Flash** 🚀")
