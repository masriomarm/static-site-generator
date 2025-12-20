import os
import shutil
import src.block_node as bn


def extract_title(heading):
    """
    It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    If there is no h1 header, raise an exception.
    extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
    """
    h1 = bn.BlockNodeHeading1(heading)
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
