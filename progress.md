# `CH2-L5`

`ParentNode`

I heard you like recursion.

Our new `ParentNode` class will handle the nesting of HTML nodes inside of one another. Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
Assignment

    Create another child class of HTMLNode called ParentNode. Its constructor should differ from HTMLNode in that:
        The tag and children arguments are not optional
        It doesn't take a value argument
        props is optional
        (It's the exact opposite of the LeafNode class)
    Add a .to_html method.
        If the object doesn't have a tag, raise a ValueError.
        If children is a missing value, raise a ValueError with a different message.
        Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node).

You can iterate over all the children and call `to_html` on each, concatenating the results and injecting them between the opening and closing tags of the parent.

For example, this node and its children:

```
node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
```

```
node.to_html()
```

Should convert to:

```
<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
```

Don't worry about indentation or pretty-printing. If pretty-printed it would look like this:

```
<p>
  <b>Bold text</b>
  Normal text
  <i>italic text</i>
  Normal text
</p>
```

Most editors are easily configured to auto-format HTML on save, so we won't worry about implementing that in our code.

    I wrote many tests for this class. I recommend you do the same, there is a lot of room for error. Test all the edge cases you can think of, including nesting ParentNode objects inside of one another, multiple children, and no children. Here's a couple to get you started:

```
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
```

Run and submit the CLI tests from the root of the project.

# `CH2-L4`

`LeafNode`

Time to render some HTML strings!

A `LeafNode` is a type of `HTMLNode` that represents a single HTML tag with no children. For example, a simple <p> tag with some text inside of it:

```
<p>This is a paragraph of text.</p>
```

We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children. In this next example, <p> is not a leaf node, but <b> is.

```
<p>
  This is a paragraph. It can have a lot of text inside tbh.
  <b>This is bold text.</b>
  This is the last sentence.
</p>
```

Assignment

    Create a child class of `HTMLNode` called `LeafNode`. Its constructor should differ slightly from the `HTMLNode` class because:
        It should not allow for any children
        Both the value and tag data members should be required (even though the tag's value may be None), while props can remain optional like the `HTMLNode` constructor.

Use the `super()` function to call the constructor of the `HTMLNode` class.

    Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).
        If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
        If there is no tag (e.g. it's None), the value should be returned as raw text.
        Otherwise, it should render an HTML tag. For example, these leaf nodes:

```
LeafNode("p", "This is a paragraph of text.").to_html()
"<p>This is a paragraph of text.</p>"
```

```
LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
"<a href="https://www.google.com">Click me!</a>"
```

    Add some tests. Here's one to get you started:

```
def test_leaf_to_html_p(self):
    node = `LeafNode`("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
```

Add more tests for different tag types.

Run and submit the CLI tests from the root of the project.

# `CH2-L3`

HTMLNode

Next, we need a way to represent HTML nodes.

    Our "TextNode" class represents the various types of inline text that can exist in HTML and Markdown.
    Our "HTMLNode" class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). It can be block level or inline, and is designed to only output HTML.

Assignment

    Create a new file called htmlnode.py in the src directory and define a class called HTMLNode in it.
    The HTMLNode class should have 4 data members set in the constructor:
        tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        children - A list of HTMLNode objects representing the children of this node
        props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    Perhaps counterintuitively, every data member should be optional and default to None:
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
    Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.
    Add a props_to_html(self) method. It should return a string that represents the HTML attributes of the node. For example, if self.props is:

{
    "href": "https://www.google.com",
    "target": "_blank",
}

Then self.props_to_html() should return:

 href="https://www.google.com" target="_blank"

Notice the leading space character before href and before target. This is important. HTML attributes are always separated by spaces.

    Add a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
    Create some tests for the HTMLNode class (at least 3). I used a new file called src/test_htmlnode.py. Create a few nodes and make sure the props_to_html method works as expected.

Run and submit the CLI tests.

# `CH2-L2`

TextNode Tests

Unit tests are a way to verify that the code you write works as expected. In other Boot.dev courses, you write code that passes the unit tests we provide. As a developer, you'll be expected to write your own tests to ensure that individual pieces of your code, "units", work as expected.

It can feel like a lot of extra work...

...but it's often worth it, especially if the logic you're testing is particularly complex while simultaneously easy to test (e.g. it doesn't rely on external stuff like files or the network). Once you have some good tests, you can run them whenever you make changes to ensure you didn't break anything.
Assignment

    Create a new script in the root of the project called test.sh. This will be a convenient way to run our tests. It should contain:

```
python3 -m unittest discover -s src
```

This command tells Python to use the standard library's unittest module to run all the tests (discover) it can find in the src directory.

    Create a test_textnode.py file in the src directory. This is where we'll write our tests for the TextNode class. Here's a file with a single test:

```
import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
```

This test creates two TextNode objects with the same properties and asserts that they are equal. Notice the missing url argument which should have a default value of None. If you run your tests with ./test.sh, you should see that the test passes.

    Add some test cases by adding methods to the TestTextNode class to verify that the TextNode class works as expected. You can use the following methods to compare the objects:
        self.assertEqual - if the inputs are equal the test passes
        self.assertNotEqual - if the inputs are not equal the test passes
    Add even more test cases (at least 3 in total) to check various edge cases, like when the url property is None, or when the text_type property is different. You'll want to make sure that when properties are different, the TextNode objects are not equal.

Run and submit the CLI tests.
Tips

    All test functions and file names must start with test_ to be discoverable by unittest.
    You may need to make test.sh executable by running:

```
chmod +x test.sh
```

# `CH2-L1`

TextNode

We're going to need a way to represent all the different types of inline text. We're going to be parsing Markdown text, and outputting it to HTML, so we need an intermediate representation of the text in our code.

When I say "inline" I just mean text that is part of a larger block of text. For us, this includes:

    text (plain)
    **Bold text**
    _Italic text_
    `Code text`
    Links, in this format: [anchor text](url)
    Images, in this format: ![alt text](url)

Everything else we're considering block level, like headings, paragraphs, and bullet lists, and we'll handle those later.
Assignment

    Create a simple main.sh shell script in the root of the project. This will be a convenient way to run our code. It should contain:

```
python3 src/main.py
```

    Create a src directory with a main.py python file. This is where we'll write our Python code. Make it print "hello world", and make sure that running the main.sh script runs the main.py file and prints "hello world":

```
./main.sh
# hello world
```

    Create a .gitignore file in the root of the project. It should contain:

```
__pycache__/
```

This will prevent autogenerated __pycache__ directories from being committed to Git. Finally, create a src/textnode.py file, and read on to see what it should contain.

    In textnode.py create an enum called TextType. It should cover all the types of text nodes mentioned above.

Here's an example of how you can create an enum:

```
from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"
```

    In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:
        self.text - The text content of the node
        self.text_type - The type of text this node contains, which is a member of the TextType enum.
        self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    Create an __eq__ method that returns True if all of the properties of two TextNode objects are equal. Our future unit tests will rely on this method to compare objects.
    Create a __repr__ method that returns a string representation of the TextNode object. It should look like this:

TextNode(TEXT, TEXT_TYPE, URL)

Where TEXT, TEXT_TYPE, and URL are the values of the text, text_type, and url properties, respectively.

You can get the string representation of the text_type enum by using the .value field.

    Create a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed:

TextNode(This is some anchor text, link, https://www.boot.dev)

Run and submit the CLI tests from the root of the project.

You can delete the files in the public directory, they aren't needed anymore.
Tips

    You may need to make main.sh executable by running:

```
chmod +x main.sh
```

    In Python, if you want to use code from one file in another file, you need to import it. For example, to use a SuperCar class from a cars.py file in a main.py file in the same directory, you would write:

```
from cars import SuperCar
```

# `CH1-L7`

Architecture

We'll dive into code in the next chapter, but first, I want to give you a high-level architecture for our static site generator.

![architecture](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/UKCNg8E-1280x607.png)

The flow of data through the full system is:

    Markdown files are in the /content directory. A template.html file is in the root of the project.
    The static site generator (the Python code in src/) reads the Markdown files and the template file.
    The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
    We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our local machine).
    We open a browser and navigate to http://localhost:8888 to view the rendered site.

How the SSG Works

The vast majority of our coding will happen in the src/ directory because almost all of the work is done in steps 2 and 3 above. Here's a rough outline of what the final program will do when it runs:

    Delete everything in the /public directory.
    Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
    Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
        Open the file and read its contents.
        Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
        Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
            Raw markdown -> TextNode -> HTMLNode
        Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
        Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
        Write the full HTML string to a file for that page in the /public directory.

How We're Gonna Build It

We're not going to build the program in the same order that it runs... that's often not the best way to build large projects. Instead, we'll tackle individual problems that we know we'll need to solve and use unit tests to make sure they work as expected. Then we'll put the pieces together into a working program as we get closer to the end.

You don't need to memorize the information on this page, but come back to review it if you ever feel lost in the details.

# `CH1-L5`

Cheat Sheet

This cheat sheet provides a quick reference for all the HTML and Markdown syntax you'll need to complete this project. Feel free to bookmark this page or open it in another tab so you can come back to it as you work on this project.
References

    [MarkdownGuide.org](https://www.markdownguide.org/cheat-sheet/)
    [HTML Element Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

Discord, GitHub, and ChatGPT all support Markdown messages. When you use Markdown on those platforms it will render beautifully.
HTML Headings

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

Markdown Headings

```
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
```

HTML Paragraphs

```
<p>This is a paragraph of text.</p>
```

Markdown Paragraphs

This is a paragraph of text.

HTML Bold

```
<p>This is a <b>bold</b> word.</p>
```

Markdown Bold

This is a **bold** word.

HTML Italics

<p>This is an <i>italic</i> word.</p>

Markdown Italics

This is an _italic_ word.

Note: *this is italic* and _this is italic_ both work in markdown, but we'll use _italic_ in this project.
HTML Links

This is a paragraph with a <a href="https://www.google.com">link</a>.

Markdown Links

This is a paragraph with a [link](https://www.google.com).

HTML Images

<img src="url/of/image.jpg" alt="Description of image" />

Markdown Images

![alt text for image](url/of/image.jpg)

HTML Unordered Lists

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

Markdown Unordered Lists

- Item 1
- Item 2
- Item 3

Note: - Item 1 and * Item 1 both work in markdown, but we'll use - Item 1 in this project.
HTML Ordered Lists

<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>

Markdown Ordered Lists

1. Item 1
2. Item 2
3. Item 3

HTML Quotes

<blockquote>This is a quote.</blockquote>

Markdown Quotes

> This is a quote.

HTML Code

<code>This is code</code>

Markdown Code

```
This is code
```

# `CH1-L4`

Markdown

Writing HTML by hand sucks. Even if you're a grubby front-end programmer, you probably don't want to write entire documents in raw HTML.

Writing Markdown is pure bliss. Markdown is a less-verbose markup language designed for ease of writing. The trouble is web browsers don't understand Markdown. They only understand HTML and CSS. The #1 job of a static site generator is to convert Markdown into HTML.

Instead of writing a verbose HTML list:

``` html
<ul>
  <li>I really</li>
  <li>hate writing</li>
  <li>in raw html</li>
</ul>
```

We can write this in Markdown:

``` markdown
- I really
- hate writing
- in raw html
```

Our static site generator will take a directory of Markdown files (one for each web page), and build a directory of HTML files. Because we're not savages, we'll also include a single CSS file to style the site.

This lesson, and every lesson on Boot.dev, is written in Markdown!

# `CH1-L3`

CSS

CSS (Cascading Style Sheets) is another "not-really-a-programming-language" that styles HTML elements. It's a way to dress up your HTML with colors, fonts, responsive layouts, animations, etc.

/* Make all <h1> HTML elements red */
h1 {
  color: red;
}

Or maybe we want the max-width of our paragraphs to be 50% of the screen width:

/* Make all <p> HTML elements 50% of the screen width */
p {
  max-width: 50%;
}

Assignment

    Copy and paste the following CSS into a file called styles.css in the public directory:

``` css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #1f1f23;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
h1 {
  color: #ffffff;
  margin-bottom: 20px;
}
p {
  color: #999999;
  margin-bottom: 20px;
}
a {
  color: #6568ff;
}
```

    Link the styles.css file in your index.html file by adding a <link> tag to the <head> section:

``` HTML
<head>
  <title>Why Frontend Development Sucks</title>
  <link rel="stylesheet" href="/styles.css" />
</head>
```

You can kill your server with Ctrl+C and restart it:

from inside the public directory
`python3 -m http.server 8888`

Run and submit the CLI tests with the server running.
Tip

If you suspect that you're having caching issues, try clearing your browser cache and reloading the page.

# `CH1-L2`

HTML

The primary output of a static site generator is HTML (HyperText Markup Language), because HTML contains all the content of a web page.

HTML is a simple language for structuring content. It's not a "programming" language in the sense that it doesn't have variables, loops, or conditionals.

HTML is a way to format text, images, links, and other media so that a web browser can render it in a GUI. Here's a simple HTML file:

<html>
  <head>
    <title>Why Frontend Development Sucks</title>
  </head>
  <body>
    <h1>Front-end Development is the Worst</h1>
    <p>
      Look, front-end development is for script kiddies and soydevs who can't
      handle the real programming. I mean, it's just a bunch of divs and spans,
      right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
      red." What a joke.
    </p>
    <p>
      Real programmers code, not silly markup languages. They code on Arch
      Linux, not macOS, and certainly not Windows. They use Vim, not VS Code.
      They use C, not HTML. Come to the
      <a href="https://www.boot.dev">backend</a>, where the real programming
      happens.
    </p>
  </body>
</html>

HTML is a tree-like structure where each "tag" (e.g. <p>, the bits enclosed in angle brackets) can contain other tags, and the whole thing is enclosed in an outermost <html> tag. Let's break down the structure of this HTML file:

    <html> is the root element of the document.
    <head> contains metadata about the document. Anything in the <head> is not rendered visibly in the browser window.
        <title> is the title of the document, which is displayed in the browser tab.
    <body> contains the content of the document, which is what is rendered in the browser window.
        <h1> is a top-level heading.
        <p> is a paragraph of text.
        <a> is a hyperlink. The href attribute is the URL the link points to. Attributes are key-value pairs that provide additional information about an element, like href="https://www.boot.dev".

Assignment

    Create a new repo on GitHub and clone it in your workspace. This is the root of your project.
    Add a directory to your project called public and save the HTML above into a file called index.html in the public directory.
    Change directories to the public directory and use Python's built-in HTTP server to serve the contents of the public directory:

cd public
python3 -m http.server 8888

    Open your browser and paste in the URL of your server, (http://localhost:8888 if you used port 8888 as suggested) into the address bar. You should see your file rendered as a web page! While the server is running, open a new terminal window.

Run and submit the CLI tests using the Boot.dev CLI tool.

# `CH1-L1`

Build a Static Site Generator

Let's build a static site generator from scratch!

Check out this live demo of what you'll build in this course! But you won't just build this site, you'll build the tool that builds this site. It's pretty meta. You'll also deploy yours to a live URL on the internet, just like mine.
What Is a Static Site Generator?

A static site generator takes raw content files (like Markdown and images) and turns them into a static website (a mix of HTML and CSS files).

Static sites are very popular in the real world for blogs and other content-heavy websites because they're lightning-fast, secure, and easy to host. For example, the Boot.dev Blog is a production-level static site generated with Hugo.
Static vs. Dynamic Sites

A static site is what it sounds like... static. The content is always the same. Users can not:

    Upload files
    Log in
    Leave comments
    Save preferences

You would need a dynamic site for that stuff, which is usually powered by a database and a custom web server. Static sites are great for:

    Blogs
    Portfolios
    Landing pages
    Documentation

Assignment

We'll be using the Boot.dev CLI to run and submit the CLI tests for some of the lessons in this project. Make sure you have it installed.

Run and submit the CLI tests.

The tests just ensure that the CLI is installed and configured correctly.
