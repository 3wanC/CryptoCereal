# ---------------------------------------------- #
# File : Generate.py                             #
# Name : Ewan C                                  #
# Date : 15/10/2026                              #
# ---------------------------------------------- #
# This script will generate a set of key files   #
# for use in message encryption. This script can #
# take a while to run.                           #
# ---------------------------------------------- #
# Revison 1 : Created                            #
#      Date : 15/10/2026                         #
# ---------------------------------------------- #

#############
#  Imports  #
#############

import secrets
import os

#############
#  Globals  #
#############

global file_path
global choice_values

choice_values = range(100,500)

#############
#  Classes  #
#############

#############
# Functions #
#############

# ---------------------------------------------- #
# Name       : getInfo                           #
# Parameters : none                              # 
# Returns    : numFiles                          #
#              INT                               #
# ---------------------------------------------- #
# Gets File Path and number of Files from the    #
# user. Verifies them before returning           #
# ---------------------------------------------- #
def getInfo():

    # Get required globals #
    global file_path
    
    correct = False

    # Loop so user can ensure inputs are correct #
    while not correct:

        os.system("cls")
        inputsClean = False

        # Get the file path from the user #
        while not inputsClean:

            # Prompt for file path #
            tmpFile = input("Please enter the file path to the store directory below\n -> Enter: ")

            # Catch user exit code #
            if tmpFile == "Exit":
                return None

            # Test the path given to ensure it is valid and python has permission to write there #
            try:
                # Create, test and delete test file #
                with open(f"{tmpFile}/test.txt", 'w') as file:
                    file.write("test")

                os.remove(f"{tmpFile}/test.txt")

                inputsClean = True
                
            except FileNotFoundError, PermissionError:
                os.system("cls")
                print(f"Invalid FilePath : {tmpFile}")

        # Now have the path, so clear and move on #
        os.system("cls")
        
        inputsClean = False

        # Get the number of files to be generated from the user #
        while not inputsClean:

            # Test the user input #
            try:
                # Prompt for the number of files #
                numFiles = input("Please enter the number of files to generate below\n -> This number must be a positive integer\n -> This number must be greater than zero\n -> Enter: ")

                # Catch user exit code #
                if numFiles == "Exit":
                    return None

                # Ensure the file is an integer above zero #
                if int(numFiles) <= 0:
                    # Trigger the except #
                    raise ValueError("Dummy")
                
                inputsClean = True
                
            except ValueError:
                os.system("cls")
                print(" Hint - Type 'Exit' to quit")

        os.system("cls")

        # We have both inputs verified, check they are correct #
        confirm = input(f"Please ensure the info below is correct before proceeding\n -> File Path  : {tmpFile}\n -> Key Files  : {numFiles}\n -> Enter (y/n): ")

        # If they are find, save the file path and return the number of files. Esle return to nesting while loop #
        if confirm == "y":
            correct = True

            file_path = tmpFile
            return int(numFiles)

# ---------------------------------------------- #
# Name       : createFile                        #
# Parameters : fileNum                           #
#              INT                               #
# Returns    : none                              #
# ---------------------------------------------- #
# Creates the key file                           #
# ---------------------------------------------- #
def createFile(fileNum):

    # Get required globals #
    global file_path
    global choice_values

    writeString = ""

    # Each file contains 50 keys #
    for x in range(50):

        # Use secrests to choose a 3-digit value #
        writeString += str(secrets.choice(choice_values))

    # Write output to file #
    with open(f"{file_path}/{fileNum}.txt", 'w') as file:
        file.write(writeString)
        
# ---------------------------------------------- #
# Name       : doGenerate                        #
# Parameters : none                              # 
# Returns    : result                            #
#              BOOL                              #
# ---------------------------------------------- #
# Function to be called externally vai import    #
# ---------------------------------------------- #  
def doGenerate():

    # Gets the info required for generation #
    numberOfFiles = getInfo()

    # If info is provided, begin generation #
    if not numberOfFiles == None:

        # Create the required files #
        for x in range(numberOfFiles):
            x += 1
            createFile(x)

        # Return True as this was successful #
        return True

    # If we get here, generation did not take place so return false #
    return False

# DEBUG ONLY # result = doGenerate()
