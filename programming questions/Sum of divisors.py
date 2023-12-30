'''Sum of all divisors of number (1 and number inclusive)'''
from math import *
n=int(input())
while n:
    s=0
    m=int(input())
    sq=int(sqrt(m))
    for i in range(1,sq+1,1):
        if m%i==0:
            s+=(i+m//i)
        
    if sq*sq==m:
        print(s-sq)
    else:
        print(s)
    
    n=n-1 

'''Sum of all divisors in RANGE L=1 to R=number'''
#include <bits/stdc++.h>
using namespace std;
main() {
    long long ans=0;
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
	    ans+=i*(n/i);
	}
	printf("%lld\n",ans);
}

'''Sum of all odd / even divisors in RANGE L to R'''
    l,r=map(int,input().split())
    ansr=0
    ansl=0
    for i in range(1,r+1,2):                      #odd divisors sum from 1 to R        #for even divisors sum initialize with i=2
        ansr+=(i*(r//i))
    for i in range(1,l,2):                        #odd divisors sum from 1 to L-1      #for even divisors sum initialize with i=2
        ansl+=(i*((l-1)//i))
    print(ansr-ansl)                              #subtract to get reqd range L to R
