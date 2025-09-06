from enum import Enum


class TextType(Enum):
    TEXT = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = ""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise Exception("Not supported type")
        else:
            return (
                (self.text == other.text)
                and (self.text_type == other.text_type)
                and (self.url == other.url)
            )

    def __repr__(self):
        ret = f"""
        TextNode(
        \tText: "{self.text}",
        \tType: "{self.text_type.value}",
        \tURL: "{self.url}",
        )
        """
        return ret
