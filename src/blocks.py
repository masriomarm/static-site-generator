import re
from enum import Enum
import src.utils as ut
import src.htmlnode as hn


def markdown_to_blocks(text):
    pattern = r"\n{2,}"
    splits = re.split(pattern, text)
    return [s.strip() for s in splits]
    pass


class BlockType(Enum):
    paragraph = "paragraph"
    heading1 = "heading1"
    heading2 = "heading2"
    heading3 = "heading3"
    heading4 = "heading4"
    heading5 = "heading5"
    heading6 = "heading6"
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
        BlockType.heading1: (r"^#{1}\s+", 0),
        BlockType.heading2: (r"^#{2}\s+", 0),
        BlockType.heading3: (r"^#{3}\s+", 0),
        BlockType.heading4: (r"^#{4}\s+", 0),
        BlockType.heading5: (r"^#{5}\s+", 0),
        BlockType.heading6: (r"^#{6}\s+", 0),
        BlockType.code: (r"^.*`{3}.*`{3}$", re.MULTILINE | re.DOTALL),
        BlockType.quote: (r"^\s*>.*$", 0),
        BlockType.unordered_list: (r"^\s*-.*$", 0),
        BlockType.ordered_list: (r"^\s*\d+\..*$", 0),
    }

    for type, pat in pattern_type.items():
        if (
            type == BlockType.quote
            or type == BlockType.unordered_list
            or type == BlockType.ordered_list
        ):
            target_type = ret
            lines = block.strip().splitlines()
            for line in lines:
                match = re.match(pat[0], line, pat[1])
                if match:
                    target_type = type
                else:
                    target_type = ret
            ret = target_type
        else:
            match = re.match(pat[0], block, pat[1])
            if match:
                ret = type
                break

    return ret
