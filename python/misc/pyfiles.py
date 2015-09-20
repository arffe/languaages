#!/usr/bin/env python
#python - file access
# lynda.com - Up and Running with Python

import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():

   if path.exists("textfile.txt.bak"): 
      src=path.realpath("textfile.txt.bak")
      with ZipFile("testzip.zip", "w") as newzip:
          newzip.write("newfile.txt")
          newzip.write("textfile.txt.bak")
          
if __name__ == "__main__":
    main()

'''
      root_dir,tail = path.split(src)
      shutil.make_archive("archive", "zip", root_dir)
    
    os.rename("textfile.txt", "newfile.txt")

   if path.exists("textfile.txt"): 
       src=path.realpath("textfile.txt")
       head, tail = path.split(src)
       print "path: " + head
       print "file: "+ tail
       dst = src + ".bak"
       shutil.copystat(src,dst)

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

    text = "textfile.txt"
    t = time.ctime(path.getmtime(text))
    print t
    print datetime.datetime.fromtimestamp(path.getmtime(text))
    
    text = "textfile.txt"
    print "Item's path: " + str(path.realpath(text))
    print "Item's path and name:  " + str(path.split(path.realpath(text)))
    
    print os.name
    text = "textfile.txt"
    print "Item exists: " + str(path.exists(text))
    print "Item is a file:  " + str(path.isfile(text))
    print "Item is a directory: " + str(path.isdir(text))
    
    f = open("textfile.txt","r")
    #if f.mode == 'r':
        #contents = f.read()
    fl = f.readlines()
    for x in fl:
        print x
    f.close()
    #print contents

f = open("textfile.txt","a+")
    for i in range(10):
        #f.write("this is line %d\r\n" % (i+1))
    f.close()
'''
