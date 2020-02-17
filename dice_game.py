import random
while(1):
    print("enter '1 if you want to play the game' '2 if you want to exit the game'")
    a=int(input())
    if(a==1):
        print(random.randint(1,6))
        continue
    else:
        print("the game is over")
        break
