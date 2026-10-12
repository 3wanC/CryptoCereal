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
        
