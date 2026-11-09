# ---------------------------------------------- #
# File : Encryption.py                           #
# Name : Ewan C                                  #
# Date : 09/11/2026                              #
# ---------------------------------------------- #
# This script will perfrom the encryption and    #
# decryption for the fully keyed RT              #
# ---------------------------------------------- #
# Revison 1 : Created                            #
#      Date : 09/11/2026                         #
# ---------------------------------------------- #

#############
#  Imports  #
#############

#############
#  Globals  #
#############

#############
#  Classes  #
#############

#############
# Functions #
#############

def getFileData(filePath):
    with open(filePath, 'r') as file:
        return file.read()

# ---------------------------------------------- #
# Name       : encrypt                           #
# Parameters : file, key, numConsumed, index,    #
#              STRING, STRING, INT, INT,         #
#              destination                       #
#              STRING                            #
# Returns    : none                              #
# ---------------------------------------------- #
# Takes the file to be encrypted and applies the #
# key. Then saves an encrypted version to the    #
# destination location                           #
# ---------------------------------------------- #
def encrypt(file, key, numConsumed, index, destination):

    rawData = getFileData(file)

    count = index
    fullKey = ""

    while count <= index + numConsumed:

        tmpPath = key + str(f"\\{count}.txt")

        with open(tmpPath, 'r') as file:
            fullKey += file.read()
        
        count += 1

    endData = ""
    
    for x in rawData:
        tmp = ord(x)

        tmp += int(fullKey[:3])

        fullKey = fullKey[3:]

        endData += str(tmp)

    with open(destination, 'w') as file:
        file.write(endData)

# DEBUG ONLY #
encrypt("C:\\SoftwareDevelopment\\GitRepos\\CryptoCeral\\INWORK FullyKeyedRT\\tstOnly\\raw\\testing.txt",
        "C:\\SoftwareDevelopment\\GitRepos\\CryptoCeral\\INWORK FullyKeyedRT\\tstOnly\\key",
        10,1,
        "C:\\SoftwareDevelopment\\GitRepos\\CryptoCeral\\INWORK FullyKeyedRT\\tstOnly\\end\\testing.txt")
    
