#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="This is Christian's verison of your script")

#================== Add arguments=============================================

#This is how we input an integer of ports
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=0, type=int, required=False, help='<required> Enter a simple Integer')

#This is how we input a float
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=0.0, type=float, required=False, help='Enter a simple Float')

#This is how we input a string
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='None', type=str, required=False, help='Enter a simple String')

#This is just passing a list to the argument (space delimited set of strings)
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')

#================ Using the parser =========================================

args = parser.parse_args()

#This is used to check if no arguments were passed.
#If not print the -h (usage instructions)
if len(sys.argv) == 1:
    print(parser.print_help())
    exit(0)
   
print("The value of your '-i' arg is: " + str(args.varInteger))
print("The value of your '-d' arg is: " + str(args.varFloat))
print("The value of your '-s' arg is: " + str(args.varString))

print("--- Here is the List ---")
print(args.varList)
for arg in args.varList:
    print(arg)
