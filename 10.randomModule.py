import random

x = random.randint(1,6)
#we can generate a random number between 1 and 6
# print(x)

y=random.random()
#this will generate a random number between 0 and 1
# print(y)

myList = ['rock', 'paper', 'scissors']
z=random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"jack","Queen","King"]
random.shuffle(cards)

print(cards)
