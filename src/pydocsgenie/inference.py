import openai


def inference(input: str):
    """Performs an inference using OpenAI API to
    get the docstring for a python code.

    Parameters
    ----------
    input : str
        Code that needs a docstring

    Returns
    -------
    str
        Docstring of the code.
    """
    prompt = (
        f"""Generate a docstring along with code in the following example:

        def first(self, inod=0):
        
        Return the number of the first node.

        Parameters
        ----------
        inod : int, optional
            The first node number to consider as the "first node".
        Returns
        -------
        int
            The first node number within either selected or all nodes.
        Examples
        --------
        Return the first selected node.
        >>> nodes.first()
        1
        Return the first node after node 10.
        >>> nodes.first(inod=10)
        11
        self._itnod = inod
        return self.next()
    with in the following code with proper indentation:

    {input}
    """
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text


def inference_from_file(file: str):
    """Generates the docstrings for a whole file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    str
        File with the docstring.
    """
    f = open(file, "r")
    response = inference(f.read())
    f.close()
    return response