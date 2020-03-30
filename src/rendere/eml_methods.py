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


def methods(m) -> dict:
    children = m.getchildren()
    for child in children:
        print(f"{child.tag}")