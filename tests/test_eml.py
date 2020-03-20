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
import pytest

from rendere.eml import Eml
from rendere.eml import eml_factory

test_eml_file = "./data/knb-lter-nin.1.1.xml"
with open(test_eml_file, "r", encoding="utf-8") as f:
    eml_str = f.read()
eml = eml_factory(eml_str)


def test_eml_object():
    assert isinstance(eml, Eml)


def test_package_id():
    package_id = "knb-lter-nin.1.1"
    assert eml.package_id == package_id


def test_title():
    title = (
        "Daily Water Sample Nutrient Data for North Inlet Estuary, "
        "South Carolina, from 1978 to 1992, North Inlet LTER"
    )
    assert eml.title == title


def test_version():
    version = "eml-2.1.0"
    assert eml.version == version
