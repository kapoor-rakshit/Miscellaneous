'''Check if a number can be expressed in form of x^y'''

from math import *
n=int(input())
sq=int(sqrt(n))
f=0

for i in range(2,sq+1,1):
    temp=int(i)
    while temp<n:
        temp*=i
    if temp==n:
        f=1
        print("True")
        break
if n==1:
    print("True")
elif f==0:
    print("False")
