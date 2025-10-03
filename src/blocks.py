import re
from enum import Enum


def markdown_to_blocks(text):
    pattern = r"\n{2,}"
    splits = re.split(pattern, text)
    return [s.strip() for s in splits]
    pass


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block: str):
    """
    Takes a single block of markdown text as input and returns the `BlockType` representing the type of block it is.

    This will compare block to multiple regex.
    """
    ret = BlockType.paragraph

    pattern_type = {
        r"#{1,6}\s+": BlockType.heading,
    }

    for pat, type in pattern_type.items():
        match = re.match(pat, block)
        if match:
            ret = type
            break

    return ret
