import shutil
import helper_utils as hu
from pathlib import Path


def main():
    curPath = Path(__file__)
    curDir = curPath.parent
    prjRoot = curDir.parent

    srcPath = Path.joinpath(prjRoot, "static")
    trgPath = Path.joinpath(prjRoot, "public")
    try:
        shutil.rmtree(trgPath)
    except FileNotFoundError:
        pass
    hu.util_copy_tree(srcPath, trgPath, debug=False)

    srcPath = Path.joinpath(prjRoot, "content")
    trgPath = Path.joinpath(prjRoot, "public")
    tmpPath = Path.joinpath(curDir.parent, "template.html")
    hu.generate_pages_recursive(srcPath, tmpPath, trgPath)


main()
