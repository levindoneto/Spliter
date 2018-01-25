import re

'''
Function that removes the extension of a file, regardless if it has a provided
path.
@Parameter: String: File's name with path and extension.
@Return: String: File's name with no extension.
'''
def getFileNameWithNoExt(fileName):
    return fileName.replace('/',' ').replace('.',' ').split()[-2]

'''
Function that creates a name for the subdirectory based on the file name.
@Parameter: String: File's name without extension.
@Return: Strings: Subdirectory's name.
'''
def getSubDirName(fileNameWithoutExt):
    return fileNameWithoutExt + '-data'

'''
Function that returns a name of a directory regarding the line ranging.
@Parameter: Integer: rangeBottom, Integer: rangeTop.
@Return: Strings: Subdirectory's name.
'''
def getSubDirNameWithRange(rangeBottom, rangeTop):
    return "_lines" + str(rangeBottom) + "-" + str(rangeTop)

'''
Function that returns a file's name regarding the line ranging.
@Parameter: Integer: rangeBottom, Integer: rangeTop.
@Return: Strings: File's name.
'''
def getFileNameWithRange(rangeBottom, rangeTop):
    return "_lines" + str(rangeBottom) + "-" + str(rangeTop) + ".txt"

'''
Function that returns a file's name for a tokens' file regarding the text's line.
@Parameter: Integer: line.
@Return: Strings: Tokens file's name.
'''
def getNameTokenLine(line):
    return "_line" + str(line) + ".tok"
