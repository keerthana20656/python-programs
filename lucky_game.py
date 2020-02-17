import random
n=1
while(n<=5):
    print("enter num between(1,9)")
    x=int(input())
    a=random.randint(1,9)
    n+=1
    if(a==x):
        print("your are win")
        break
    else:
        print("try again")
        continue
    
print("you lose the game")
