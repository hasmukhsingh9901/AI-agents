import ast

def analyze_dependencies(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    return imports
