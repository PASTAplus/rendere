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


class Eml:
    def __init__(self, eml_root):
        self._eml_root = eml_root
        self._abstract = self._get_abstract()
        self._creators = self._get_creators()
        self._package_id = (self._eml_root.attrib["packageId"]).strip()
        self._title = self._get_title()
        self._version = ((self._eml_root.nsmap["eml"]).split("/"))[-1]

    def _get_abstract(self):
        abstract = ""
        _ = self._eml_root.find(".//abstract")
        if _ is not None:
            abstract = clean(_.xpath("string()"))
        return abstract

    def _get_creators(self):
        creators = list()
        _creators = self._eml_root.findall(".//dataset/creator")
        for _creator in _creators:
            individual_names = list()
            organization_names = list()
            position_names = list()
            _individual_names = _creator.findall(".//individualName")
            for _individual_name in _individual_names:
                given_names = list()
                _given_names = _individual_name.findall(".//givenName")
                for _given_name in _given_names:
                    given_name = (clean(_given_name.xpath("string()"))).strip()
                    given_names.append(given_name)
                _sur_name = _individual_name.find(".//surName")
                sur_name = (clean(_sur_name.xpath("string()"))).strip()
                individual_name = {"sur_name": sur_name,
                                   "given_names": given_names}
                individual_names.append(individual_name)
            _organization_names = _creator.findall(".//organizationName")
            for _organization_name in _organization_names:
                organization_name = (
                    clean(_organization_name.xpath("string()"))).strip()
                organization_names.append(organization_name)
            _position_names = _creator.findall(".//positionName")
            for _position_name in _position_names:
                position_name = (clean(_position_name.xpath("string()")))
                position_names.append(position_name)
            creator = {"individual_names": individual_names,
                       "organization_names": organization_names,
                       "position_names": position_names}
            creators.append(creator)
        return creators

    def _get_title(self):
        title = ""
        _ = self._eml_root.find(".//title")
        if _ is not None:
            title = clean(_.xpath("string()"))
        return title

    @property
    def abstract(self):
        return self._abstract

    @property
    def creators(self):
        return self._creators

    @property
    def package_id(self):
        return self._package_id

    @property
    def title(self):
        return self._title

    @property
    def version(self):
        return self._version


class Eml210(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


class Eml211(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


class Eml220(Eml):
    def __init__(self, eml_root):
        super().__init__(eml_root)


versions = {
        "eml://ecoinformatics.org/eml-2.1.0": Eml210,
        "eml://ecoinformatics.org/eml-2.1.1": Eml211,
        "https://eml.ecoinformatics.org/eml-2.2.0": Eml220,
}


def clean(text):
    return " ".join(text.split())


def eml_factory(eml_str: str):
    """
    Returns the EML object for the specified version of EML
    :param eml_str: EML XML string
    :return: EML object
    """
    eml = eml_str.encode("utf-8")
    eml_root = etree.fromstring(eml)
    return versions[eml_root.nsmap["eml"]](eml_root)


def main():
    return 0


if __name__ == "__main__":
    main()
