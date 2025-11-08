import unittest

import src.blocks as bk


class Testutils(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = bk.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_block_type_list_ordered(self):
        md = """
        1. ordered list text 1
        2. ordered list text 2
        3. ordered list text 3
        4. ordered list text 4
        """
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.ordered_list)

    def test_block_type_list_unordered(self):
        md = """
        - unordered list text 1
        - unordered list text 2
        - unordered list text 3
        - unordered list text 4
        """
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.unordered_list)

    def test_block_type_quote(self):
        md = """
        > Quoted text 1
        > Quoted text 2
        > Quoted text 3
        > Quoted text 4
        """
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.quote)

    def test_block_type_code(self):
        md = """
        ``` python
        print("Testing...")
        ```
        """
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.code)

    def test_block_type_heading1(self):
        md = "# Heading1"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading1)

    def test_block_type_heading2(self):
        md = "## Heading2"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading2)

    def test_block_type_heading3(self):
        md = "### Heading3"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading3)

    def test_block_type_heading4(self):
        md = "#### Heading4"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading4)

    def test_block_type_heading5(self):
        md = "##### Heading5"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading5)

    def test_block_type_heading6(self):
        md = "###### Heading6"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading6)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = bk.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple_breaks(self):
        md = """
This is **bolded** paragraph






This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
        """
        blocks = bk.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


if __name__ == "__main__":
    unittest.main()
