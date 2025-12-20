from enum import Enum
import re
import src.blocks as bk
import src.utils as ut
import src.htmlnode as hn


class BlockType(Enum):
    paragraph = "p"
    heading1 = "h1"
    heading2 = "h2"
    heading3 = "h3"
    heading4 = "h4"
    heading5 = "h5"
    heading6 = "h6"
    code = "code"
    quote = "blockquote"
    unordered_list = "ul"
    ordered_list = "ol"


def block_to_block_type(block: str) -> BlockType:
    """
    Takes a single block of markdown text as input and returns the `BlockType` representing the type of block it is.

    This will compare block to multiple regex.
    """
    ret: BlockType = BlockType.paragraph

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


class BlockNode:
    def __init__(self, val, debug=False):
        self.val = val
        if debug:
            print("Block node val =", self.val)
        self.type: BlockType = block_to_block_type(self.val)
        self.tag = self.type.value
        self.children = []
        self.textNodes = []

    def __repr__(self):
        ret = f"""
        BlockNode(
        Type: `{self.type}`
        Tag: `{self.tag}`
        Value: `{self.val}`
        TextNodes: `{self.textNodes}`
        Children: `{self.children}`
        )
        """
        return ret

    def to_html(self):
        raise NotImplementedError(
            f"Each block type must override this method to render themselves as HTML. Currently not implemented for {type(self)}"
        )


class BlockNodeParagraph(BlockNode):
    def __init__(self, val):
        super().__init__(val)
        self.textNodes = ut.text_to_textnodes(self.val)
        for node in self.textNodes:
            html_node = ut.text_node_to_html_node(node)
            leaf_node = hn.LeafNode(html_node.tag, html_node.value, html_node.props)
            self.children.append(leaf_node)

    def to_html(self):
        return hn.ParentNode(self.tag, self.children).to_html()


class BlockNodeQuote(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        lines = self.val.split("\n")
        self.quote_val = ""
        if debug:
            print(lines)
        for line in lines:
            pattern = (r"^\s*> (.*)$", re.DOTALL)
            matches = re.search(pattern[0], line, pattern[1])
            if debug:
                print("matches =", matches)
            self.quote_val += matches.group(1) + "\n"
        if debug:
            print("quote val =", self.quote_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.quote_val).to_html()


class BlockNodeCode(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^.*`{3}\n+(.*)`{3}$", re.MULTILINE | re.DOTALL)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.code_val = matches.group(1).lstrip()
        if debug:
            print("matches =", matches)
            print("code val =", self.code_val)

    def to_html(self):
        return hn.LeafNode(
            "pre", (hn.LeafNode(self.tag, self.code_val).to_html())
        ).to_html()


class BlockNodeHeading1(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{1}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()


class BlockNodeHeading2(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{2}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()


class BlockNodeHeading3(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{3}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()


class BlockNodeHeading4(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{4}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()


class BlockNodeHeading5(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{5}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()


class BlockNodeHeading6(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        pattern = (r"^#{6}\s(.*)", 0)
        matches = re.search(pattern[0], self.val, pattern[1])
        self.head_val = matches.group(1)
        if debug:
            print("matches =", matches)
            print("heading val =", self.head_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.head_val).to_html()

    pass


class BlockNodeListOrdered(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        lines = self.val.split("\n")
        self.list_val = ""
        if debug:
            print(lines)
        for line in lines:
            pattern = (r"^\s*\d+\. (.*)$", 0)
            matches = re.search(pattern[0], line, pattern[1])
            if debug:
                print("matches =", matches)
            item = matches.group(1)
            item = hn.LeafNode("li", item).to_html()
            self.list_val += item
        if debug:
            print("list val =", self.list_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.list_val).to_html()


class BlockNodeListUnordered(BlockNode):
    def __init__(self, val, debug=False):
        super().__init__(val)
        lines = self.val.split("\n")
        self.list_val = ""
        if debug:
            print(lines)
        for line in lines:
            pattern = (r"^\s*- (.*)$", 0)
            matches = re.search(pattern[0], line, pattern[1])
            if debug:
                print("matches =", matches)
            item = matches.group(1)
            item = hn.LeafNode("li", item).to_html()
            self.list_val += item
        if debug:
            print("list val =", self.list_val)

    def to_html(self):
        return hn.LeafNode(self.tag, self.list_val).to_html()


block_type_map = {
    BlockType.paragraph: BlockNodeParagraph,
    BlockType.heading1: BlockNodeHeading1,
    BlockType.heading2: BlockNodeHeading2,
    BlockType.heading3: BlockNodeHeading3,
    BlockType.heading4: BlockNodeHeading4,
    BlockType.heading5: BlockNodeHeading5,
    BlockType.heading6: BlockNodeHeading6,
    BlockType.code: BlockNodeCode,
    BlockType.quote: BlockNodeQuote,
    BlockType.unordered_list: BlockNodeListUnordered,
    BlockType.ordered_list: BlockNodeListOrdered,
}


def create_block_node(block_string) -> BlockNode:
    blockType = block_to_block_type(block_string)
    childClass = block_type_map.get(blockType)
    if childClass is None:
        raise NotImplementedError(
            f"Block node child class for BlockType {blockType} not found."
        )
    return childClass(block_string)
