# ---------------------------------------------- #
# File : Encryption.py                           #
# Name : Ewan C                                  #
# Date : 05/09/2026                              #
# ---------------------------------------------- #
# This file contains the encryption and          #
# decryption function. These both except and     #
# return strings.                                #
# ---------------------------------------------- #
# Revison 1 : Created inital script (EC)         #
#      Date : Unknown                            #
#                                                #
# Revison 2 : Add both encrpt and decrypt        #
#             functions to same file. Revised    #
#             processes, adding comments and     #
#             removing redundent code (EC)       #
#      Date : 05/09/2026                         #
# ---------------------------------------------- #

#############
#  Imports  #
#############
import random

#############
#  Globals  #
#############

#############
# Functions #
#############

# ---------------------------------------------- #
# Name       : encrypt                           #
# Parameters : rawString                         #
#              STRING                            #
# Returns    : (keyString, encryptedString)      #
#              TUPLE (STRING STRING)             #
# ---------------------------------------------- #
# This fucntions takes in a string and returns a #
# tuple containing the synthesised encrption key #
# and encrypted data.                            #
# ---------------------------------------------- #
def encrypt(rawString):

    # Create empty variables to store output #
    keyString = ""
    encryptedString = ""

    for x in range(len(rawString)):

        # Get assci value of current character #
        toChange = rawString[x]
        toChange = ord(toChange)
    
        switch = ""

        # Create a random key #
        key = random.randint(100,500)
        hidden = toChange + key
    
        switch = str(key)

        # Concate the output varaibales with the last character #
        keyString = keyString + str(key)
        encryptedString = encryptedString + str(hidden)

    return (keyString, encryptedString)

# ---------------------------------------------- #
# Name       : decrypt                           #
# Parameters : encryptedPair                     #
#              TUPLE (STRING STRING)             #
# Returns    : rawString                         #
#              STRING                            #
# ---------------------------------------------- #
# This fucntion takes a tuple containing an      #
# encrypted string and the key then coverts it   #
# back to its original.                          #
# ---------------------------------------------- #
def decrypt(encryptedPair):

    # Split tuple into contained variables #
    keySting = encryptedPair[0]
    encryptedString = encryptedPair[1]

    # Initiate count and return string #
    posCount = 0
    rawString = ""

    while posCount < len(encryptedString):

        # Get the current 3 digit char from strings #
        currentKey = keySting[posCount] + keySting[posCount+1] + keySting[posCount+2]
        currentLetter = encryptedString[posCount] + encryptedString[posCount+1] + encryptedString[posCount+2]

        # Convert from ASCCI #
        decoded = chr(int(currentLetter) - int(currentKey))
        rawString = rawString + decoded

        # Jump to next char #
        posCount = posCount + 3
        
    return rawString

#############
# File  End #
#############
