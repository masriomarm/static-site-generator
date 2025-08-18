from enum import Enum


class TextNodeVariant(Enum):
    TEXT = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextNodeVariant, url: str):
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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
