#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml

:Synopsis:

:Author:
    servilla

:Created:
    3/19/20
"""
import daiquiri
from lxml import etree


versions = {
        "eml://ecoinformatics.org/eml-2.1.0": "2.1.0",
        "eml://ecoinformatics.org/eml-2.1.1": "2.1.1",
        "https://eml.ecoinformatics.org/eml-2.2.0": "2.2.0",
}


class Eml:
    def __init__(self, eml_root):
        pass


class Eml210(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


class Eml211(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


class Eml220(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


def eml_factory(eml_file: str):
    with open(eml_file, "r", encoding="utf-8") as f:
        eml_str = f.read()
    eml = eml_str.encode("utf-8")
    eml_root = etree.fromstring(eml)
    version = versions[eml_root.nsmap["eml"]]
    if version == "2.1.0":
        return Eml210(eml_root)
    elif version == "2.1.1":
        return Eml211(eml_root)
    else: # version == "2.2.0":
        return Eml220(eml_root)


def main():
    return 0


if __name__ == "__main__":
    main()
