#Variables in python

#string
first_name, last_name="Vikas" , "anand"
full_name = first_name + " " + last_name
#the above line will throw error as memory 

#this is string concatentaion
#strings in python are immutable

# age = 19 #int
# height = 250.5 #float

# human= True #boolean

#I'll use multiple assignement technique here
age, height, human= 19, 250.5, True 


print(full_name + "\'s" + " age is",age)
#in above example we are not conacatenating string with int as it runs with error
print("His height is " + str(height)+" cm")
#this is typecasting 

#this is if statement
if human:
    print(full_name + " is a human.")

#this will return data type of variable used
print(type(full_name),type(age), type(height), type(human))



