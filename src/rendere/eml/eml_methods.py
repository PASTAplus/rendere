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

from rendere.eml.eml_text import eml_text, html_text
from rendere.eml.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def eml_methods(element_obj) -> list:
    methods = list()
    children = element_obj.getchildren()
    for child in children:
        if child.tag == "methodStep":
            methods.append({"Method Step": eml_method_step(child)})
        elif child.tag == "sampling":
            methods.append({"Sampling": "sampling"})
        else:  # child.tag == "qualityControl"
            methods.append({"Quality Control": "quality control"})
    return methods


def eml_method_step(element_obj) -> dict:
    method_step = dict()
    description = element_obj.find("./description")
    method_step["Description"] = html_text(eml_text(description))
    instrumentation = element_obj.findall("./instrumentation")
    if len(instrumentation) > 0:
        i = list()
        for instrument in instrumentation:
            i.append(clean(instrument.xpath("string()")))
        method_step["Instrumentation"] = i
    substep = element_obj.findall("./subStep")
    if len(substep) > 0:
        s = list()
        for step in substep:
            s.append(eml_method_step(step))
        method_step["Sub Step(s)"] = s
    return method_step
