#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: recast

:Synopsis:
    Recast is a helper class to modify the EML object members so that
    they are more easily rendered in the Jinja2 template.
:Author:
    servilla

:Created:
    3/21/20
"""
import daiquiri
import markdown


logger = daiquiri.getLogger(__name__)


class Recast:
    def __init__(self, eml):
        self._eml = eml
        self._abstract = text_field(self._eml.abstract)
        self._contacts = responsible_party(self._eml.contact, position=True)
        self._creators = responsible_party(self._eml.creator)
        self._dataset = eml.dataset
        self._datatable = self._dataset["dataTable"]
        self._intellectual_rights = text_field(self._eml.intellectual_rights)
        self._package_id = eml.package_id
        self._title = eml.title
        self._version = eml.version

    @property
    def abstract(self):
        return self._abstract

    @property
    def data_tables(self):
        return self._datatable

    @property
    def contacts(self):
        return self._contacts

    @property
    def creators(self):
        return self._creators

    @property
    def intellectual_rights(self):
        return self._intellectual_rights

    @property
    def package_id(self):
        return self._package_id

    @property
    def title(self):
        return self._title

    @property
    def version(self):
        return self._version


def responsible_party(rp: list, position: bool = False) -> list:
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


def text_field(t: list) -> str:
    html = ""
    for _ in t:
        for key in _:
            if key == "markdown":
                md = _[key][0]["value"]
                html += markdown.markdown(md)
            if key == "value":
                html += _[key]
            if key == "para":
                html += "<p>" + text_field(_[key]) + "</p>"
            if key == "itemizedlist":
                html += "<ul>" + text_field(_[key]) + "</ul>"
            if key == "orderedlist":
                html += "<ol>" + text_field(_[key]) + "</ol>"
            if key == "listitem":
                html += "<li>" + text_field(_[key]) + "</li>"
            if key == "literalLayout":
                html += "<pre>" + text_field(_[key]) + "</pre>"
            if key == "section":
                html += "<p>" + text_field(_[key]) + "</p>"
            if key == "title":
                html += "<h4>" + text_field(_[key]) + "</h4>"
    return html


def main():
    return 0


if __name__ == "__main__":
    main()
