#NOTE : perfect squares always have odd no. of divisors
#       this prog will find no. of perfect squares (or those with odd no. of divisors) in the given range

from math import *
t=int(input())
while t:
    a,b=map(int,input().split())
    print(floor(sqrt(b))-ceil(sqrt(a))+1)                      #floor of right - ceil of left + 1
    t-=1
