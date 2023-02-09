"""Module containing functions for splitting python files into its module_orgs."""

import ast
import astunparse

def read_file(path):
    with open(path, "r") as file:
        module_org = file.read()
    return module_org
    
def separate_input_functions(module_org):
    module = ''
    new_list = module_org.split('"""')
    for i in range (len(new_list)):
        if i % 2 == 0:
            module = (module + new_list[i])
    tree = ast.parse(module)
    input = [astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    if input is None:
        input = [astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return input