import re
from enum import Enum
from pprint import pprint
import src.utils as ut
import src.htmlnode as hn


def markdown_to_blocks(text):
    pattern = r"\n{2,}"
    splits = re.split(pattern, text)
    ret = []
    for split in splits:
        s = split.strip()
        if s:
            ret.append(s)
    return ret


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


def block_type_to_html_props(block_type: BlockType):
    tag = None
    converter = None
    match block_type:
        case BlockType.paragraph:
            tag = "p"
            converter = block_paragraph_to_html_node

        case BlockType.quote:
            tag = "blockquote"
            converter = block_quote_to_html_node

        case BlockType.code:
            tag = "code"
            converter = block_code_to_html_node

        case BlockType.unordered_list:
            tag = "ul"
            converter = block_unordered_list_to_html_node

        case BlockType.ordered_list:
            tag = "ol"
            converter = block_ordered_list_to_html_node

        case BlockType.heading1:
            tag = "h1"
            converter = block_heading1_to_html_node

        case BlockType.heading2:
            tag = "h2"
            converter = block_heading2_to_html_node

        case BlockType.heading3:
            tag = "h3"
            converter = block_heading3_to_html_node

        case BlockType.heading4:
            tag = "h4"
            converter = block_heading4_to_html_node

        case BlockType.heading5:
            tag = "h5"
            converter = block_heading5_to_html_node

        case BlockType.heading6:
            tag = "h6"
            converter = block_heading6_to_html_node

    return (tag, converter)


def block_paragraph_to_html_node(block, debug=False):
    pass


def block_quote_to_html_node(block, debug=False):
    pass


def block_code_to_html_node(block, debug=False):
    pass


def block_unordered_list_to_html_node(block, debug=False):
    pass


def block_ordered_list_to_html_node(block, debug=False):
    pass


def block_heading1_to_html_node(block, debug=False):
    pass


def block_heading2_to_html_node(block, debug=False):
    pass


def block_heading3_to_html_node(block, debug=False):
    pass


def block_heading4_to_html_node(block, debug=False):
    pass


def block_heading5_to_html_node(block, debug=False):
    pass


def block_heading6_to_html_node(block, debug=False):
    pass


def markdown_to_html_node(markdown, debug=False):
    # - [ ] Split the markdown into blocks (you already have a function for this)
    blocks = markdown_to_blocks(markdown)
    # - [ ] Loop over each block:
    if debug:
        print("====== Blocks ======")
        print("Blocks of length:", len(blocks))
        pprint(blocks)

    children_parent = []
    for block in blocks:
        block_type = block_to_block_type(block)
        blockTag, blockConverter = block_type_to_html_props(block_type)

        if debug:
            print("====== Block ======")
            pprint(block_type)
            pprint(blockTag)
            pprint(block)

        childrens = []
        # - [ ] Determine the type of block (you already have a function for this)
        nodes = []
        if block_type != BlockType.code:
            nodes = ut.text_to_textnodes(block)
            if debug:
                print("====== Nodes ======")
                pprint(nodes)
        for node in nodes:
            html_node = ut.text_node_to_html_node(node)
            leaf_node = hn.LeafNode(html_node.tag, html_node.value, html_node.props)
            childrens.append(leaf_node)
            if debug:
                print("====== Leaf node ======")
                leaf_node = leaf_node.to_html()
                pprint(leaf_node)

        parent = hn.ParentNode(blockTag, childrens)
        children_parent.append(parent)
        if debug:
            pprint(parent)
            print(parent.to_html())

    grandparent = hn.ParentNode("div", children_parent)
    ret = grandparent
    if debug:
        pprint(grandparent)
        print(grandparent.to_html())

    return ret
