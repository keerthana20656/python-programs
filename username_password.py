
def userid(gmail):
 a=0
 b=0
 c=0
 for i in range(len(gmail)):
    if(gmail[i]=="@"):
        a=i
        continue
    elif(gmail[i]=="."):
        b=i
        continue
    else:
        continue
 if(a<=1  and  b<=2):
      print("invalid user id")
 elif(b<a):
    print("invalid user id ")
 else:
     print("gmail id is uploaded sucessfullyS")
     c+=1
 return(c)
def pswd(password):
 s=len(password)
 e=0
 f=0
 g=0
 h=0
 li=["@","#","$","^","&","*","(",")","_","+"]
 if(s>=5 and s<=15):
   for i in range(len(password)):
    a=password[i].isupper()
    b=password[i].islower()
    c=password[i].isdigit()
    d=i in li
    if(a==True):
        e+=1
        continue
    elif(b==True):
        f+=1
        continue
    elif(c==True):
        g+=1
        continue
    elif(d==True):
        h+=1
        continue
    else:
        continue
  
   if(e>=1 and f>=1 and g>=1 and h>=1):
     print("password entered sucessfully")
   else:
     print("enter valid password")
 else:
     print("password should be within 5 to 15 elements")
 return 1
x=input("enter userid: ")
z=input("password: ")
y=userid(x)
if(y==1):
    k=pswd(z)
