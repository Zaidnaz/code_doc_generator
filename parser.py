import ast

def extract_functions(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
        tree = ast.parse(code)
    
    functions = []
    classes = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_info = {
                'type': 'function',
                'name': node.name,
                'args': [arg.arg for arg in node.args.args],
                'body': ast.get_source_segment(code, node),
                'lineno': node.lineno
            }
            functions.append(func_info)
        
        elif isinstance(node, ast.ClassDef):
            methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
            class_info = {
                'type': 'class',
                'name': node.name,
                'methods': [m.name for m in methods],
                'body': ast.get_source_segment(code, node)[:500],  # First 500 chars
                'lineno': node.lineno
            }
            classes.append(class_info)
    
    return functions, classes

def generate_class_docstring(class_info):
    """Generate docstring for classes"""
    from generator import client
    
    prompt = f"""Generate a Google-style docstring for this Python class:

{class_info['body']}

Include: class purpose, main attributes, and methods overview."""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text
