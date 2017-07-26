#!/usr/bin/python 

from NameBaseConverter import NameBaseConverter
import sys

nameConv = NameBaseConverter()
print "{0}".format(nameConv.encode(int(sys.argv[1])))




