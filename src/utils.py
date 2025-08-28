import textnode as tn
import htmlnode as hn


def text_node_to_html_node(text_node: tn.TextNode):
    match text_node.text_type:
        case tn.TextType.TEXT:
            return hn.HTMLNode(None, text_node.text, None, None)
        case tn.TextType.BOLD:
            return hn.HTMLNode("b", text_node.text, None, None)
        case tn.TextType.ITALIC:
            return hn.HTMLNode("i", text_node.text, None, None)
        case tn.TextType.CODE:
            return hn.HTMLNode("code", text_node.text, None, None)
        case tn.TextType.LINK:
            props = {
                "href": text_node.url,
            }
            return hn.HTMLNode("a", text_node.text, None, props)
        case tn.TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            return hn.HTMLNode("img", None, None, props)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    deli_vals = {
        "**": tn.TextType.BOLD,
        "`": tn.TextType.CODE,
        "_": tn.TextType.ITALIC,
    }
    ret = []
    for node in old_nodes:
        splits = node.text.split(delimiter)
        if len(splits) == 3:  # valid split
            temp = tn.TextNode(splits[0], tn.TextType.TEXT)
            ret.append(temp)
            temp = tn.TextNode(splits[1], deli_vals[delimiter])
            ret.append(temp)
            temp = tn.TextNode(splits[2], tn.TextType.TEXT)
            ret.append(temp)
        else:
            raise ValueError("Invalid markdown syntax - unmatched delimiters.")
    return ret
