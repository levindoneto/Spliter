import Directory
import File
import Utils

'''
Function that manages the creation of directories and files.
@Parameter: List: tokens, Strings: File's name.
@Return: Void: It only creates a file with tokens.
'''
def manager(theFile, size):
    directoryName = Utils.getFileNameWithNoExt(theFile)
    inputText = open(theFile, "r")
    numberOfLines = File.getNumberOfLines(theFile)
    createdDirectory = Directory.createSubDir(theFile, True)
    Directory.cd(createdDirectory)
    for i in range((numberOfLines)):
        # Create subdirectories for each set of lines
        subDir = Utils.getSubDirNameWithRange(i+1, i+int(size))
        createdDirectory = Directory.createSubDir(subDir, False)
        i += int(size)
