def evaluate_docstring(generated_docstring, reference_docstring):
    score = 0
    max_score = 7

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

    # Check relevance
    if all(keyword in generated_docstring for keyword in ["function", "inputs", "outputs"]):
        score += 1

    # Check readability
    lines = generated_docstring.split("\n")
    if all(len(line) <= 75 for line in lines):
        score += 1

    # Check examples
    if "Examples" in generated_docstring:
        score += 1

    return score / max_score
