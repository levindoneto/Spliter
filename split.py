#!/usr/local/bin/python3

'''
Splitter

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
        if (int(size) > 0):
            Management.manager(theFile, size)
        else:
            print("The size must be greater than 0")
    except:
        print("\nOne or more arguments have not been provided correctly\nUsage:")
        print("\tpython split.py text.format size")
        print("Verify if the file exists")

if __name__ == '__main__':
    main(sys.argv)
