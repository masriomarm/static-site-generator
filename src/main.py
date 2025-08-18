import textnode as tn


def main():
    inst = tn.TextNode(
        "This is some anchor text", tn.TextNodeVariant.LINKS, "https://www.boot.dev"
    )
    print(inst)


main()
