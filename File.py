'''
Function that creates a file with tokens
@Parameter: List: tokens, Strings: File's name
@Return: Void: It only creates a file with tokens
'''
def createTokensFile(tokens, filename):
    tokenFile = open(filename, "w+")
    for i in range(len(tokens)):
        tokenFile.write(tokens[i] + '\n')
    tokenFile.close()

'''
Function that creates a file with the parts of the text
@Parameter: List: parts of the file, Strings: File's name
@Return: Void: It only creates a file with tokens
'''
def createPartsFile(parts, filename):
    print("Create parts' file")
