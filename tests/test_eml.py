#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: test_eml_parsing

:Synopsis:

:Author:
    servilla

:Created:
    1/21/20
"""
from lxml import etree
import pytest
from rendere.eml import Eml
from rendere.eml import eml_factory
import rendere.eml_responsible_party as eml_creator
import rendere.eml_resource as eml_resource

test_eml_file = "./data/knb-lter-nin.1.1.xml"
with open(test_eml_file, "r", encoding="utf-8") as f:
    eml_str = f.read()


def test_creator():
    root = etree.fromstring(eml_str.encode("utf-8"))
    dataset = root.find(".//dataset")
    dataset_creators = dataset.findall(".//creator")
    creators = eml_creator.creator(dataset_creators)
    number_creators = len(creators)
    assert number_creators == 3


def test_eml_object():
    eml = eml_factory(eml_str)
    assert isinstance(eml, Eml)


def test_resource():
    root = etree.fromstring(eml_str.encode("utf-8"))
    dataset = root.find(".//dataset")
    resource = eml_resource.resource_group(dataset)
    assert isinstance(resource, dict)


