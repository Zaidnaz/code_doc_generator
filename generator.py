from google import genai
import os
from dotenv import load_dotenv
import ast

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_docstring(func_info):
    prompt = f"""Generate a Google-style docstring for this Python function:

{func_info['body']}

Include: brief description, Args with types, Returns with type, and a usage example."""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

def insert_docstrings(file_path, functions_with_docs):
    """Insert generated docstrings into the original file"""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Sort by line number in reverse to avoid offset issues
    functions_with_docs.sort(key=lambda x: x['lineno'], reverse=True)
    
    for func in functions_with_docs:
        # Find the function definition line
        func_line = func['lineno'] - 1
        indent = len(lines[func_line]) - len(lines[func_line].lstrip())
        
        # Format docstring with proper indentation
        docstring_lines = func['docstring'].strip().split('\n')
        formatted_doc = ' ' * (indent + 4) + '"""' + docstring_lines[0] + '\n'
        for line in docstring_lines[1:]:
            formatted_doc += ' ' * (indent + 4) + line + '\n'
        formatted_doc += ' ' * (indent + 4) + '"""\n'
        
        # Insert after function definition
        lines.insert(func_line + 1, formatted_doc)
    
    return ''.join(lines)
