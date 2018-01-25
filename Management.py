import Directory
import File
import Utils

'''
Function that manages the creation of directories and files.
@Parameter: List: tokens, Strings: File's name.
@Return: Void: It only creates a file with tokens.
'''
def manager(theFile, size):
    inputText = open(theFile, "r")
    numberOfLines = File.getNumberOfLines(theFile)
    print('number of lines: ', numberOfLines)
    createdDirectory = Directory.createSubDir(theFile)
    Directory.cd(createdDirectory)
    #for i in range(len())
