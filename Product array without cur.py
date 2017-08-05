a=list(map(int,input().split()))
temp=1
prod=[]
for i in a:
    prod.append(temp)                #Product of left elems of cur
    temp*=i
temp=1
n=len(prod)
for i in range(n-1,-1,-1):           #Product of right elems of cur
    prod[i]*=temp
    temp*=a[i]
    
print(*prod)
