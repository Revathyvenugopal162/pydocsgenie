"""Module containing functions for splitting python files into its module_orgs."""

import ast
import json
import os

import astunparse


def read_file(path):
    with open(path, "r") as file:
        module_org = file.read()
    return module_org


def separate_input_functions(module_org):
    module = ""
    new_list = module_org.split('"""')
    for i in range(len(new_list)):
        if i % 2 == 0:
            module = module + new_list[i]
    tree = ast.parse(module)
    input = [astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    if input is None:
        input = [
            astunparse.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        ]
    return module


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
    "C:/Users/afernand/Documents/repositories/pymapdl/src/ansys/mapdl/core/inline_functions"
)
fill_json(inputs, outputs)
