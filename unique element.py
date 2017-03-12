#All elements in an array ocuur "twice" except one unique element. Find that element.
#Traverse the array and find XOR of all elements, gives the unique element. Because 1^1=0, 0^0=0, 1^0=1

n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(1,n,1):
    ans=ans^a[i]
print(ans)


#All elements in an array ocuur "thrice" except one unique element. Find that element.

import sys
n=int(input())
a=list(map(int,input().split()))
sz=sys.getsizeof(int)
res=0
s=0
for i in range(0,sz,1):               #Traverse all bits of an integer
    x=(1<<i)                          #Set each bit starting from LSB to MSB and reset all except current 
    for j in range(0,n,1):
        if a[j]&x:                    #Check if the current bit of element is also set 
            s+=1
    if s%3:                           #If no. of bits set are not multiple of 3 then that bit is set in unique element 
        res|=x
    s=0
print(res)
