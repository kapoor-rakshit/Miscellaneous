# given an array , find the XOR of each subarrays and result is XOR of these subarrays.

n=int(input())
while n:
    ans=0
    l=int(input())
    a=list(map(int,input().split()))
    for i in range(0,l,1):
        if ((l-i)*(i+1))%2==1:                 # check for count of occurence of each elem in subarrays , if odd consider elem 
            ans^=a[i]
    print(ans)
    n=n-1