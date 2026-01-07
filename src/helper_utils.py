import os
import shutil
import src.block_node as bn
import src.blocks as bk
from pathlib import Path
import difflib


def extract_title(heading):
    """
    It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    If there is no h1 header, raise an exception.
    extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
    """
    h1 = bn.BlockNodeHeading1(heading, debug=False)
    if not h1.head_val:
        raise ValueError(f"Invalid heading <{heading}>")
    return h1.head_val.strip()


def util_copy_tree(src, dst, debug=True):
    srcPath = os.path.abspath(os.fspath(src))
    if debug:
        print("Source path received:", srcPath)

    dstPath = os.path.abspath(os.fspath(dst))
    if debug:
        print("Destination path received:", srcPath)

    srcContents = os.listdir(srcPath)
    if debug:
        print("Source contents:\n", srcContents)
        for srcItem in srcContents:
            print(srcItem)

    srcContentsAbs = list(map(lambda p: os.path.abspath(p), srcContents))
    if debug:
        print("Source contents absolute:\n", srcContentsAbs)
        for srcItem in srcContentsAbs:
            print(srcItem)

    if not os.path.exists(dstPath):
        if debug:
            print("Destination not found. Creating...", dstPath)
        os.mkdir(dstPath)

    shutil.copytree(srcPath, dstPath, dirs_exist_ok=True)


def generate_page(from_path, template_path, dest_path, debug=False):
    """
    Create a generate_page(from_path, template_path, dest_path) function. It should:

        1. Print a message like "Generating page from from_path to dest_path using template_path".
        2. Read the markdown file at from_path and store the contents in a variable.
        3. Read the template file at template_path and store the contents in a variable.
        4. Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
        5. Use the extract_title function to grab the title of the page.
        6. Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
        7. Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    seperator = "<<<<<<>>>>>>>"
    with open(from_path, "r") as file:
        fileFrom = file.read()

    with open(template_path, "r") as file:
        fileTemplate = file.read()

    htmlGenerated = bk.markdown_to_blocks(fileFrom)
    if debug:
        print(seperator)
        print(htmlGenerated)

    htmlTitle = extract_title(htmlGenerated[0])
    if debug:
        print(seperator)
        print(htmlTitle)

    # if debug:
    #     contents = "\n\n".join(htmlGenerated)
    #     print(seperator)
    #     print(contents == fileFrom)
    #     diff = difflib.ndiff(
    #         contents.splitlines(keepends=True), fileFrom.splitlines(keepends=True)
    #     )
    #     print("".join(diff))
    #     print(seperator)

    htmlGenerated = bk.markdown_to_html_node(fileFrom, debug)
    if debug:
        print(seperator)
        print(htmlGenerated)

    placeHolders = {
        "{{ Title }}": htmlTitle,
        "{{ Content }}": htmlGenerated,
    }
    for k, v in placeHolders.items():
        if debug:
            print("Replacing <", k, ">", "with <", v, ">")
        fileTemplate = fileTemplate.replace(k, v)
    if debug:
        print(seperator)
        print("Final output")
        print(fileTemplate)

    # 7. Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    pathDest = Path(dest_path)
    if not os.path.exists(dest_path.parent):
        os.makedirs(pathDest.parent)

    with open(dest_path, "w") as file:
        file.write(fileTemplate)
