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
import markdown

class Recast:
    def __init__(self, eml):
        self._eml = eml
        self._abstract = self._abstract()
        self._creators = self._creators()
        self._package_id = eml.package_id
        self._title = eml.title
        self._version = eml.version

    def _abstract(self):
        return text_field(self._eml.abstract)

    def _creators(self):
        creators = list()

        for creator in self._eml.creators:
            organizations = ", ".join(creator["organization_names"])
            individuals = creator["individual_names"]
            for individual in individuals:
                sur_name = individual["sur_name"]
                given_names = " ".join(individual["given_names"])
                creators.append(f"{sur_name}, {given_names} ({organizations})")

        for creator in self._eml.creators:
            if len(creator["individual_names"]) == 0:
                for organization in creator["organization_names"]:
                    creators.append(organization)

        return creators

    @property
    def abstract(self):
        return self._abstract

    @property
    def creators(self):
        return self._creators

    @property
    def package_id(self):
        return self._package_id

    @property
    def title(self):
        return self._title

    @property
    def version(self):
        return self._version


def text_field(t):
    html = ""
    for _ in t:
        for key in _:
            if key == "markdown":
                html += markdown.markdown(_[key])
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
    return html


def main():
    return 0


if __name__ == "__main__":
    main()
