from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_readme(project_name, functions, classes, file_content):
    """Generate comprehensive README for the project"""
    
    func_names = [f['name'] for f in functions]
    class_names = [c['name'] for c in classes]
    
    prompt = f"""Generate a professional README.md for this Python project:

Project Name: {project_name}

Code Overview:
{file_content[:2000]}

Functions: {', '.join(func_names)}
Classes: {', '.join(class_names)}

Include these sections:
1. Project Title & Description
2. Features
3. Installation
4. Usage with code examples
5. API Documentation (function/class signatures)
6. Contributing
7. License (MIT)

Make it professional and GitHub-ready."""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text
