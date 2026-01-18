from google import genai
import os
from dotenv import load_dotenv

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
