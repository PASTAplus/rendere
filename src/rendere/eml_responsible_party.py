#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_responsible_party

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import logging
import os

import daiquiri
from lxml import etree

from rendere.eml_utils import clean


cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/eml_responsible_party.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))


def responsible_party(parties:list) -> list:
    responsible_parties = list()
    for party in parties:
        individual_names = list()
        organization_names = list()
        position_names = list()
        _individual_names = party.findall(".//individualName")
        for _individual_name in _individual_names:
            given_names = list()
            _given_names = _individual_name.findall(".//givenName")
            for _given_name in _given_names:
                given_name = (clean(_given_name.xpath("string()"))).strip()
                given_names.append(given_name)
            _sur_name = _individual_name.find(".//surName")
            sur_name = (clean(_sur_name.xpath("string()"))).strip()
            individual_name = {"sur_name": sur_name, "given_names": given_names}
            individual_names.append(individual_name)
        _organization_names = party.findall(".//organizationName")
        for _organization_name in _organization_names:
            organization_name = (
                clean(_organization_name.xpath("string()"))).strip()
            organization_names.append(organization_name)
        _position_names = party.findall(".//positionName")
        for _position_name in _position_names:
            position_name = (clean(_position_name.xpath("string()")))
            position_names.append(position_name)
        party_grp = {"individual_names": individual_names,
                     "organization_names": organization_names,
                     "position_names": position_names}
        responsible_parties.append(party_grp)
    return responsible_parties
