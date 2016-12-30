from math import *
n=int(input())
while n:
    s=0
    m=int(input())
    sq=int(sqrt(m))
    for i in range(1,sq+1,1):
        if m%i==0:
            s+=(i+m//i)
        
    if sq*sq==m:
        print(s-sq)
    else:
        print(s)
    
    n=n-1 
