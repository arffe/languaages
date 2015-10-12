#!/usr/bin/env python

# manifest check

from xml.etree import ElementTree
import time

def main():
#    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
#    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]


    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]

# ADD warning re manifest and conmfiormation check 
# ADD whatist to onlycheck normal hosting

# initialise variables
    cdslen=0
    version_table=[]
# get versions
    for vnt in variant:
        verlist = []
        for grp in policy:
	    # ADD time check to throttle requests
            URL = "URL&SystemID={}&SWVersion=8.4.20&policy={}.xml".format(vnt,grp)
            with open(URL, 'rt') as f:
                tree = ElementTree.parse(f)
            # ADD error checking for no file etc
            for node in tree.iter("version"):
                print vnt, node.tag, node.text
                x = node.text
            if len(x) > cdslen:
		        cdslen = len(x)
            verlist.append(x)
            x = "-"
        version_table.append(verlist)
   
   # print table
    print "\n+----------" + ("+" + "-" * (cdslen+2)) * (len(policy)) + "+"
    print "| variant  |",
    for pol in policy:
	shortpol = pol.replace("feedbackgroup", "fbg ")
        print " {txt: ^{width}}|".format(txt=shortpol,width=cdslen),
    print  "\n+----------" + ("+" + "-" * (cdslen+2)) * (len(policy)) + "+",
    for variant_data in version_table:
	a = version_table.index(variant_data)
	cleanvar = variant[a].replace(".", "")
	print "\n| " + cleanvar + " |",
	for cds_version in variant_data:
	    print "{txt: ^{width}} |".format(txt=cds_version,width=cdslen),
    print  "\n+----------" + ("+" + "-" * (cdslen+2)) * (len(policy)) + "+\n"
      
if __name__ == "__main__":
    main();
