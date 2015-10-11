#!/usr/bin/env python

# manifest check

from xml.etree import ElementTree

def main():
    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
    for vnt in variant:
        print "+----------+----------------+----------+"
        for grp in policy:
            URL = "URL&SystemID={}&SWVersion=8.4.20&policy={}.xml".format(vnt,grp)
            with open(URL, 'rt') as f:
                tree = ElementTree.parse(f)
            for node in tree.iter("version"):
                x = node.text
                cleanvar = vnt.replace(".", "")
                print "|{:^10}| {:<15}|{:^10}|".format(cleanvar,grp,x)
if __name__ == "__main__":
    main();
