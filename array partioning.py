#SOURCE : https://ashishmadaanblog.wordpress.com/2017/09/12/array-elements-partitioning-problem/

# Similar approach can be followed for even/odd elem

# Make positive elements appear at even indices
#      negative elements appear at odd indices

a=list(map(int,input().split(',')))
n=len(a)

pos=0
neg=1

while 1:
    while pos<n and a[pos]>=0:
        pos+=2
    while neg<n and a[neg]<0:
        neg+=2
        
    if pos<n and neg<n:
        a[pos],a[neg]=a[neg],a[pos]
    else:
        break

print(*a)
