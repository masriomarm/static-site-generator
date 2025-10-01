import re


def markdown_to_blocks(text):
    pattern = r"\n{2,}"
    splits = re.split(pattern, text)
    return [s.strip() for s in splits]
    pass
