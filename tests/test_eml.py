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

test_eml_file = "./data/test_eml.1.1.xml"


def test_eml_object():
    eml = eml_factory(test_eml_file)
    assert isinstance(eml, Eml)
