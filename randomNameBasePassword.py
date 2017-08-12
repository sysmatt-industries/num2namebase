#!/usr/bin/python 

from NameBaseConverter import NameBaseConverter
import sys
import random
import argparse

defaultBits=40
defaultNameSet=4
defaultDelim="-" 
defaultCase="upper"

argsParser=argparse.ArgumentParser()
argsParser.add_argument("-v", "--verbose", help="Enable Verbose Messages", action="store_true")
argsParser.add_argument("-c", "--case", help="Enable name case randomization", action="store_true")
argsParser.add_argument("-d", "--delim", help="Enable delimiter randomization", action="store_true")
argsParser.add_argument("-b", "--bits", help="Specify number of bits in password to be generated, default={0}".format(defaultBits), type=int, default=defaultBits)
argsParser.add_argument("-n", "--names", help="Specify name set to use by letter count, default={0}".format(defaultNameSet), type=int, default=defaultNameSet, choices=[3,4,5])
argsParser.add_argument("-q", "--quantity", help="Specify quantity of passwords to generate, default=1", type=int, default=1)
args=argsParser.parse_args()


rando = random.SystemRandom()

for q in range(0,args.quantity):
    passwdBitsFrom=2**args.bits
    passwdBitsTo=(2**(args.bits+1))-1
    myRandInt = rando.randint(passwdBitsFrom,passwdBitsTo)
    myDelim=defaultDelim
    if args.delim:
        myDelim=rando.choice("-_^:,.?$%+=;")
    myCase=defaultCase
    if args.case:
        myCase=rando.choice(tuple("upper lower title".split(" ")))
    if args.verbose:
        print "     args.bits[{0}]".format(args.bits)
        print "    args.names[{0}]".format(args.names)
        print "       myDelim[{0}]".format(myDelim)
        print "        myCase[{0}]".format(myCase)
        print "passwdBitsFrom[{0}]".format(passwdBitsFrom)
        print "  passwdBitsTo[{0}]".format(passwdBitsTo)
        print "     myRandInt[{0}]".format(myRandInt)

    nameConv = NameBaseConverter(args.names,delim=myDelim)
    nameOut = nameConv.encode(myRandInt)
    if myCase == "upper":
        nameOut=nameOut.upper()
    elif myCase == "lower":
        nameOut=nameOut.lower()
    elif myCase == "title":
        nameOut=nameOut.title()
    print "{0}".format(nameOut)




