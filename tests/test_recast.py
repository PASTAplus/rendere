#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: test_recast

:Synopsis:

:Author:
    servilla

:Created:
    3/21/20
"""
from rendere.eml import Eml
from rendere.eml import eml_factory
from rendere.recast import Recast

test_eml_file = "./data/knb-lter-nin.1.1.xml"
with open(test_eml_file, "r", encoding="utf-8") as f:
    eml_str = f.read()
eml = eml_factory(eml_str)


def test_recast_obj():
    recast_eml = Recast(eml)
    assert isinstance(recast_eml, Recast)