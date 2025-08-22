import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
