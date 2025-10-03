import unittest

import blocks as bk


class Testutils(unittest.TestCase):
    def test_block_type_heading1(self):
        md = "# Heading1"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

    def test_block_type_heading2(self):
        md = "## Heading2"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

    def test_block_type_heading3(self):
        md = "### Heading3"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

    def test_block_type_heading4(self):
        md = "#### Heading4"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

    def test_block_type_heading5(self):
        md = "##### Heading5"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

    def test_block_type_heading6(self):
        md = "###### Heading6"
        type = bk.block_to_block_type(md)
        self.assertEqual(type, bk.BlockType.heading)

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
