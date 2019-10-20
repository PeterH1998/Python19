myfile = open('myfile.txt')
info = myfile.read()
space = 0
delete = 0
backspace = 0
tab = 0
for character in info:
    if character == " ":
        space +=1
    elif character == '\N{delete}':
        delete += 1
    elif character == '\b':
        backspace += 1
    elif character == '\t'
        tab += 1
sumall = space + delete + backspace + tab
print ("Space: " + space)
print ("Delete: " + delete)
print ("Backspace: " backspace)
print ("Tab: " + tab)
print ("All non printable characters: " + sumall)

myfile.close()