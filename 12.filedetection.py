import os

def p(something):
    print(something)

path= "D:\\python\\test.txt"

if os.path.exists(path):
    p("That location exists")
    if os.path.isfile(path):
        p("This is a file")
    elif os.path.isdir(path):
        p("This is a directory")
    
else:
    p("This location doesn\'t exist")




