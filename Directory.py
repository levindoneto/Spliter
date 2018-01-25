import Utils
import os

'''
Function that creates a subdirectory with the same path as the file given, and
creates the name for this subdirectory based on the filename provided on the
commandline, removing the ending
@Parameter: String: File's name
@Return: String: Name of the created directory (used for reference)
'''
def createSubDir(fileName):
    fileNameWithoutExtension = Utils.getFileNameWithNoExt(fileName)
    subdirectoryName = Utils.getSubDirName(fileNameWithoutExtension)
    if not (os.path.exists(subdirectoryName)):
        os.makedirs(subdirectoryName)
    return subdirectoryName

'''
Function that changes the current directory to a one passed as the parameter
@Parameter: String: Directory's name
@Return: Void: It changes the directory
'''
def cd(directoryPath):
    os.chdir(directoryPath)
