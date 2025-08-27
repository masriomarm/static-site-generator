class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "Child classes will override this method to render themselves as HTML"
        )

    def props_to_html(self):
        # raise Exception(NotImplemented, "Todo")
        ret = ""
        if self.props:
            for k, v in self.props.items():
                ret += f' {k}="{v}"'  # Notice the leading space character
        return ret

    def __repr__(self):
        ret = f"""
        HTMLNode(
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}
        )
        """
        return ret


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")

        ret = self.value
        if self.tag:
            ret = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return ret

    def __repr__(self):
        ret = f"""
        LeafNode(
        Tag: {self.tag}
        Value: {self.value}
        Props: {self.props}
        )
        """
        return ret


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag for parent node.")
        if self.children is None:
            raise ValueError("Missing children for parent node.")

        ret = f"<{self.tag}>"
        for child in self.children:
            ret += child.to_html()
        ret += f"</{self.tag}>"

        return ret

    def __repr__(self):
        ret = f"""
        ParentNode(
        Tag: {self.tag}
        Children: {self.children}
        Props: {self.props}
        )
        """
        return ret
