#!/usr/bin/env python3
"""Module for serializing and deserializing data using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to convert.
        filename (str): The name of the output XML file.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
