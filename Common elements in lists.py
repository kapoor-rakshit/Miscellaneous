a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a=sorted(a)
b=sorted(b)
c=sorted(c)

la=len(a)
lb=len(b)
lc=len(c)

i=0
j=0
k=0
ans=[]
while i<la and j<lb and k<lc:
    if(a[i]==b[j] and b[j]==c[k]):
        ans.append(a[i])
        i+=1
        j+=1
        k+=1
    elif(a[i]<b[j]):
        i+=1
    elif(b[j]<c[k]):
        j+=1
    else:
        k+=1
print(*ans)
