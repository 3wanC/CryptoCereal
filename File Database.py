class folder:
    def __init__(self, name, subs):
        self.name = name
        self.subs = subs
        
    def display(self):
        for x in self.subs:
            if isinstance(x, file):
                print(f" --- {x.name}")
            elif isinstance(x, folder):
                print(f" --> {x.name}")
            
    def enter(self, name):
        exists = False
        for x in self.subs:
            if name == x.name and isinstance(x, folder):
                exists = True
                path.updatePath(name)
                break;
        if exists == False:
            print(f"Folder '{name}' not found in current directory")
            
    def open(self, name):
        exists = False
        for x in self.subs:
            if name == x.name and isinstance(x, file):
                exists = True
                x.open()
                break;
        if exists == False:
            print(f"File '{name}' not found in current directory")
            
    def create(self, name, data = None):
        exists = False
        for x in self.subs:
            if name == x.name:
                exists = True
                break;
        if exists:
            print(f"Name {name} already exists in this directory")
        else:
            if data == None:
                self.subs.append(folder(name, []))
            else:
                self.subs.append(file(name, data))
                
    def createCloseString(self):
        closeString = f"d{self.name}<"
        
        for x in self.subs:
            closeString += x.createCloseString()
            
        closeString += ">"
        return closeString
        
class file:
    def __init__(self, name, data):
        self.name = name
        self.data = str(data)
        
    def read(self):
        print(self.data)
        
    def edit(self):
        print(self.data)
        newData = input(" -> Start with char 'a' to append, or 'w' to overwrite\n -> Enter new data below:\n")
        if newData[0] == "a":
            self.data += newData[1:]
        elif newData[0] == "w":
            self.data = newData[1:]
        
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
                
    def createCloseString(self):
        return f"f{self.name}<{self.data}>"
                
class ini(file):
    def read(self):
        pass
        
class path:
    def __init__(self):
        self.location = "Home"
        self.address = ["Home"]
        
    def getAddress(self):
        fullPath = ""
        for x in self.address:
            fullPath += f"/{x}"
        return fullPath
        
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
                
    def updatePath(self, nextFolder = None):
        if nextFolder == None:
            if self.location != "Home":
                self.address.remove(self.address[-1])
                self.location = self.address[-1]
        else:
            self.location = nextFolder
            self.address.append(nextFolder)

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