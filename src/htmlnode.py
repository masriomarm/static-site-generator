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
        ret = []
        for k, v in self.props.items():
            temp = f' {k}="{v}"'  # Notice the leading space character
            ret.append(temp)
        return str.join("", ret)

    def __repr__(self):
        ret = f"""
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}
        """
        return ret


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        comp_tag_beg = ""
        comp_tag_end = ""
        comp_props = ""
        if self.tag:
            comp_tag_beg = f"<{self.tag}"
            comp_tag_end = f"</{self.tag}>"
        if self.props:
            comp_props = self.props_to_html()
            comp_props += ">"
        else:
            if self.tag:
                comp_tag_beg += ">"

        ret = f"{comp_tag_beg}{comp_props}{self.value}{comp_tag_end}"

        return ret
