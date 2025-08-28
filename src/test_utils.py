import unittest

import utils as ut
import textnode as tn
import htmlnode as hn


class Testutils(unittest.TestCase):
    def test_text(self):
        node = tn.TextNode("This is a text node", tn.TextType.TEXT)
        html_node: hn.HTMLNode = ut.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_code(self):
        node = tn.TextNode("This is text with a `code block` word", tn.TextType.TEXT)
        new_nodes = ut.split_nodes_delimiter([node], "`", tn.TextType.CODE)

        expected = [
            tn.TextNode("This is text with a ", tn.TextType.TEXT),
            tn.TextNode("code block", tn.TextType.CODE),
            tn.TextNode(" word", tn.TextType.TEXT),
        ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_code_unbalanced(self):
        node = tn.TextNode("This is text with a `code block word", tn.TextType.TEXT)
        with self.assertRaises(ValueError):
            ut.split_nodes_delimiter([node], "`", tn.TextType.CODE)

    def test_split_nodes_bold(self):
        node = tn.TextNode(
            "This is text with a **bolded phrase** word", tn.TextType.TEXT
        )
        new_nodes = ut.split_nodes_delimiter([node], "**", tn.TextType.CODE)

        expected = [
            tn.TextNode("This is text with a ", tn.TextType.TEXT),
            tn.TextNode("bolded phrase", tn.TextType.BOLD),
            tn.TextNode(" word", tn.TextType.TEXT),
        ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_bold_unbalanced(self):
        node = tn.TextNode("This is text with a **bolded phrase word", tn.TextType.TEXT)
        with self.assertRaises(ValueError):
            ut.split_nodes_delimiter([node], "**", tn.TextType.CODE)

    def test_split_nodes_italic(self):
        node = tn.TextNode("This is text with a _italic phrase_ word", tn.TextType.TEXT)
        new_nodes = ut.split_nodes_delimiter([node], "_", tn.TextType.CODE)

        expected = [
            tn.TextNode("This is text with a ", tn.TextType.TEXT),
            tn.TextNode("italic phrase", tn.TextType.ITALIC),
            tn.TextNode(" word", tn.TextType.TEXT),
        ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_italic_unbalanced(self):
        node = tn.TextNode("This is text with a _italic phrase word", tn.TextType.TEXT)
        with self.assertRaises(ValueError):
            ut.split_nodes_delimiter([node], "_", tn.TextType.CODE)


if __name__ == "__main__":
    unittest.main()
