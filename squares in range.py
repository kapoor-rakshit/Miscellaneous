from math import *
t=int(input())
while t:
    a,b=map(int,input().split())
    print(floor(sqrt(b))-ceil(sqrt(a))+1)                      #floor of right - ceil of left + 1
    t-=1
