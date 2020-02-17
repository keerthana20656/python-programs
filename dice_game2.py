import random
while(1):
    print("enter your choice")
    a=input()
    if(a=="YES" or a=="yes" or a=="Yes" or a=="ys"):
        print(random.randint(1,6))
        continue
    elif(a=="NO" or a=="No" or a=="no" or a=="N"):
        print("game over")
        break
    else:
        print("enter valid input")
        continue
