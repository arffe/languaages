#!/usr/bin/env python
# manifest check
from xml.etree import ElementTree

class cdsArray():
    def __init__(self,xx,yy):
        self.colwidth = []
        self.mainarray = []
    def printArray():
#         cdslist.append(cleanvar)
#         cleanvar = vnt.replace(".", "")
        print self.mainarray
    def addversion(version, x, y):
        mainarray.append([x],[y]) = version

    def printHeader(policylist,variantlist):
        print "header"
    def printFooter(policylist,variantlist):
        print "footer"

# variants to use
variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
# policy setttings to use
policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
# main program
myArray = cdsArray()
for vnt in variant:
    for grp in policy:
        URL = "URL&SystemID={}&SWVersion=8.4.20&policy={}.xml".format(vnt,grp)
        with open(URL, 'rt') as f:
            tree = ElementTree.parse(f)
        for node in tree.iter("version"):
            v = node.text
        myArray(v,x,y)
myArray.printHeader(policy)
myArray.printArray(variant)
myArray.printFooter()
