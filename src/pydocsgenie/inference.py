import openai
openai.api_key = "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"

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
        f"""Generate a docstring and a docstring example in sphinx style
    for the following code:\n"""
        + input
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=512,
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