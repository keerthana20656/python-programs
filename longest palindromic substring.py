s=input()
i=0
t=0
k=s
while(i<=len(s)-1):
    if k==k[::-1]:
        m=k 
        break
    k=s[t+i:]
    i+=1
print(m)
