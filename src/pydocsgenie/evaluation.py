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
