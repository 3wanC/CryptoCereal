# ---------------------------------------------- #
# File : Exploer.py                              #
# Name : Ewan C                                  #
# Date : 15/10/2026                              #
# ---------------------------------------------- #
# This file contains the implmentation for the   #
# classes path and folder. It also contains the  #
# command structure for creating, exploring and  #
# terminating the database.                      #
# "folder" is an object with a name used to      #
# contain other folders and files.               #
# "path" is a construct used to navigate through #
# the database                                   #
# ---------------------------------------------- #
# Revison 1 : Added comments                     #
#      Date : 15/10/2026                         #
# ---------------------------------------------- #

#############
#  Imports  #
#############

from File import file

#############
#  Globals  #
#############

#############
#  Classes  #
#############

# folder class #
class folder:

    # ---------------------------------------------- #
    # Name       : __init__                          #
    # Parameters : name, subs                        #
    #              STRING, LIST                      # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Constructor and data initiliation              #
    # ---------------------------------------------- #
    def __init__(self, name, subs):
        self.name = name
        self.subs = subs

    # ---------------------------------------------- #
    # Name       : display                           #
    # Parameters : none                              # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Loops through its subs and prints to console   #
    # ---------------------------------------------- #    
    def display(self):
        for x in self.subs:

            # Prints --- for files and --> for folders #
            if isinstance(x, file):
                print(f" --- {x.name}")
            elif isinstance(x, folder):
                print(f" --> {x.name}")

    # ---------------------------------------------- #
    # Name       : enter                             #
    # Parameters : name                              #
    #              STRING                            #
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Attempts to enter a folder of the name given   #
    # as an argument to the function                 #
    # ---------------------------------------------- #        
    def enter(self, name):
        exists = False

        # Attempts to find fplder #
        for x in self.subs:
            if name == x.name and isinstance(x, folder):
                exists = True

                # Folder exists to enter it #
                path.updatePath(name)
                break;
        if exists == False:
            print(f"Folder '{name}' not found in current directory")

    # ---------------------------------------------- #
    # Name       : open                              #
    # Parameters : name                              #
    #              STRING                            # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Attempts to open a file of the name given as   #
    # an argument to the function                    #
    # ---------------------------------------------- #        
    def open(self, name):
        exists = False

        # Ensures to find file #
        for x in self.subs:
            if name == x.name and isinstance(x, file):
                exists = True

                # File found so open it #
                x.open()
                break;
        if exists == False:
            print(f"File '{name}' not found in current directory")

    # ---------------------------------------------- #
    # Name       : create                            #
    # Parameters : name, data                        #
    #              STRING, (STRING)                  #
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Attempts to create a new folder in the current #
    # area, if data is given, a file. It will not    #
    # create an entity with the same name as another #
    # ---------------------------------------------- #        
    def create(self, name, data = None):
        exists = False

        # Ensures there are no duplicates #
        for x in self.subs:
            if name == x.name:
                exists = True
                break;
        if exists:
            print(f"Name {name} already exists in this directory")
        else:
            # Create File or Folder based on data parameter #
            if data == None:
                self.subs.append(folder(name, []))
            else:
                self.subs.append(file(name, data))

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
        closeString = f"d{self.name}<"

        # Call same function on all folder children #
        for x in self.subs:
            closeString += x.createCloseString()
            
        closeString += ">"
        return closeString

# path class #
class path:

    # ---------------------------------------------- #
    # Name       : __init__                          #
    # Parameters : none                              # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Constructor and data initiliation              #
    # ---------------------------------------------- #
    def __init__(self):
        # location and address are used to store the users current location #
        self.location = "Home"
        self.address = ["Home"]

    # ---------------------------------------------- #
    # Name       : getAddress                        #
    # Parameters : none                              # 
    # Returns    : fullPath                          #
    #              STRING                            #
    # ---------------------------------------------- #
    # Returns the current file path                  #
    # ---------------------------------------------- #    
    def getAddress(self):
        fullPath = ""
        for x in self.address:
            fullPath += f"/{x}"
        return fullPath

    # ---------------------------------------------- #
    # Name       : getLocation                       #
    # Parameters : none                              # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Allows for the manipulation of data            #
    # ---------------------------------------------- #    
    def getLocation(self):
        level = 1
        if len(self.address) == 1:
            return folder_Home
        else:
            folderToSearch = folder_Home
            while level < len(self.address):
                for x in folderToSearch.subs:
                    if x.name == self.address[level]:
                        folderToSearch = x
                level += 1
            return folderToSearch

    # ---------------------------------------------- #
    # Name       : edit                              #
    # Parameters : none                              # 
    # Returns    : none                              #
    # ---------------------------------------------- #
    # Allows for the manipulation of data            #
    # ---------------------------------------------- #            
    def updatePath(self, nextFolder = None):
        if nextFolder == None:
            if self.location != "Home":
                self.address.remove(self.address[-1])
                self.location = self.address[-1]
        else:
            self.location = nextFolder
            self.address.append(nextFolder)

#############
# Functions #
#############

# ---------------------------------------------- #
# Name       : edit                              #
# Parameters : none                              # 
# Returns    : none                              #
# ---------------------------------------------- #
# Allows for the manipulation of data            #
# ---------------------------------------------- #
def getDirString(toSearch, dirNum):
    openCnt = 0
    closCnt = 0
    dirString = ""
    start = False
    count = 0
    
    for x in toSearch:
        dirString += x
        if x == "<":
            openCnt += 1
            start = True
        elif x == ">":
            closCnt += 1
            
        if start == True and closCnt == openCnt:
            if count == dirNum:
                break
            else:
                start = False
                openCnt = 0
                closCnt = 0
                dirString = ""
                count += 1
                
    return dirString

# ---------------------------------------------- #
# Name       : edit                              #
# Parameters : none                              # 
# Returns    : none                              #
# ---------------------------------------------- #
# Allows for the manipulation of data            #
# ---------------------------------------------- #    
def getDirItems(stringToCheck):
    itemCount = 0
    check = False

    while check == False:
        test = getDirString(stringToCheck, itemCount)
        if test != "":
            itemCount += 1
        else:
            check = True

    for x in range(itemCount):
        createPart(stringToCheck, x)

# ---------------------------------------------- #
# Name       : edit                              #
# Parameters : none                              # 
# Returns    : none                              #
# ---------------------------------------------- #
# Allows for the manipulation of data            #
# ---------------------------------------------- #
def createPart(stringBiuld, root):
    currentPart = getDirString(stringBiuld, root)
    
    nameFound = False
    name = ""
    count = 1
    
    while nameFound == False:
        if currentPart[count] != "<":
            name += currentPart[count]
            count += 1
        else:
            nameFound = True
    
    if currentPart[0] == "d":
        path.getLocation().create(name)
        path.getLocation().enter(name)
        
        cutNum = len(name) + 2
        tempPart = currentPart[cutNum:-1]

        getDirItems(tempPart)
        path.updatePath()
        
    elif currentPart[0] == "f":
        dataFound = False
        data = ""
        dataCount = 1 + count
        while dataFound == False:
            if currentPart[dataCount] != ">":
                data += currentPart[dataCount]
                dataCount += 1
            else:
                dataFound = True
                
        path.getLocation().create(name, data)

path = path()

string = "dfolder_1<dfolder_1<ffile_2<123456>>ffile_1<12345>ffile_2<67890>>dfolder_2<dfolder_3<ffile_3<24680>>>ffile_4<76543>"

folder_Home = folder("Home", [])

getDirItems(string)

# ---------------------------------------------- #
# Name       : edit                              #
# Parameters : none                              # 
# Returns    : none                              #
# ---------------------------------------------- #
# Allows for the manipulation of data            #
# ---------------------------------------------- #
cont = True
while cont:
    action = input(f"user{path.getAddress()}/ -> ")
    if action == "exit":
        cont = False
    elif action[:5] == "enter":
        path.getLocation().enter(action[6:])
    elif action[:4] == "open":
        path.getLocation().open(action[5:])
    elif action[:6] == "create":
        actionVars = action.split()
        if len(actionVars) == 2:
            path.getLocation().create(actionVars[1])
        else:
            path.getLocation().create(actionVars[1], actionVars[2])
    elif action == "list":
        path.getLocation().display()
    elif action == "back":
        path.updatePath()
    else:
        print(" - Command not recognised -")
        
exitString = folder_Home.createCloseString()[6:-1]

print(string)
print(exitString)
