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

#############
#  Classes  #
#############

#############
# Functions #
#############

def getInfo():

    global file_path
    correct = False

    while not correct:

        os.system("cls")
        inputsClean = False

        while not inputsClean:
            
            tmpFile = input("Please enter the file path to the store directory below\n -> Enter: ")

            if tmpFile == "Exit":
                return None

            try:
                with open(f"{tmpFile}/test.txt", 'w') as file:
                    file.write("test")

                os.remove(f"{tmpFile}/test.txt")

                inputsClean = True
                
            except FileNotFoundError, PermissionError:
                os.system("cls")
                print(f"Invalid FilePath : {tmpFile}")

        os.system("cls")
        
        inputsClean = False

        while not inputsClean:

            try:
                numFiles = input("Please enter the number of files to generate below\n -> This number must be a positive integer\n -> This number must be greater than zero\n -> Enter: ")

                if numFiles == "Exit":
                    return None
                
                if int(numFiles) <= 0:
                    int("Dummy")
                
                inputsClean = True
                
            except ValueError:
                os.system("cls")
                print(" Hint - Type 'Exit' to quit")

        os.system("cls")

        confirm = input(f"Please ensure the info below is correct before proceeding\n -> File Path  : {tmpFile}\n -> Key Files  : {numFiles}\n -> Enter (y/n): ")

        if confirm == "y":
            correct = True

            file_path = tmpFile
            return numFiles

def createFiles(numFiles):

    global file_path
    
  
def doGenerate():
    numberOfFiles = getInfo()

    if not numberOfFiles == None:
        createFiles(numberOfFiles)

doGenerate()
