# ---------------------------------------------- #
# File : File.py                                 #
# Name : Ewan C                                  #
# Date : 12/10/2026                              #
# ---------------------------------------------- #
# This file contains the class definition "file" #
# used for navigating the database               #
# ---------------------------------------------- #
# Revison 1 : Moved Implmentation from           #
#             Explorer.py and added comments     #
#      Date : 12/10/2026                         #
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

# File Class #
class file:

    # Constructor #
    def __init__(self, name, data):
        self.name = name
        self.data = str(data)

    # Display data to console #
    def read(self):
        print(self.data)

    # Allows for the manipulation of file data #
    def edit(self):
        print(self.data)
        newData = input(" -> Start with char 'a' to append, or 'w' to overwrite\n -> Enter new data below:\n")
        if newData[0] == "a":
            self.data += newData[1:]
        elif newData[0] == "w":
            self.data = newData[1:]

    # Contains while loop to allow command s to be run with the file open #
    def open(self):
        _open = True
        while _open:
            action = input(f"Perform action on {self.name} -> ")
            if action == "read":
                self.read()
            elif action == "edit":
                self.edit()
            elif action == "close":
                _open = False
            else:
                print(" - Command not recognised -")

    # Used to construct the structure save line #                
    def createCloseString(self):
        return f"f{self.name}<{self.data}>"

#############
# Functions #
#############
