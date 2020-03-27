#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_utils

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri


logger = daiquiri.getLogger(__name__)


def clean(text):
    return " ".join(text.split())
