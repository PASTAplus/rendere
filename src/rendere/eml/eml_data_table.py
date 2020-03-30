#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_data_table

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri

from rendere.eml.eml_methods import eml_methods
from rendere.eml.eml_physical import eml_physical
from rendere.eml.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def eml_data_table(tables: list) -> list:
    data_table = list()
    for table in tables:
        t = dict()
        t["Entity Name"] = clean(table.find("./entityName").xpath("string()"))
        description = table.find("./entityDescription")
        if description is not None:
            t["Entity Description"] = clean(description.xpath("string("))
        physical = table.findall(".//physical")
        if len(physical) > 0:
            t["Physical"] = eml_physical(physical)
        data_table.append(t)
        methods = table.find("./methods")
        if methods is not None:
            t["Methods"] = eml_methods(methods)
    return data_table
