import time
#I'm importing a library that have timer function

#while loop: runs a block of code as long as it's condition remains true

'''i=0
while(i<5):
    print("I am ", i)
    i=i+1'''

'''name=None #or name=""

# while(len(name)==0):
while not name:
    name= input("Enter your name properly:")

print("Hello "+ name)'''

#for loop= a statement that will executes it's block of code a limited amount of times
# while loop= unlimited, for loop= limited 



'''for i in range(2,3,1):
    #range(start,stop,step)
    #range(stop)
    #range(start,stop )
    print(i)'''

#method of iterating a string using for loop
'''for i in "Vikas Anand":
    print(i)'''

#simulating a timer
'''for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Time's up buddy...")'''

#nested for loop
for i in range(5):
    for j in range(i):
        print("*",end='') #end="" stops our cursor from moving in newline
    print() #used to end the line after nested for loop ends in each iteration

#without nested loop
for i in range(5):
    print("*"*i)

#loop control statements
#break- used to terminate the loop entirely
#continue- skips to the next iteration of the loop
#pass- does nothing, acts as a placeholder

while True:
    name=input("Enter you name: ")
    if name!="" :
        break
phoneNo= "123-456-789"

for number in phoneNo:
    if (number=='-'):
        continue
    print(number, end='')