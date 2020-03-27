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

from rendere.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def data_table(tables: list) -> list:
    data_tables = list()
    for table in tables:
        t = dict()
        t["entityName"] = clean(table.find("./entityName").xpath("string()"))
        description = table.find("./entityDescription")
        if description is not None:
            t["entityDescription"] = clean(description.xpath("string("))
        physicals = table.findall("./physical")
        if len(physicals) > 0:
            t["physical"] = physical(physicals)
        data_tables.append(t)

    return data_tables


def physical(phys: list) -> list:
    physicals = list()
    for phy in phys:
        p = dict()
        p["objectName"] = phy.find("./objectName").text.strip()
        size = phy.find("./size")
        if size is not None:
            value = clean(size.xpath("string()"))
            unit = size.attrib["unit"].strip()
            p["size"] = f"{value} ({unit})"
        checksums = phy.findall("./authentication")
        if len(checksums) > 0:
            for checksum in checksums:
                c = list()
                value = clean(checksum.xpath("string()"))
                method = checksum.attrib["method"].strip()
                c.append(f"{value} ({method})")
            p["authentication"] = c
        physicals.append(p)
    return physicals
