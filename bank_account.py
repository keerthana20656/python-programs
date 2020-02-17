
def deposit(a,accbal):
    accbal+=a
    print("your account balance is :",accbal)
def withdraw(a,accbal):
    if(accbal==0):
        print("you have insufficent balance")
    else:
        accbal=accbal-a
        print("your balance is:",accbal)
while(1):
 n=input("Enter your choice: Deposit or Withdraw or quit")
 accbal=0
 if(n=="Deposit"):
    c=int(input("enter the amount: "))
    deposit(c,accbal)
 elif(n=="Withdraw"):
    b=int(input("enter the amount to withdraw: "))
    withdraw(b,accbal)
 elif(n=="quit"):
     break
 else:
     print("please enter valid choice")
