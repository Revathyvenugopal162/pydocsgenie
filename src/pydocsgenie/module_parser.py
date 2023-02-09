"""Module containing functions for splitting python files into its methods."""

def module2class_split(module_str: str):
    """Splits a module into its component classes

    Parameters
    ----------
    module_str : str
        String containing the whole module.

    Returns
    -------
    List[str]
        List with each of the classes of the module in string format.
    """
    classes_list = ["class " + elem for elem in module_str.split("class ")[1:]]
    return classes_list


def split_methods(class_str: str):
    """Splits a class into its component methods.

    Parameters
    ----------
    class_str : str
        String containing the class.

    Returns
    -------
    List
        List with each of the methods of the class in string format.
    """
    methods_list = ["def " + elem for elem in class_str.split("def ")[1:]]
    return methods_list

def get_methods_from_module(module_str: str):
    """Gets a list with all the methods contained in this module.

    Parameters
    ----------
    module_str : str
        String containing the whole module.

    Returns
    -------
    List
        List with each of the methods of the module in string format.
        
    Examples
    --------
    >>> with open("test.py", "r") as file:
    >>>     module_str = file.read()
    >>> methods_list = get_methods_from_module(module_str=module_str)
    """
    classes = module2class_split(module_str=module_str)
    if classes is None:
        methods_nested = split_methods(class_str=module_str)
    methods_nested = [split_methods(class_str=class_str) for class_str in classes]

    # flattens the list. methods_nested format: [class1[method1, method2..], class2[method1, method2..]]
    methods_flatten = [method for class_methods in methods_nested for method in class_methods]
    return methods_flatten
