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
