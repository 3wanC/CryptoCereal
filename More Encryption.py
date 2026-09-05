import random

string = input("Enter your word: ")
key = [0] * len(string)
hidden = [0] * len(string)

fullKey = ""
fullHidden = ""
switching = 0

for x in range(len(string)):
    
    toChange = string[x]
    toChange = ord(toChange)
    
    switch = ""
    
    key[x] = random.randint(100,500)
    
    hidden[x] = toChange + key[x]
    
    switch = str(key[x])
    
    if (x % 3 == 0) | (x == 0):
        switching = 1
    else:
        switching = 0
    
    if switching == 1:
        sw1 = switch[0]
        sw2 = switch[1]
        sw3 = switch[2]
    
        switch = sw3 + sw2 + sw1
        
    fullKey = fullKey + switch #str(key[x])
    fullHidden = fullHidden + str(hidden[x])
    
    if len(str(toChange)) < 3:
        strToChange = "0" + str(toChange)
    else:
        strToChange = str(toChange)
    
    print(string[x], " ", strToChange, " ", str(key[x]), " ", switching, " ", switch, " ", str(hidden[x]))
    
print(fullKey)
print(fullHidden)