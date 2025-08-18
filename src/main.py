import textnode as tn


def main():
    inst = tn.TextNode(
        "This is some anchor text", tn.TextType.LINKS, "https://www.boot.dev"
    )
    print(inst)


main()
