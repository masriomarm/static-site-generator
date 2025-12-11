from enum import Enum
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


class BlockNode:
    def __init__(self, val):
        self.val = val
        self.type: BlockType = bk.block_to_block_type(val)
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

    def to_html():
        raise NotImplementedError(
            "Each block type will override this method to render themselves as HTML"
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


# class BlockNodeQuote(BlockNode):
# class BlockNodeCode(BlockNode):
# class BlockNodeHeading(BlockNode):
# class BlockNodeListOrdered(BlockNode):
# class BlockNodeListUnordered(BlockNode):
