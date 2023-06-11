name= "Vikas Anand"

#useful strings methods
print(len(name)) #returns length of string
print(name.find("k")) #returs index of k in name
print(name.upper()) #returns uppercase version of string
print(name.lower())
print(name.isdigit()) #checks whether characters are numbers or not 
print("46".isdigit())
print(name.isalpha()) #checks whether string includes no blankspaces

print(name.replace("a", "A")) #replace all a with A

threetimename= name*3 #we can multiply strings
print(threetimename)
        
#typecasting a datatype

x=1
y=2.0
z="3"
print(z*3)
z=int(z) #this is typecasting of string to integer
print(z*3)

#string slicing
# 1.can be done by index method
# 2. can be done by slice() funtion
#indexing[start:stop:step] it will give string upto stop-1 index only starting from start index
firstname= name[0:5]  #vikas
print(firstname)
print(firstname[0::2])
#in above expression only starting index and step is given here 2 means that it will skip one char after starting index and run till str.length()

#reversing the string
print(name[::-1])

website1= "https://google.com"
website2= "https://wikipedia.com"
website= website1[slice(8,-4)]
#it includes 8th index but not include -4th index
#negative index starts from end of string with -1 and runs towards left end of the string
print(website)
print(website2[slice(8,-4)])

'''-----index operator [] -----'''
na= "las vegas"
if(na[0].islower()):
    na=na.capitalize() #capitalize function only capitalize first alphabet
print(na)


'''-----string formatting----'''
animal= 'cow'
place= 'moon'

# print("The "+ animal+ " jumped over the "+ place)

print("The {} jumped over the {}".format(animal,place))
#{} are called fromat fields, format() takes positional arguments

#another way using keyword arguments
print("You are {name:^10} and you are {age} years old".format(age=19,name="Vikas Anand"))

#we can add paddng to format fields like this {:10}, it will leaves 10 spaces after taking the arguments , this is right align. We can also align text to center using {:^10} 

pi= 3.14159
number= 69696969

print("The number pi is {:.8f} and in binary this is {:b}".format(pi,number))

#this will retur upto 2nd decimal palce of pi somewhat similar to C language


