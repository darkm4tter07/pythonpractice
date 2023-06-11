#decision making

who = input("Are you a robot = (y/n): ")

if (who=='N' or who=='n'):
    print("You are a robot.")
elif(who=='N' or who=='n'): #and or not are logical operators
    print("Hello hoomann!!")
else:
    thenwho= input("You are neither a robot nor a human, then who are you.... ")
    if(thenwho[0]=='a' or thenwho[0]=='e' or thenwho[0]=='i' or thenwho[0]=='o' or thenwho[0]=='u'):
        print("So you are an "+ thenwho)
    else:
        print("So you are a "+ thenwho)
    print("You seems interesting :)")