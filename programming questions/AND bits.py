#Given a range, AND the bits of all numbers in this range 

import sys
n=int(input())
sz=sys.getsizeof(int)
while n:
    a,b=map(int,input().split())
    res=0
    for i in range(32,-1,-1):              #replace 32 with reqd bitsize. Start from max size
        if (a&(1<<i))!=(b&(1<<i)):         #if current bits of both numbers not same, break
            break
        if a&(1<<i):                       #if current bit is 1 for both, set it ON in answer
            res|=(1<<i)
    print(res)
    n=n-1
