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
argsParser.add_argument("-b", "--bits", help="Specify number of bits in password to be generated, default={}".format(defaultBits), type=int, default=defaultBits)
argsParser.add_argument("-n", "--names", help="Specify name set to use by letter count, default={}".format(defaultNameSet), type=int, default=defaultNameSet, choices=[3,4,5])
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
        print "     args.bits[{}]".format(args.bits)
        print "    args.names[{}]".format(args.names)
        print "       myDelim[{}]".format(myDelim)
        print "        myCase[{}]".format(myCase)
        print "passwdBitsFrom[{}]".format(passwdBitsFrom)
        print "  passwdBitsTo[{}]".format(passwdBitsTo)
        print "     myRandInt[{}]".format(myRandInt)

    nameConv = NameBaseConverter(args.names,delim=myDelim)
    nameOut = nameConv.encode(myRandInt)
    if myCase == "upper":
        nameOut=nameOut.upper()
    elif myCase == "lower":
        nameOut=nameOut.lower()
    elif myCase == "title":
        nameOut=nameOut.title()
    print "{0}".format(nameOut)




