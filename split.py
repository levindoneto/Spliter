#!/usr/local/bin/python3

'''
Spliter

Usage:
    python split.py text.ext size

The program reads a filename (with absolute or relative path)
and a number as arguments from the commandline and splits the contents of the
file into smaller parts, also creating token-per-line output. The number
specified determines the size of the file parts in lines
'''
import sys
import Management

def main(args):
    try:
        theFile = args[1]
        size = args[2]
        Management.manager(theFile, size)
    except:
        print("\nOne or more arguments have not been provided\nUsage:")
        print("\tpython split.py text.format size")

if __name__ == '__main__':
    main(sys.argv)
