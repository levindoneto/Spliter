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
    ListOfLinesStr = inputText.readlines()
    d = 0
    for i in range(d, numberOfLines, int(size)):
        # Create subdirectories for each set of lines
        subDir = Utils.getSubDirNameWithRange(d+1, d+int(size))
        createdDirectory = Directory.createSubDir(subDir, False)
        Directory.cd(createdDirectory)
        File.createPartsFile(
            theFile,
            Utils.getFileNameWithRange(d + 1, d + int(size))
            ,d + 1,
            d + int(size)
        )
        for j in range(d, d + int(size), 1):
                if (d < numberOfLines):
                    File.createTokensFile(
                        Utils.getTokens(ListOfLinesStr[d]),
                        Utils.getNameTokenLine(d+1)
                    )
                d += 1
        Directory.cd('../') # In order to fill another subdirectory
