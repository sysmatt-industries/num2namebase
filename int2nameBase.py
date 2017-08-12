#!/usr/bin/python 

from NameBaseConverter import NameBaseConverter
import sys

try:
    nameLength=int(sys.argv[2])
except: 
    nameLength=4

nameConv = NameBaseConverter(nameLength)
print "{0}".format(nameConv.encode(int(sys.argv[1])))




