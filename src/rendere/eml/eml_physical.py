#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_physical

:Synopsis:

:Author:
    servilla

:Created:
    3/29/20
"""
import daiquiri

from rendere.eml.eml_utils import clean
from rendere.eml.eml_data_format import eml_data_format


logger = daiquiri.getLogger(__name__)


def eml_physical(phys: list) -> list:
    physical = list()
    for phy in phys:
        p = dict()
        p["Object Name"] = phy.find("./objectName").text.strip()
        size = phy.find("./size")
        if size is not None:
            value = clean(size.xpath("string()"))
            unit = size.attrib["unit"].strip()
            p["Size"] = f"{value} ({unit})"
        checksums = phy.findall(".//authentication")
        if len(checksums) > 0:
            for checksum in checksums:
                c = list()
                value = clean(checksum.xpath("string()"))
                method = checksum.attrib["method"].strip()
                c.append(f"{value} ({method})")
            p["Checksum(s)"] = c
        compression_methods = phy.findall(".//compressionMethod")
        if len(compression_methods) > 0:
            for compression_method in compression_methods:
                c = list()
                c.append(clean(compression_method.xpath("string()")))
            p["Compression Method"] = c
        encoding_methods = phy.findall(".//encodingMethod")
        if len(encoding_methods) > 0:
            for encoding_method in encoding_methods:
                c = list()
                c.append(clean(encoding_method.xpath("string()")))
            p["Encoding Method"] = c
        character_encoding = phy.find("./characterEncoding")
        if character_encoding is not None:
            value = clean(character_encoding.xpath("string()"))
            p["Character Encoding"] = value
        p["Data Format"] = eml_data_format(phy.find("./dataFormat"))
        physical.append(p)
    return physical
