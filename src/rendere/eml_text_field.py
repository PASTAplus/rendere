#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_text_field

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri

logger = daiquiri.getLogger(__name__)


def leftshift_markdown(md):
    lines = md.text.split("\n")
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


def text_field(t):
    text_list = list()
    if t.text is not None:
        if t.tag == "markdown":
            text = process_markdown(t)
            text_list.append({"value": text})
        else:
            text_list.append({"value": t.text})
    for _ in t:
        text_list.append({_.tag: text_field(_)})
    if t.tail is not None:
        text_list.append({"value": t.tail})
    return text_list
