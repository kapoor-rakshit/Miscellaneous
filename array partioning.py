#SOURCE : https://ashishmadaanblog.wordpress.com/2017/09/12/array-elements-partitioning-problem/

# Similar approach can be followed for even/odd elem partioning

# Make positive elements appear at even indices
#      negative elements appear at odd indices

# NOTE : not necessarily alternative

#      relative order for elem must be maintained


a=list(map(int,input().split(',')))
n=len(a)

pos=0
neg=1

while 1:
    while pos<n and a[pos]>=0:                    # search for undesired elem 
        pos+=2
    while neg<n and a[neg]<0:                     # search for undesired elem
        neg+=2
        
    if pos<n and neg<n:
        a[pos],a[neg]=a[neg],a[pos]
    else:
        break

print(*a)
