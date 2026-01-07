import shutil
import helper_utils as hu
from pathlib import Path


def main():
    curPath = Path(__file__)
    curDir = curPath.parent
    trgPath = Path.joinpath(curDir.parent, "public")  # target path
    srcPath = Path.joinpath(curDir.parent, "static")  # source path
    try:
        shutil.rmtree(trgPath)
    except FileNotFoundError:
        pass
    hu.util_copy_tree(srcPath, trgPath, debug=False)

    srcPath = Path.joinpath(curDir.parent, "content", "index.md")  # source path
    trgPath = Path.joinpath(curDir.parent, "public", "index.html")  # content path
    tmpPath = Path.joinpath(curDir.parent, "template.html")  # content path
    hu.generate_page(srcPath, tmpPath, trgPath)


main()
