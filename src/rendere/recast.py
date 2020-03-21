#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: recast

:Synopsis:

:Author:
    servilla

:Created:
    3/21/20
"""


class Recast:
    def __init__(self, eml):
        self._eml = eml
        self._abstract = eml.abstract
        self._creators = self._creators()
        self._package_id = eml.package_id
        self._title = eml.title
        self._version = eml.version

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


def main():
    return 0


if __name__ == "__main__":
    main()
