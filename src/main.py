import shutil
import helper_utils as hu
from pathlib import Path
import sys


def main():
    curPath = Path(__file__)
    curDir = curPath.parent
    prjRoot = curDir.parent

    srcPath = Path.joinpath(prjRoot, "static")
    if len(sys.argv) == 2:
        trgPath = Path.joinpath(prjRoot, "docs")
    else:
        trgPath = Path.joinpath(prjRoot, "public")
    try:
        shutil.rmtree(trgPath)
    except FileNotFoundError:
        pass
    hu.util_copy_tree(srcPath, trgPath, debug=False)

    if len(sys.argv) == 2:
        basePath = sys.argv[1]
        trgPath = Path.joinpath(prjRoot, "docs")
    else:
        basePath = "/"
        trgPath = Path.joinpath(prjRoot, "public")

    srcPath = Path.joinpath(prjRoot, "content")
    tmpPath = Path.joinpath(curDir.parent, "template.html")
    hu.generate_pages_recursive(srcPath, tmpPath, trgPath, basePath)


main()
