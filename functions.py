from random import shuffle
import webbrowser

normalChars = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

# This function sets and changes the key in .csv format.

def setKey():
    
    defaultEncodedChars = list(normalChars)
    shuffle(defaultEncodedChars)
    
    encryptionKeyFile = open("defaultEncodedChars.csv", "w")
    encryptionKeyFile.write("".join(defaultEncodedChars))
    encryptionKeyFile.close()
    

try:
    encodedLetterSequence = open("defaultEncodedChars.csv", "r")
    
except FileNotFoundError:
    setKey()
    encodedLetterSequence = open("defaultEncodedChars.csv", "r")

defaultEncodedChars =  tuple(encodedLetterSequence.read())
encodedLetterSequence.close()

# This function assures that if the key was changed after some file was encoded the file could still be decoded.
        
def keyWrite(fileToWriteKey):

    setEncodedChars = []
    
    for i in defaultEncodedChars:
        setEncodedChars.append(i + "%#$&")

    fileToWriteKey = open(fileToWriteKey, "a")
    fileToWriteKey.writelines("\n" + "".join(setEncodedChars))
    fileToWriteKey.close()


def keyRead(fileToReadKey):
    
    fileToReadKey = open(fileToReadKey, "r")
    setEncodedChars = fileToReadKey.readlines()[-1]
    defaultEncodedChars = []
    
    if "%#$&" in setEncodedChars:
        for i in setEncodedChars.split("%#$&"):
            defaultEncodedChars.append(i)
        return tuple(defaultEncodedChars)
    
    else:
        encodedLetterSequence = open("defaultEncodedChars.csv", "r")
        defaultEncodedChars = tuple(encodedLetterSequence.read())
        encodedLetterSequence.close()
        return defaultEncodedChars
    
    
# This function takes a file/file path and encodes it.

def encrypt(filePathToEncode):

    pathValidity = True
    
    try:
        fileToEncode = open(filePathToEncode, "r")
    except FileNotFoundError:
        pathValidity = False
    
    if pathValidity == True:
        
        textToEncode = fileToEncode.readlines()
        fileToEncode.close()
        
        if "#$#$#&#&@&@^%&^%" not in "".join(textToEncode):
            
            for line in textToEncode:
                if line != "\n":
                    newLine = list(line)
                    for letter in newLine:
                        if letter in normalChars:
                            newLine[newLine.index(letter)] = defaultEncodedChars[normalChars.index(letter)] + "#$#$#&#&@&@^%&^%"
                    textToEncode[textToEncode.index(line)] = "".join(newLine)
                    
                
            textToEncode = "".join(textToEncode)
            fileToEncode = open(filePathToEncode, "w")
            fileToEncode.write(textToEncode)
            fileToEncode.close()
            keyWrite(filePathToEncode)
            print("\n  File Encoded.")
            webbrowser.open(filePathToEncode)
            
        else:
            pass
        
    else:
        print("\n  File not found. Enter a valid path. Don't include quotes at the beginning and ending of the path.")

# This function takes a file/file path and decodes it.

def decrypt(filePathToDecode):
    
    pathValidity = True
    
    try:
        fileToDecode = open(filePathToDecode, "r")
    except FileNotFoundError:
        pathValidity = False
    
    if pathValidity == True:
        
        keyRead(filePathToDecode)
        
        textToDecode = fileToDecode.readlines()
        fileToDecode.close()
    
        if "#$#$#&#&@&@^%&^%" in "".join(textToDecode):
            
            for line in textToDecode:
                if line != "\n":
                    newLine = list(line.replace("#$#$#&#&@&@^%&^%", ""))
                    for letter in newLine:
                        if letter in defaultEncodedChars:
                            newLine[newLine.index(letter)] = normalChars[defaultEncodedChars.index(letter)] + "#$#$#^#^"
                    textToDecode[textToDecode.index(line)] = "".join(newLine).replace("#$#$#^#^", "")

            if "%#$&" in textToDecode[-1]:
                textToDecode.remove(textToDecode[-1])
                
            if "\n" in textToDecode[-1]:
                textToDecode[-1] = textToDecode[-1].replace("\n", "")
                
        else:
            pass

        textToDecode = "".join(textToDecode)
        fileToDecode = open(filePathToDecode, "w")
        fileToDecode.write(textToDecode)
        fileToDecode.close()
        print("\n  File Decoded.")
        webbrowser.open(filePathToDecode)
        
    else:
        print("\n  File not found. Enter a valid path. Don't include quotes at the beginning and ending of the path.")