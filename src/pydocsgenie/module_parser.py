"""Module containing functions for splitting python files into its module_orgs."""

import ast
import astunparse

def read_file(path):
    """
    Reads a file from the given `path` and returns its content as a string.
    
    Parameters
    ----------
    path: str
        The file path to read.
        
    Returns
    -------
    str
        The content of the file as a string.
    """
    with open(path, "r") as file:
        module_org = file.read()
    return module_org
    
def separate_input_functions(module_org):
    """
    Separates the functions and classes in a python module into a list of strings.
    
    Parameters
    ----------
    module_org :str
        The original module content as a string.
        
    Returns
    -------
    list 
        A list of strings, each string representing a function or class in the module.
    """
    module = ''.join(new_list for i, new_list in enumerate(module_org.split('"""')) if i % 2 == 0)
    tree = ast.parse(module)
    input_classes = [astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    if not input_classes:
        input_functions = [astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return input_functions
    return input_classes