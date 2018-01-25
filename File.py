from itertools import islice

'''
Function that creates a file with tokens.
@Parameter: List: tokens, Strings: File's name.
@Return: Void: It only creates a file with tokens.
'''
def createTokensFile(tokens, filename):
    tokenFile = open(filename, "w+")
    for i in range(len(tokens)):
        tokenFile.write(tokens[i] + '\n')
    tokenFile.close()

'''
Function that creates a file with the parts of the text
@Parameter: String: path/name of the input file,
            String: name of the output file,
            Integer: range bottom, Integer: range top
@Return: Void: It only creates a file with tokens
'''
def createPartsFile(textFileName, partsFileName, rangeBottom, rangeTop):
    outputFile = open(partsFileName, "w+")
    with open('../../' + textFileName) as inputFile:
        head = list(islice(inputFile, rangeBottom, rangeTop))
    for i in range(len(head)):
        outputFile.write(head[i])

'''
Function that returns the number of lines of a file
@Parameter: String: file (it might contain the pat)
@Return: Integer: Number of lines
'''
def getNumberOfLines(theFile):
    return sum(1 for line in open(theFile))
