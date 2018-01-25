import Utils
import os

'''
Function that creates a subdirectory with the same path as the file given, and
creates the name for this subdirectory based on the filename provided on the
commandline, removing the ending
@Parameter: String: File's name
@Return: Void: It only creates a directory
'''
def createSubDir(fileName):
    fileNameWithoutExtension = Utils.getFileNameWithNoExt(fileName)
    subdirectoryName = Utils.getSubDirName(fileNameWithoutExtension)
    if not (os.path.exists(subdirectoryName)):
        os.makedirs(subdirectoryName)
