import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTLMNode(unittest.TestCase):
    def test_props_to_html(self):
        children = []
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(children=children, props=props)
        ret = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(ret, expected)

    def test_props_to_html_2(self):
        children = []
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "more": "_blank",
        }
        node = HTMLNode(children=children, props=props)
        ret = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank" more="_blank"'

        self.assertEqual(ret, expected)

    def test_default_to_html(self):
        children = []
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(children=children, props=props)

        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
