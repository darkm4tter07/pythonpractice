#exception= evenets detected during execution that interrupt the flow of a program

'''
num= int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
result= num/den
#this will show exception at den=0 like zerodivision error

print(result)'''

try:
    num= int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))
    result= num/den
    #we can have multiple exception box
except ZeroDivisionError as e:
    print(e)
    print("Zero can't be the denominator. idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    #runs after checking for all exceptions
    print(result)
finally:
    print("This will always execute")