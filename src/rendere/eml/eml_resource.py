#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_resource

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri

from rendere.eml.eml_responsible_party import eml_responsible_party
from rendere.eml.eml_text import eml_text, html_text
from rendere.eml.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def eml_resource(element_obj) -> dict:
    resource = dict()

    resource["Title"] = clean(element_obj.find("./title").xpath("string()"))
    creator = element_obj.findall("./creator")
    resource["Creator"] = eml_responsible_party(creator, position=False)

    alternate_identifiers = element_obj.findall("./alternateIdentifier")
    alt_id = list()
    for alternate_identifier in alternate_identifiers:
        alt_id.append(clean(alternate_identifier.xpath("string()")))
    resource["Alternate Identifier"] = alt_id

    abstract = element_obj.find("./abstract")
    if abstract is not None:
        resource["Abstract"] = html_text(eml_text(abstract))

    intellectual_rights = element_obj.find("./intellectualRights")
    if intellectual_rights is not None:
        resource["Intellectual Rights"] = \
            html_text(eml_text(intellectual_rights))

    return resource


