message = input("Enter encrypted message: ")
fullKey = input("Enter encryption key: ")

x = 0;
y = len(message)

string = ""

while x < y:
    
    currentKey = 0
    currentLetter = 0
    
    currentKey = fullKey[x] + fullKey[x+1] + fullKey[x+2]
    currentLetter = message[x] + message[x+1] + message[x+2]

    decoded = chr(int(currentLetter) - int(currentKey))
    
    print(currentKey, " ", currentLetter, " ", (int(currentLetter) - int(currentKey)), " ", decoded)
    
    string = string + decoded
    
    x = x + 3
    
print("\n", string)
    
