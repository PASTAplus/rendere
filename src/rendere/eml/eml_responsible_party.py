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
import daiquiri

from rendere.eml.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def eml_responsible_party(parties: list, position: bool) -> list:
    # list of element_objs
    responsible_party = list()
    for party in parties:
        individual_names = list()
        organization_names = list()
        position_names = list()
        _individual_names = party.findall("./individualName")
        for _individual_name in _individual_names:
            given_names = list()
            _given_names = _individual_name.findall("./givenName")
            for _given_name in _given_names:
                given_name = (clean(_given_name.xpath("string()"))).strip()
                given_names.append(given_name)
            _sur_name = _individual_name.find("./surName")
            sur_name = (clean(_sur_name.xpath("string()"))).strip()
            individual_name = {"sur_name": sur_name, "given_names": given_names}
            individual_names.append(individual_name)
        _organization_names = party.findall("./organizationName")
        for _organization_name in _organization_names:
            organization_name = (
                clean(_organization_name.xpath("string()"))).strip()
            organization_names.append(organization_name)
        _position_names = party.findall("./positionName")
        for _position_name in _position_names:
            position_name = (clean(_position_name.xpath("string()")))
            position_names.append(position_name)
        party_grp = {"individual_names": individual_names,
                     "organization_names": organization_names,
                     "position_names": position_names}
        responsible_party.append(party_grp)

        processed = process_responsible_party(responsible_party, position)

    return processed


def process_responsible_party(rp: list, position: bool) -> list:
    rps = list()
    for p in rp:
        organizations = ", ".join(p["organization_names"])
        individuals = p["individual_names"]
        for individual in individuals:
            sur_name = individual["sur_name"]
            given_names = " ".join(individual["given_names"])
            if len(organizations) > 0:
                rps.append(f"{sur_name}, {given_names} ({organizations})")
            else:
                rps.append(f"{sur_name}, {given_names}")

    if position:
        for p in rp:
            if len(p["individual_names"]) == 0:
                organizations = ", ".join(p["organization_names"])
                positions = p["position_names"]
                for position in positions:
                    if len(organizations) > 0:
                        rps.append(f"{position} ({organizations})")
                    else:
                        rps.append(f"{position}")
        for p in rp:
            if len(p["individual_names"]) == 0 and len(
                    p["position_names"]) == 0:
                for organization in p["organization_names"]:
                    rps.append(organization)
    else:
        for p in rp:
            if len(p["individual_names"]) == 0:
                for organization in p["organization_names"]:
                    rps.append(organization)

    return rps
