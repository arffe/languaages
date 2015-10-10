#!/usr/bin/env python

# # lynda.com - Up and Running with Python
# examples of accessing URLs

import xml.dom.minidom
def main():
    doc1 = xml.dom.minidom.parse("samplexml.xml");
#    print "node = ", doc.nodeName

#    print "tag = ", doc.firstChild.tagName
#    versions = doc.getElementsByTagName("version")
#    print "{} versions:".format(versions.length)
#    for i in versions:
#        print "attrib =  ", i.getAttribute("i")
#
    for node in doc1.getElementsByTagName('version'):  # visit every node <bar />
        print "version tag = ", node.toxml()


if __name__ == "__main__":
    main();
