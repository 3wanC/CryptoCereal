# ---------------------------------------------- #
# File : Run.py                                  #
# Name : Ewan C                                  #
# Date : 15/10/2026                              #
# ---------------------------------------------- #
# This script is for controling UI on the cosole #
# ---------------------------------------------- #
# Revison 1 : Created                            #
#      Date : 13/11/2026                         #
# ---------------------------------------------- #

#############
#  Imports  #
#############

import Generate
import Encryption
import os

#############
#  Globals  #
#############

#############
#  Classes  #
#############

#############
# Functions #
#############

def prepareGen():
    os.system("cls")

    action = input("Generate Key\n\nPlease ensure you have a location in mind of where to store your key, it can be large\n\t1 - Quit\n\t2 - Return to Menu\n\nPress enter to continue: ")

    if action == "1":
        return False
    elif action == "2":
        return True
    else:
        Generate.doGenerate()
        return True

def main():
    print("Welcome to Crypto Cereal FullyKeyedRT\n")

    running = True

    while running:

        isValid = False

        while not isValid:

            try:
                action = int(input("What would you like to do today? (Enter number that corrasponds to option)\n\t1 - Encrypt Files\n\t2 - Decrypt Files\n\t3 - Generate New Key\n\t4 - Help\n\t5 - View License\n\t6 - Exit\n"))

                if 1 > action or action > 6:
                    int("Dummy")
                
            except ValueError:
                os.system("cls")
                print("!ERROR !Please ensure you enter a valid interger value\n")
                continue

            isValid = True

        if action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            running = prepareGen()
            os.system("cls")
        elif action == 4:
            pass
        elif action == 5:
            pass
        else:
            running = False
                

# Run the program #
main()
