import random

myList = ['rock', 'paper', 'scissors']
print("1.Rock \n2.Paper\n3.Scissors")


while True:
    ch=int(input("Enter the number: "))
    z=random.choice(myList)

    if (ch==1):
        print("Player: ",myList[0])
        print("Computer: ",z)
        if z=='paper':
            print("You lost bro :(")
            break
        elif z=='scissors':
            print("You won :)")
            break
        else:
            print("Match tie...playing again")
            continue

    if (ch==2):
        print("Player: ",myList[1])
        print("Computer: ",z)
        if z=='rock':
            print("You won :)")
            break
        elif z=='scissors':
            print("You lost bro :(")
            break
        else:
            print("Match tie...playing again")
            continue

    if (ch==3):
        print("Player: ",myList[2])
        print("Computer: ",z)
        if z=='rock':
            print("You lost bro :(")
            break
        elif z=='paper':
            print("You won :)")
            break
        else:
            print("Match tie...playing again")
            continue

    else:
        print("Invalid number")
        break
