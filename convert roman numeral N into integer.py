def value(r):
  if r=="I":
    return 1
  if r=="V":
    return 5
  if r=="X":
    return 10
  if r=="L":
    return 50
  if r=="C":
    return 50
  return -1
s=input()
res=0
i=0
while(i<len(s)):
  s1=value(s[i])
  if(i+1<len(s)):
    s2=value(s[i+1])
    print(s2)
    if s1>=s2:
      res+=s1
      i=i+1
      print("yes")
    else:
      res=res+s2-s1
      i+=2
