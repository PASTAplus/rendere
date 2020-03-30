#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_methodsd

:Synopsis:

:Author:
    servilla

:Created:
    3/29/20
"""
import daiquiri

logger = daiquiri.getLogger(__name__)


def eml_methods(element_obj) -> list:
    methods = list()
    children = element_obj.getchildren()
    for child in children:
        if child.tag == "methodStep":
            methods.append({"Method Step": "method step"})
        elif child.tag == "sampling":
            methods.append({"Sampling": "sampling"})
        else:  # child.tag == "qualityControl"
            methods.append({"Quality Control": "quality control"})
    return methods
