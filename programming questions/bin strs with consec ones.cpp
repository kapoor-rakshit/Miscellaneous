/*
Given an integer m, find no. of binary strings of length m ie no.s from 0 to (2^m)-1 which have consecutive 1's.
*/
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long
void multiply(long long fm[][2],long long tm[][2])
{
    	long long a=(fm[0][0]*tm[0][0]+fm[0][1]*tm[1][0])%mod;
	long long b=(fm[0][0]*tm[0][1]+fm[0][1]*tm[1][1])%mod;
	long long c=(fm[1][0]*tm[0][0]+fm[1][1]*tm[1][0])%mod;
	long long d=(fm[1][0]*tm[0][1]+fm[1][1]*tm[1][1])%mod;
 
		fm[0][0]=a;
		fm[0][1]=b;
		fm[1][0]=c;
		fm[1][1]=d;
}
void power(long long fm[][2],long long tm[][2],long long n)
{
    if(n==0||n==1) return;
    
    power(fm,tm,n/2);                           //1.recursive multiplication to get power(tm,n)
    multiply(fm,fm);                           //2.
    
    if(n%2) multiply(fm,tm);                  //3.
}
long long fibo(long long n)
{
    if(n==0) return 0;                          //for 0 based indexing of fibonacci numbers
    
	long long fm[2][2]={1,1,1,0};              //[ fn+1 fn
	                                           //  fn   fn-1 ]    0 based indexing
	                                           
	                                           //this fm matrix raised to power n gives f(n)
	long long tm[2][2]={1,1,1,0};              
	
	power(fm,tm,n);
	return fm[0][1]%mod;                   //for 0 based indexing use fm[0][1] or fm[1][0]
	                                      //for 1 based indexing use fm[1][1]
}
ll fastmod(ll base,ll expo,int mo)
{
    ll ans=1;
    while(expo>0)
    {
        if(expo%2) ans=(ans*base)%mo;
        base=(base*base)%mo;
        expo/=2;
    }
    return ans;
}
main()
{
    int n;
    scanf("%d",&n);
    ll m;
    while(n--)
    {
        scanf("%lld",&m);
        ll fans=(fastmod(2,m,mod)%mod-fibo(m+2)%mod)%mod;    //total comb. (2^m) - without consec ones (fibo(m+2))
        if(fans>=0)
        printf("%lld\n",fans);
        else printf("%lld\n",fans+mod);                     //if answer is negatve then add modulus to get it to reqd
    }
} 
