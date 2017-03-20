"""In mathematics, a Kaprekar number for a given base is a non-negative integer, 
the representation of whose square in that base can be split into two parts that add up to the original number again. 
For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.

NOTE : Right part has same no. of digits as actual number. Left part has remaining digits"""

p=int(input())
q=int(input())
ans=[]
for i in range(p,q+1,1):       #find kaprekar no. in given range
    d=len(str(i))
    sq=i*i
    st=str(sq)
    n=len(st)
    st=list(st)
    l=0
    j=0
    k=n-d
    while j<k:
        l=l*10+int(st[j])
        j+=1
    r=0
    while k<n:
        r=r*10+int(st[k])
        k+=1
    if l+r==i:
        ans.append(i)
if(len(ans)==0):
    print("INVALID RANGE")
else:
    print(*ans)
