n,k=map(int,input().split())
m=[int(i) for i in input().split()]
m=sorted(m)
m=m[::-1]
print(m[k-1])
