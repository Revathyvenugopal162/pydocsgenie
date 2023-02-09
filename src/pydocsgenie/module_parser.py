"""Module containing functions for splitting python files into its module_orgs."""

import ast
import json
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


def fill_json(inputs, outputs):
    f = open("dataset.jsonl", "w")
    for i in range(len(inputs)):
        prompt = (
            "Add a sphinx docstring and docstring examples to the following code:\n"
            + inputs[i]
        )
        completion = outputs[i]
        sample = "{\"prompt\": \"" + prompt +  "\", \"completion\": \"" + completion + "\"}"
        f.write(str(sample))
        f.write("\n")
    f.close()


def get_dataset(path: str):
    """_summary_

    Parameters
    ----------
    path : str
        _description_

    Returns
    -------
    _type_
        _description_

    Examples
    --------
    >>>inputs, outputs = get_dataset("path/to/modules")
    >>>fill_json(inputs, outputs)
    """
    inputs = []
    outputs = []
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            file_str = read_file(f)
            input = separate_input_functions(file_str)
            output = file_str
            inputs.append(input)
            outputs.append(output)
    return inputs, outputs


inputs, outputs = get_dataset(
    "path/to/modules"
)
fill_json(inputs, outputs)