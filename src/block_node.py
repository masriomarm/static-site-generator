from enum import Enum
import src.blocks as bk


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


class BlockNode:
    def __init__(self, val):
        self.val = val
        self.type: BlockType = bk.block_to_block_type(val)
        self.tag = self.type.value
        self.children = []

    def __repr__(self):
        ret = f"""
        BlockNode(
        Type: {self.type}
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        )
        """
        return ret


# class BlockNodeParagraph(BlockNode):
# class BlockNodeQuote(BlockNode):
# class BlockNodeCode(BlockNode):
# class BlockNodeHeading(BlockNode):
# class BlockNodeListOrdered(BlockNode):
# class BlockNodeListUnordered(BlockNode):
