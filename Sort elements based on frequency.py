from collections import Counter 
from itertools import repeat, chain 
a=int(input())
ini_list =  list(map(int,input().split()))
d=[]
s=[]
result = list(chain.from_iterable(repeat(i, c) 
		for i, c in Counter(ini_list).most_common()))
for j in ini_list:
    if result.count(j)==1:
        d.append(j)
        result.remove(j)
    elif result.count(j)==2:
        k=1
        while(k<=2):
         s.append(j)
         result.remove(j)
         k+=1
    else:
        pass
d=sorted(d)
s=sorted(s)
k=d+s+result
print(''+" ".join([str(z) for z in k]))
