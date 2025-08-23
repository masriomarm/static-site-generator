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


if __name__ == "__main__":
    unittest.main()
