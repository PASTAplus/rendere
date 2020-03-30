#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_text

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri
import markdown

logger = daiquiri.getLogger(__name__)


def eml_text(element_obj) -> list:
    text_list = list()
    if element_obj.text is not None:
        if element_obj.tag == "markdown":
            text = process_markdown(element_obj.text)
            text_list.append({"value": text})
        else:
            text_list.append({"value": element_obj.text})
    for _ in element_obj:
        text_list.append({_.tag: eml_text(_)})
    if element_obj.tail is not None:
        text_list.append({"value": element_obj.tail})
    return text_list


def leftshift_markdown(md):
    lines = md.split("\n")
    line_no = 0
    for line in lines:
        if len(line.strip()) > 0:
            break
        else:
            line_no += 1
    col_diff = len(lines[line_no]) - len(lines[line_no].lstrip())
    line_no = 0
    for line in lines:
        lines[line_no] = line[col_diff:]
        line_no += 1
    text = "\n".join(lines)
    return text


def process_markdown(md):
    text = leftshift_markdown(md)
    return text


def html_text(t: list) -> str:
    html = ""
    for _ in t:
        for key in _:
            if key == "markdown":
                md = _[key][0]["value"]
                html += markdown.markdown(md)
            if key == "value":
                html += _[key]
            if key == "para":
                html += "<p>" + html_text(_[key]) + "</p>"
            if key == "itemizedlist":
                html += "<ul>" + html_text(_[key]) + "</ul>"
            if key == "orderedlist":
                html += "<ol>" + html_text(_[key]) + "</ol>"
            if key == "listitem":
                html += "<li>" + html_text(_[key]) + "</li>"
            if key == "literalLayout":
                html += "<pre>" + html_text(_[key]) + "</pre>"
            if key == "section":
                html += "<p>" + html_text(_[key]) + "</p>"
            if key == "title":
                html += "<h4>" + html_text(_[key]) + "</h4>"
    return html
