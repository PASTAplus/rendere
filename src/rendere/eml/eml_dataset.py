#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_dataset

:Synopsis:

:Author:
    servilla

:Created:
    3/26/20
"""
import daiquiri

from rendere.eml.eml_data_table import eml_data_table
from rendere.eml.eml_methods import eml_methods
from rendere.eml.eml_resource import eml_resource
from rendere.eml.eml_responsible_party import eml_responsible_party


logger = daiquiri.getLogger(__name__)


def eml_dataset(ds) -> dict:
    dataset = dict()
    dataset["Resource"] = eml_resource(ds)
    contact = ds.findall("./contact")
    dataset["Contact"] = eml_responsible_party(contact, position=True)
    methods = ds.find("./methods")
    if methods is not None:
        dataset["Methods"] = eml_methods(methods)
    data_table = ds.findall("./dataTable")
    if len(data_table) > 0:
        dataset["Data Table"] = eml_data_table(data_table)
    return dataset
