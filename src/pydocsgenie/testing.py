def evaluate_docstring(generated_docstring, reference_docstring):
    score = 0
    max_score = 10

    # Check correctness
    if generated_docstring == reference_docstring:
        score += 1

    # Check completeness
    if all(keyword in generated_docstring for keyword in ["Parameters", "Returns", "Examples"]):
        score += 1

    # Check clarity
    if len(generated_docstring) <= 150:
        score += 1

    # Check consistency
    if all(generated_docstring.startswith(prefix) for prefix in ["Parameters", "Returns", "Examples"]):
        score += 1

    # Check relevance to the code
    if all(keyword in generated_docstring for keyword in ["function", "inputs", "outputs"]):
        score += 1

    # Check readability
    lines = generated_docstring.split("\n")
    if all(len(line) <= 75 for line in lines):
        score += 1

    # Check examples
    if "Examples" in generated_docstring:
        score += 1

    # Check formatting
    if generated_docstring == reference_docstring:
        score += 1

    # Check conciseness
    if len(generated_docstring) <= 100:
        score += 1

    # Check example clarity
    if "Examples" in generated_docstring and all(example in generated_docstring for example in [">>>", "return"]):
        score += 1

    # Check PEP 8 style guide
    if all(keyword in generated_docstring for keyword in ["Capitalized", "period", "space"]):
        score += 1

    return score / max_score

import pathlib
import pathlib
import ast
import os

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

from pydocsgenie.inference import inference

THIS_PATH = pathlib.Path(__file__).parent.resolve()
TEST_PATH = (THIS_PATH / "test.py").absolute()

module = read_file(str(TEST_PATH))
result = separate_input_functions(module)
generated_docstring = inference(result)