#!/usr/bin/env python

# # lynda.com - Up and Running with Python
# examples of accessing URLs

import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("samplexml.xml");
    print doc.nodeName
    print doc.firstChild.tagName

    versions = doc.getElementsByTagName("version")
    print "{} versions:".format(versions.length)
    for version in versions:
        print version.getAttribute("version")

if __name__ == "__main__":
    main();
