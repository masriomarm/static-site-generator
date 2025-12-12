import unittest

import src.blocks as bk
import src.block_node as bn


class Testutils(unittest.TestCase):
    #     def test_block_list_ordered(self):
    #         md = """
    #         1. ordered list text 1 with `inline code`
    #         2. ordered list text 2 with **inline bold** and `inline code`
    #         3. ordered list text 3 with __inline italic__, **inline bold**, and `inline code`
    #         """
    #         node = bk.markdown_to_html_node(md)
    #         html = node.to_html()
    #         self.assertEqual(
    #             html,
    #             "<div><ol><li>ordered list text 1 with <code>inline code</code></li><li>ordered list text 2 with <b>inline bold</b> and <code>inline code</code></li><li>ordered list text 3 with <i>inline italic</i>, <b>inline bold</b>, and <code>inline code</code></li></ol></div>",
    #         )

    #     def test_block_list_unordered(self):
    #         md = """
    #         - unordered list text 1 with `inline code`
    #         - unordered list text 2 with **inline bold** and `inline code`
    #         - unordered list text 3 with __inline italic__, **inline bold**, and `inline code`
    #         """
    #         node = bk.markdown_to_html_node(md)
    #         html = node.to_html()
    #         self.assertEqual(
    #             html,
    #             "<div><ul><li>unordered list text 1 with <code>inline code</code></li><li>unordered list text 2 with <b>inline bold</b> and <code>inline code</code></li><li>unordered list text 3 with <i>inline italic</i>, <b>inline bold</b>, and <code>inline code</code></li></ul></div>",
    #         )

    def test_block_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = bk.markdown_to_html_node(md)
        html = node
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_block_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = bk.markdown_to_html_node(md)
        html = node
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
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.ordered_list)

    def test_block_type_list_unordered(self):
        md = """
        - unordered list text 1
        - unordered list text 2
        - unordered list text 3
        - unordered list text 4
        """
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.unordered_list)

    def test_block_type_quote(self):
        md = """
        > Quoted text 1
        > Quoted text 2
        > Quoted text 3
        > Quoted text 4
        """
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.quote)

    def test_block_type_code(self):
        md = """
        ``` python
        print("Testing...")
        ```
        """
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.code)

    def test_block_type_heading1(self):
        md = "# Heading1"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading1)

    def test_block_type_heading2(self):
        md = "## Heading2"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading2)

    def test_block_type_heading3(self):
        md = "### Heading3"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading3)

    def test_block_type_heading4(self):
        md = "#### Heading4"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading4)

    def test_block_type_heading5(self):
        md = "##### Heading5"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading5)

    def test_block_type_heading6(self):
        md = "###### Heading6"
        type = bn.block_to_block_type(md)
        self.assertEqual(type, bn.BlockType.heading6)

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
