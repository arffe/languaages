#!/usr/bin/env python

# XML parsing

from xml.etree import ElementTree


def main():
    with open('samplexml.xml', 'rt') as f:
        tree = ElementTree.parse(f)


    for node in tree.iter("version"):
        x = node.text
        print x
#        name = node.attrib.get('text')
#        print name

if __name__ == "__main__":
    main();
