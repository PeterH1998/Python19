code = raw_input("Enter Code")
length = len(code)
ocount = 0
ccount = 0
fair = True
for x in range(0, length):
    if code[x] == "(":
        ocount += 1
    elif code[x] == ")":
        ccount += 1
    if ocount < ccount:
        fair = False

if fair == True:
    if ocount == ccount:
        print "Code looks fine."
    else:
        print "You haven't close all your parentheses."
else:
    print "You closed a parentheses you hadn't open."
