import textnode as tn
import htmlnode as hn
import re


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
    ret = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            ret.append(node)
            continue
        splits = node.text.split(delimiter, 2)
        while len(splits) >= 1:
            if len(splits) == 3:  # valid split
                temp = tn.TextNode(splits[0], tn.TextType.TEXT)
                if temp.text:
                    ret.append(temp)
                temp = tn.TextNode(splits[1], text_type)
                ret.append(temp)
                temp = tn.TextNode(splits[2], tn.TextType.TEXT)
                if temp.text:
                    splits = temp.text.split(delimiter, 2)
                else:
                    break
            elif len(splits) == 1:  # no more splits found
                temp = tn.TextNode(splits[0], tn.TextType.TEXT)
                if temp.text:
                    ret.append(temp)
                break
            else:
                raise ValueError("Invalid markdown syntax - unmatched delimiters.")
    return ret


def extract_markdown_images(text):
    # that takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    # that extracts markdown links instead of images. It should return tuples of anchor text and URLs
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes):
    delimiter = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    ret = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            ret.append(node)
            continue
        receieved = node.text
        splits = re.split(delimiter, receieved)
        found = re.findall(delimiter, receieved)
        for s in splits:
            if not s:
                continue
            node = None
            if s in found:
                # split text and link parts.
                alt_text = r"!\[([^\[\]]*)\]"
                found_text = re.findall(alt_text, s)[0]
                link = r"\(([^\(\)]*)\)"
                found_link = re.findall(link, s)[0]
                node = tn.TextNode(found_text, tn.TextType.IMAGE, found_link)
            else:
                node = tn.TextNode(s, tn.TextType.TEXT)
            ret.append(node)

    return ret


def split_nodes_link(old_nodes):
    delimiter = r"(\[[^\[\]]*\]\([^\(\)]*\))"
    ret = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            ret.append(node)
            continue
        receieved = node.text
        splits = re.split(delimiter, receieved)
        found = re.findall(delimiter, receieved)
        for s in splits:
            if not s:
                continue
            node = None
            if s in found:
                # split text and link parts.
                text = r"\[([^\[\]]*)\]"
                found_text = re.findall(text, s)[0]
                link = r"\(([^\(\)]*)\)"
                found_link = re.findall(link, s)[0]
                node = tn.TextNode(found_text, tn.TextType.LINK, found_link)
            else:
                node = tn.TextNode(s, tn.TextType.TEXT)
            ret.append(node)

    return ret


def text_to_textnodes(text):
    nodes = [tn.TextNode(text, tn.TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", tn.TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", tn.TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", tn.TextType.ITALIC)
    return nodes
