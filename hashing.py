from collections import *
n=int(input())
a=list(map(int,input().split()))
d=(Counter(a))                             #returns a dict containing key as numbers and values as correspondign count
q=int(input())
s=0
while(q):
    b=input()
    b=b.split(' ')
    b[0],b[1]=int(b[0]),int(b[1])
    if(d[b[0]]>0):
        s+=b[1]
        d[b[0]]-=1
    q=q-1
print(s)
