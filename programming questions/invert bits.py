import sys
n=int(input())
sz=sys.getsizeof(int)
res=0
fact=1
for i in range(0,32,1):               #replace 32 with the size required (sz)
    fact*=2
fact=fact-1                           #invert of 0 ie 11111111..........111  all ones
while n:
    a=int(input())
    print(a^fact)                     #XOR with 1 result in NOT of a bit
    n=n-1
