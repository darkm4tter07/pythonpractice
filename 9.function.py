def hello(name):
    print("Hello "+name)

def swap(a,b):
    #scope of these 3 local variables are only upto function only
    temp=a
    a=b
    b=temp
    return a,b

hello("vikas")
#these 2 are global variables
#local > enclosing > global > built-in
a=5
b=6
a,b=swap(a,b)
print(a,b)

#while passing an argument in parameters of function it will take by default in order to avoid this we use identifier

def hello(first,last):
    print("Hello "+first+ " "+last)

hello(last="anand",first='Vikas') #passing arguments using identifiers

'''-----------Nested Functions-----------'''
num=-3.14
num= round(float(abs(num))) #we are nesting 3 functions here
print(num)


'''------args-------in functions'''
#*args= parameter taht will pack all arguments into a tuple
#useful so that a function can accept a varying amount of arguements

def add(*numbers):
    sum=0
    numbers = list(numbers) #this is typecasting a tuple into list, as tuple is immutable and we can't modify tuple
    for i in numbers:
        if(i<0):
            i=abs(i)
        sum +=i
    return sum

print(add(1,2,3,4,-5))

'''------kwargs-------in functions'''
# **kwargs = parameter that will pack all arguments into a dictionary
#useful so that a function can accept a varying amount of keyword arguments

def hello(**names):
    # print("Hello " + kwargs['first']+ " " +kwargs["last"])
    print("Hello ", end="")
    for i in names.values():
        print(i,end=" ")

hello(first="vikas", middle="darkmatter", last="anand")


