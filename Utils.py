import re

'''
Function that removes the extension of a file, regardless if it has a provided
path
@Parameter: String: File's name with path and extension
@Return: String: File's name with no extension
'''
def getFileNameWithNoExt(fileName):
    return fileName.replace('/',' ').replace('.',' ').split()[-2]

'''
Function that creates a name for the subdirectory based on the file name
@Parameter: String: File's name without extension
@Return: Strings: Subdirectory's name
'''
def getSubDirName(fileNameWithoutExt):
    print("Get sub dir name")
