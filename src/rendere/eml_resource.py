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

from rendere.eml_responsible_party import responsible_party
from rendere.eml_text_field import text_field
from rendere.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def resource_group(module) -> dict:
    resource = dict()

    resource["title"] = clean(module.find("./title").xpath("string()"))
    resource["creator"] = responsible_party(module.findall("./creator"))

    alternate_identifiers = module.findall("./alternateIdentifier")
    _ = list()
    for alternate_identifier in alternate_identifiers:
        _.append(clean(alternate_identifier.xpath("string()")))
    resource["alternateIdentifier"] = _

    abstract = module.find("./abstract")
    if abstract is not None:
        resource["abstract"] = text_field(abstract)

    intellectual_rights = module.find("./intellectualRights")
    if intellectual_rights is not None:
        resource["intellectualRights"] = text_field(intellectual_rights)

    return resource


