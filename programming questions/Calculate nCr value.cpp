#include<bits/stdc++.h>
#define li long long int
int mo=1000000007;
using namespace std;
main
{
li calcfact[100001];
	calcfact[0]=1;
	for(int i=1;i<=100001;i++)
	calcfact[i]=(calcfact[i-1]*i)%mo;                                           //calculate  factorials
	
	 li fastmodexp(li base,li exponent,li m)                                    //fast modular exponentiation
    {
    li result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)result = (result * base) % m;
        exponent = exponent >> 1;
        base = (base * base) % m;
    }
    return result;
}
	
	 li t=(calcfact[i]*calcfact[m-i])%mo;                                       //(n-r)!*(r)!
	 
	fans=(fans%mo+(calcfact[m]*fastmodexp(t,mo-2,mo))%mo)%mo;                  //(n)!*   (inverse modulus property used for t%mo) ie
	                                                                           //        (A^-1)%mo == (A^mo-2)%mo;
	
	 printf("%lld\n",fans);
}
