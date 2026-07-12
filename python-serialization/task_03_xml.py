import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs a Python dictionary from it.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    reconstructed_dict = {}
    for child in root:
        reconstructed_dict[child.tag] = child.text
    return reconstructed_dict
