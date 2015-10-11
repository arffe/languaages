#!/usr/bin/env python

# manifest check

from xml.etree import ElementTree
import time, urllib2, sys

def main():
#    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
#    policy=["normal","feedbackgroup","feedbackgroup2","feedbackgroup3","feedbackgroup4","feedbackgroup5"]
    policy=["normal"]       

#    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
#    variant=["80B0.7000","84B0.7000","80B0.8500","84B0.8500","86B0.8500","87B0.8500"]
    variant=["80B0.7000"]

# ADD warning re manifest and user confirmation check 
# ADD swithc to onlycheck normal hosting

# initialise variables
    cdslen=6
    version_table=[]
# get versions
    for vnt in variant:
        version_list = []
        for grp in policy:
	    # consider adding time check to throttle requests **but run time is several seconds **
	    # consider adding user agent info to identifyscript

            
            #url = "http://www.humaxtvportal.com/SWUpdate/CheckNewSW?SystemID={}Version=8.4.20&policy={}".format(vnt,grp) 
            url = "http://52.25.101.195/URL{}policy{}.xml".format(vnt,grp) 

            try: getxml = urllib2.urlopen(url)
            except urllib2.HTTPError as e:
                err_string = "HTTP " + str(e.code)
                version_list.append(err_string)
                if cdslen < 9:
                    cdslen = 9
                continue
            except urllib2.URLError as e:
                version_list.append("URL error")
                if cdslen < 9:
                    cdslen = 9
                continue
            except urllib2.HTTPException as e:
                version_list.append("HTTP exc")
                if cdslen < 8:
                    cdslen = 8
                continue
            if (getxml.getcode() != 200):
                version_list.append("not found")
                if cdslen < 9:
                    cdslen = 9
            else:
                tree = ElementTree.parse(getxml)
                for node in tree.iter("version"):
                    cdsversion = node.text
                if len(node.text) > cdslen:
		            cdslen = len(node.text)
                version_list.append(node.text)
        version_table.append(version_list)
  
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