from parser import extract_functions
from generator import generate_docstring

file_path = "test_sample.py"
functions = extract_functions(file_path)

for func in functions:
    print(f"\n{'='*50}")
    print(f"Function: {func['name']}")
    print(f"{'='*50}")
    docstring = generate_docstring(func)
    print(docstring)
