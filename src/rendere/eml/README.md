### Rendere EML package

The Rendere EML package converts EML XML into an EML presentation model that
can be rendered more easily to HTML. Modules within this package are modeled
closely on the corresponding EML hierarchy, but not necessarily one-to-one.

Input parameters to each module function is either an *lxml etree* element
object or a list of element objects. Function return values are either a
dictionary or a list of dictionaries (in most cases). Dictionary keys tend to
be the more human readable form of EML XML element tag names: this facilitates
their display when iterating through long lists of items. For example, in the
case of the EML XML element `objectName`, the corresponding model key is set
to `Object Name`:

  ```p["Object Name"] = phy.find("./objectName").text.strip()```
  
The `Object Name` dictionary key contains the object name of the entity being
described as a simple unicode text value. 