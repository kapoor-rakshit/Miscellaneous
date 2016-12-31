'''Given an array, find the no. of pairs whose XOR is equal to given integer (x here)'''

n,x=map(int,input().split())
a=list(map(int,input().split()))

chk=[]
ans=0
for i in range(0,100001,1):                       #hash array initialized to 0
    chk.append(0)
for i in range(0,n,1):                            #hash the values of array
    chk[a[i]]+=1

for i in range(0,100001,1):                      #100000 gives the upper limit of value in input array
    if(i^x<=100000):
        if(i==i^x):
            ans+=chk[i]*(chk[i]-1)
        else:
            ans+=chk[i]*chk[i^x]
print(ans//2)
        
