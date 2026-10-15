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

    # ---------------------------------------------- #
    # Name       : __init__                          #
    # Parameters : name, data                        #
    #              STRING, STRING                    #
    # Returns    : none                              #
    # ---------------------------------------------- #
    # This is the constructor for the File class     #
    # ---------------------------------------------- #
    def __init__(self, name, data):
        self.name = name
        self.data = str(data)

    # ---------------------------------------------- #
    # Name       : read                              #
    # Parameters : none                              #
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Prints the contents of data to the console     #
    # ---------------------------------------------- #
    def read(self):
        print(self.data)

    # ---------------------------------------------- #
    # Name       : edit                              #
    # Parameters : none                              # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Allows for the manipulation of data            #
    # ---------------------------------------------- #
    def edit(self):
        print(self.data)
        newData = input(" -> Start with char 'a' to append, or 'w' to overwrite\n -> Enter new data below:\n")
        if newData[0] == "a":
            self.data += newData[1:]
        elif newData[0] == "w":
            self.data = newData[1:]

    # ---------------------------------------------- #
    # Name       : open                              #
    # Parameters : none                              #
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Allows commands to by run on the opne file and #
    # procides the close functionallity              #
    # ---------------------------------------------- #
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

    # ---------------------------------------------- #
    # Name       : createCloseString                 #
    # Parameters : none                              #
    # Returns    : formatedString                    #
    #              STRING                            #
    # ---------------------------------------------- #
    # This allows the explorer to create the file    #
    # structure string so that data can be saved     #
    # ---------------------------------------------- #                
    def createCloseString(self):
        return f"f{self.name}<{self.data}>"

#############
# Functions #
#############
