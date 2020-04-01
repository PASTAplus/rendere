#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: render

:Synopsis:

:Author:
    servilla

:Created:
    3/19/20
"""
import logging
import os

import click
import daiquiri
from jinja2 import Environment, FileSystemLoader

from rendere.eml.eml import eml_factory


cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/render.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))


def render(eml_file) -> str:
    html = ""

    env = Environment(loader=FileSystemLoader(f"{cwd}/templates"))

    with open(eml_file, "r", encoding="utf-8") as f:
        eml_str = f.read()
    eml = eml_factory(eml_str)

    template = env.get_template("eml.html")
    html = template.render(eml=eml)
    return html


help_outfile = "Send rendered HTML to file"
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("eml", required=True)
@click.option("-o", "--outfile", default=None, help=help_outfile)
def main(eml: str, outfile:str):
    """
        rendere /ˈrɛndere/

        \b
        Render an EML metadata document into HTML

        \b
        EML: path to EML file to be converted
    """
    html = render(eml)
    if outfile is not None:
        with open(outfile, "w") as f:
            f.writelines(html)
    else:
        click.echo(html)
    return 0


if __name__ == "__main__":
    main()
