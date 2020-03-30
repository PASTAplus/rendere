#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: eml_data_table

:Synopsis:

:Author:
    servilla

:Created:
    3/25/20
"""
import daiquiri

from rendere.eml_methods import methods
from rendere.eml_utils import clean


logger = daiquiri.getLogger(__name__)


def data_table(tables: list) -> list:
    data_tables = list()
    for table in tables:
        t = dict()
        t["entityName"] = clean(table.find("./entityName").xpath("string()"))
        description = table.find("./entityDescription")
        if description is not None:
            t["entityDescription"] = clean(description.xpath("string("))
        physicals = table.findall(".//physical")
        if len(physicals) > 0:
            t["physical"] = physical(physicals)
        data_tables.append(t)
        m = table.find("./methods")
        if m is not None:
            methods(m)

    return data_tables


def physical(phys: list) -> list:
    physicals = list()
    for phy in phys:
        p = dict()
        p["Object Name"] = phy.find("./objectName").text.strip()
        size = phy.find("./size")
        if size is not None:
            value = clean(size.xpath("string()"))
            unit = size.attrib["unit"].strip()
            p["Size"] = f"{value} ({unit})"
        checksums = phy.findall(".//authentication")
        if len(checksums) > 0:
            for checksum in checksums:
                c = list()
                value = clean(checksum.xpath("string()"))
                method = checksum.attrib["method"].strip()
                c.append(f"{value} ({method})")
            p["Checksum(s)"] = c
        compression_methods = phy.findall(".//compressionMethod")
        if len(compression_methods) > 0:
            for compression_method in compression_methods:
                c = list()
                c.append(clean(compression_method.xpath("string()")))
            p["Compression Method"] = c
        encoding_methods = phy.findall(".//encodingMethod")
        if len(encoding_methods) > 0:
            for encoding_method in encoding_methods:
                c = list()
                c.append(clean(encoding_method.xpath("string()")))
            p["Encoding Method"] = c
        character_encoding = phy.find("./characterEncoding")
        if character_encoding is not None:
            value = clean(character_encoding.xpath("string()"))
            p["Character Encoding"] = value
        p["Data Format"] = data_format(phy.find("./dataFormat"))
        physicals.append(p)
    return physicals


# noinspection DuplicatedCode
def data_format(df) -> dict:
    d_format = dict()
    f = df.getchildren()[0]  # Can only be one child
    if f.tag == "textFormat":
        tf = dict()
        num_header_lines = f.find("./numHeaderLines")
        if num_header_lines is not None:
            tf["Header Lines"] = clean(num_header_lines.xpath("string()"))
        num_footer_lines = f.find("./numFooterLines")
        if num_footer_lines is not None:
            tf["Footer Lines"] = clean(num_footer_lines.xpath("string()"))
        record_delimiters = f.findall("./recordDelimiter")
        if record_delimiters is not None:
            rd = list()
            for record_delimiter in record_delimiters:
                rd.append(clean(record_delimiter.xpath("string()")))
            tf["Record Delimiter(s)"] = rd
        physical_line_delimiters = f.findall(".//physicalLineDelimiter")
        if len(physical_line_delimiters) > 0:
            pd = list()
            for physical_line_delimiter in physical_line_delimiters:
                pd.append(clean(physical_line_delimiter.xpath("string()")))
            tf["Physical Line Delimiter(s)"] = pd
        num_physical_lines_per_record = f.find("./numPhysicalLinesPerRecord")
        if num_physical_lines_per_record is not None:
            tf["Physical Lines Per Record"] = \
                clean(num_physical_lines_per_record.xpath("string()"))
        max_record_length = f.find("./maxRecordLength")
        if max_record_length is not None:
            tf["Maximum Record Length"] = \
                clean(max_record_length.xpath("string()"))
        attribute_orientation = f.find("./attributeOrientation")
        tf["Attribute Orientation"] = \
            clean(attribute_orientation.xpath("string()"))
        simple_delimited = f.find("./simpleDelimited")
        if simple_delimited is not None:
            td = dict()
            fd = list()
            field_delimiters = simple_delimited.findall("./fieldDelimiter")
            for field_delimiter in field_delimiters:
                fd.append(clean(field_delimiter.xpath("string()")))
            td["Field Delimiter"] = fd
            collapse_delimiters = simple_delimited.find("./collapseDelimiters")
            if collapse_delimiters is not None:
                td["Collapse Delimiters"] = \
                    clean(collapse_delimiters.xpath("string()"))
            quote_characters = simple_delimited.findall("./quoteCharacter")
            if quote_characters is not None:
                qc = list()
                for quote_character in quote_characters:
                    qc.append(clean(quote_character.xpath("string()")))
                td["Quote Character"] = qc
            literal_characters = simple_delimited.findall("./literalCharacter")
            if literal_characters is not None:
                lc = list()
                for literal_character in literal_characters:
                    lc.append(clean(literal_character.xpath("string()")))
                td["Literal Character"] = lc
        complex = f.find("./complex")
        if complex is not None:
            c = list()
            c_children = complex.getchildren()
            for c_child in c_children:
                if c_child == "textFixed":
                    tf = dict()
                    field_width = c_child.find("./fieldWidth")
                    tf["Field Width"] = clean(field_width.xpath("string()"))
                    line_number = c_child.find("./lineNumber")
                    if line_number is not None:
                        tf["Line Number"] = \
                            clean(line_number.xpath("string()"))
                    field_start_column = c_child.find("./fieldStartColumn")
                    if field_start_column is not None:
                        tf["Field Start Column"] = \
                            clean(field_start_column.xpath("string()"))
                    c.append({"textFixed": tf})
                else:  # c_child == "textDelimited"
                    td = dict()
                    field_delimiter = c_child.find("./fieldDelimiter")
                    td["Field Delimiter"] = \
                        clean(field_delimiter.xpath("string()"))
                    collapse_delimiters = \
                        c_child.find("./collapseDelimiters")
                    if collapse_delimiters is not None:
                        td["Collpase Delimiters"] = \
                            clean(collapse_delimiters.xpath("string()"))
                    line_number = c_child.find("./lineNumber")
                    if line_number is not None:
                        td["Line Number"] = clean(
                            line_number.xpath("string()"))
                    quote_characters = c_child.findall("./quoteCharacter")
                    if quote_characters is not None:
                        qc = list()
                        for quote_character in quote_characters:
                            qc.append(
                                clean(quote_character.xpath("string()")))
                        td["Quote Character"] = qc
                    literal_characters = c_child.findall("./literalCharacter")
                    if literal_characters is not None:
                        lc = list()
                        for literal_character in literal_characters:
                            lc.append(
                                clean(literal_character.xpath("string()")))
                        td["Literal Character"] = lc
                    c.append({"Text Delimited": td})
        d_format["Text"] = tf
    elif f.tag == "externallyDefinedFormat":
        edf = dict()
        format_name = f.find("./formatName")
        edf["Format Name"] = clean(format_name.xpath("string()"))
        format_version = f.find("./formatVersion")
        if format_version is not None:
            edf["Format Version"] = clean(format_version.xpath("string()"))
        d_format[{"Externally Defined"}] = edf
    else:  # f.tag == binaryRasterFormat
        brf = dict()
        row_col_orientation = f.find("./rowColumnOrientation")
        brf["Row/Column Orientation"] = \
            clean(row_col_orientation.xpath("string()"))
        multi_band = f.find("./multiBand")
        if multi_band is not None:
            nbands = multi_band.find("./nbands")
            layout = multi_band.find("./layout")
            brf["Multi-band"] = {
                "Number of bands": clean(nbands.xpath("string()")),
                "Layout": clean(layout.xpath("string()"))
            }
        num_of_bits = f.find("./nbits")
        brf["Number of bits"] = clean(num_of_bits.xpath("string()"))
        byte_order = f.find("./byteorder")
        brf["Byte Order"] = clean(byte_order.xpath("string()"))
        skip_bytes = f.find("./skipbytes")
        if skip_bytes is not None:
            brf["Skip bytes"] = clean(skip_bytes.xpath("string()"))
        band_row_bytes = f.find("./bandrowbytes")
        if band_row_bytes is not None:
            brf["Band row bytes"] = clean(band_row_bytes.xpath("string()"))
        total_row_bytes = f.find("./totalrowbytes")
        if total_row_bytes is not None:
            brf["Total row bytes"] = clean(total_row_bytes.xpath("string()"))
        band_gap_bytes = f.find("./bandgapbytes")
        if band_gap_bytes is not None:
            brf["Band-gap bytes"] = clean(band_gap_bytes.xpath("string()"))
        d_format["Binary Raster"] = brf
    return d_format
