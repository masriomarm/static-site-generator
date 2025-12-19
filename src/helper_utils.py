import os
import shutil


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
