#!/usr/bin/env python

# manifest check

from xml.etree import ElementTree

def main():
    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
    
    printpol = []
    cdslen=8
    for v in policy:
	printpol.append(v.replace("feedbackgroup", "fbg "))
    print "\n"
    print "+----------" * (len(policy) + 1) + "+"
    print "| variant ",
    for y in printpol:
        print "| {txt: ^{width}}".format(txt=y,width=cdslen), 
    print "|"
    print "+----------" * (len(policy) + 1) + "+"
    for vnt in variant:
        cdslist = []
        cleanvar = vnt.replace(".", "")
        #cdslist.append(cleanvar)
        for grp in policy:
            URL = "URL&SystemID={}&SWVersion=8.4.20&policy={}.xml".format(vnt,grp)
            with open(URL, 'rt') as f:
                tree = ElementTree.parse(f)
            for node in tree.iter("version"):
                x = node.text
            cdslist.append(x)
        print "| {}".format(cleanvar),
	for p in cdslist:
	    print "| {txt: ^{width}}".format(txt=p,width=cdslen),
	print "|"
    print "+----------" * (len(policy) + 1) + "+"
    print " "

if __name__ == "__main__":
    main();
