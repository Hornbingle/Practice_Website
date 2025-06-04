from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            prop_dictionary_link = {}
            if "href" in text_node.props:
                prop_dictionary_link["href"] = text_node.props["href"]
            else:
                raise Exception("Text node has no href")
            return LeafNode("a", text_node.text, prop_dictionary_link)
        case TextType.IMAGE:
            prop_dictionary_img = {}
            if "src" in text_node.props:
                prop_dictionary_img["src"] = text_node.props["src"]
            else:
                raise Exception("Text node has no src")
            if "alt" in text_node.props:
                prop_dictionary_img["alt"] = text_node.props["alt"]
            else:
                raise Exception("Text node has no alt")
            return LeafNode("img", "", prop_dictionary_img)
        case _:
            raise Exception("Text node has an invalid text type")