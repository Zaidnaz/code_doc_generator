import ast

def extract_functions(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
        tree = ast.parse(code)
    
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_info = {
                'name': node.name,
                'args': [arg.arg for arg in node.args.args],
                'body': ast.get_source_segment(code, node),
                'lineno': node.lineno
            }
            functions.append(func_info)
    return functions
