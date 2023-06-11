import os
import shutil 
#this will give access of copying a file



def p(something):
    print(something)

'''-------Reading a file---------'''

try:
    with open("D:\\python\\test.txt",'r') as file:
        p(file.read())
    #this open method of reading the file and print into console and automatically close it after reading 
except FileNotFoundError:
    p("This file doesn't exists")

    

#to check whether our file is closed or not
# print(file.closed)

'''other methods of file handling
r= reading mode
w= write only mode ,create or overwrite an existing file
a = Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.



'''
# text="\n This line is added using python."
# with open("D:\\python\\test.txt",'a') as file:
#     file.write(text)

with open("D:\\python\\test.txt",'r') as file:
    p(file.read())

'''-----copying operations on file--------'''
#copyfile()=copies contents of a file
#copy() = copyfile()+ permission mode + destination can be a directory
#copy2() = copy()+ copies metadata(file's creation and modification time)

shutil.copyfile("D:\\python\\test.txt","D:\\python\\copy.txt")

