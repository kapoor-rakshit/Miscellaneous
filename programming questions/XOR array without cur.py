a=list(map(int,input().split()))
x=0
for i in a:
    x=i^x                            #XOR of all elems to get set/reset bits
n=len(a)
for i in range(0,n,1):
    a[i]=a[i]^x                   #XOR with each elem the prod to invert bits of a[i] which are set in prod
print(*a)
