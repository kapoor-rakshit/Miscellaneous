# EXAMPLE 1

# XOR from 1 to n

#  Find the remainder of n by moduling it with 4.
# If rem = 0, then xor will be same as n.
# If rem = 1, then xor will be 1.
# If rem = 2, then xor will be n+1.
# If rem = 3 ,then xor will be 0.

# coz When we do XOR of numbers, we get 0 as XOR value just before a multiple of 4



# EXAMPLE 2

# XOR from L to R

# Find XOR val 1 to R     as above
# Find XOR val 1 to L-1   as above
# XOR this upper and lower bounds

# coz (L)^(L+1)^(L+2).......^(R)   =  1^2^3^...(L-1) ^ [L ^ L+1 ^ ....^ R] ^ 1^2^3^...(L-1)



# EXAMPLE 3
# given an array where A(i) = A(i-1) ^ i     OR      0^1^2^3^.....^Ai
# find XOR for elem A(l) to A(R) where L,R defines range

def chk(l):
    if l%8==0 or l%8==1:               # Array becomes 0,1,3,0,4,1,7,0,8.... ie in a grp of 4 it becomes 2 so total of 8 elem grp will become 0
        lower=l
    elif l%8==2 or l%8==3:
        lower=2
    elif l%8==4 or l%8==5:
        lower=l+2
    elif l%8==6 or l%8==7:
        lower=0
    return lower

q=int(input())
while q:
    l,r=map(int,input().split())

    print(chk(l-1)^chk(r))
    q=q-1