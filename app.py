import streamlit as st
from parser import extract_functions
from generator import generate_docstring
import tempfile

st.title("🤖 AI Code Documentation Generator")
st.caption("Upload Python files → Get instant docstrings powered by Gemini")

uploaded_file = st.file_uploader("Upload a Python file", type=['py'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    functions = extract_functions(tmp_path)
    
    st.success(f"Found {len(functions)} functions")
    
    for func in functions:
        with st.expander(f"📝 {func['name']}()"):
            with st.spinner("Generating docstring..."):
                docstring = generate_docstring(func)
                st.code(docstring, language='python')
                
                if st.button(f"Copy {func['name']}", key=func['name']):
                    st.code(docstring)
