#!/usr/bin/env python

# manifest check

from xml.etree import ElementTree

def main():
    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
    print " "
    print "+----------+----------+----------+----------+----------+----------+----------+"
    print "| variant  |  normal  |    fbg   |   fbg 2  |   fbg 3  |   fbg 4  |   fbg 5  |"
    print "+----------+----------+----------+----------+----------+----------+----------+"
    for vnt in variant:
        cdslist = []
        cleanvar = vnt.replace(".", "")
        cdslist.append(cleanvar)
        for grp in policy:
            URL = "URL&SystemID={}&SWVersion=8.4.20&policy={}.xml".format(vnt,grp)
            with open(URL, 'rt') as f:
                tree = ElementTree.parse(f)
            for node in tree.iter("version"):
                x = node.text
            cdslist.append(x)
        print '|', ' | '.join([str(item) for item in cdslist]), '|'
    print "+----------+----------+----------+----------+----------+----------+----------+"
    print " "

if __name__ == "__main__":
    main();
