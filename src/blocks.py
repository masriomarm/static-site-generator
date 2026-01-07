import re
from pprint import pprint
import block_node as bn
import htmlnode as hn


def markdown_to_blocks(text):
    pattern = r"\n{2,}"
    splits = re.split(pattern, text)
    ret = []
    for split in splits:
        s = split.strip()
        if s:
            ret.append(s)
    return ret


def markdown_to_html_node(markdown, debug=False):
    # - [ ] Split the markdown into blocks (you already have a function for this)
    blocks = markdown_to_blocks(markdown)
    ret = ""
    # - [ ] Loop over each block:
    if debug:
        print("====== Blocks ======")
        print("Blocks of length:", len(blocks))
        pprint(blocks)

    for block in blocks:
        if debug:
            print("====== Block node ======")
            pprint(block)
        blockNode = bn.create_block_node(block, debug)
        ret += blockNode.to_html()

    ret = hn.LeafNode("div", ret).to_html()

    return ret
