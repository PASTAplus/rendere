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

from rendere.eml_data_table import data_table

logger = daiquiri.getLogger(__name__)


def dataset(ds) -> dict:
    datasets = dict()
    data_tables = ds.findall("./dataTable")
    if len(data_tables) > 0:
        datasets["dataTable"] = data_table(data_tables)

    return datasets
