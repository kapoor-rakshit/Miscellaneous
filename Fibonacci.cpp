/*NOTE : To check for whether a number(n) is a Fibonacii number or not , 
         check if    5*n*n-4 or 5*n*n+4    is a perfect square or not .
         if the condition is true , it is a fibonacci number , else not.*/

/*NOTE : GCD of nth, kth, ith..... fibonacci no.s is fibonacci(gcd(n,k,i,...))*/  

/*NOTE : Number of ways to write a number as sum of 1's and 2's is fibo(number+1)*/

Methods to get nth fibonacci no.
Method 1 : Memoization

Method 2 : Matrix exponentiation O(n)
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
long long fibo(long long n)
{
    if(n==0) return 0;                          //for 0 based indexing of fibonacci numbers
    
	long long fm[2][2]={1,1,1,0};              //[ fn+1 fn
	                                           //  fn   fn-1 ]    0 based indexing
	                                           
	                                           //this fm matrix raised to power n gives fibonacci(n)
	long long tm[2][2]={1,1,1,0};              
	
	for(long long i=2;i<=n;i++)
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
	return fm[0][1]%mod;                   //for 0 based indexing use fm[0][1] or fm[1][0]
	                                      //for 1 based indexing use fm[1][1]
}
main()
{
	int q;
	scanf("%d",&q);
	while(q--)
	{
            long long n;
		scanf("%lld",&n);
		printf("%lld\n",fibo(n));
	}
}

Method 3 : Optimised Matrix exponentiation O(log(n))
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
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

main()
{
	int q;
	scanf("%d",&q);
	long long n;
	cin>>n;
	long long gc=n;
	q=q-1;
	while(q--)
	{
		scanf("%lld",&n);
		gc=__gcd(gc,n);
	}
	printf("%lld\n",fibo(gc));
}

Method 4 : Recurrence in O(log(n)*loglog(n))
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long
map<ll,ll> fm;
ll fibo(ll n)
{
    if(fm.count(n)) return fm[n];               //check if fm[n] already calculated.
                                           //since map has unique values so it returns 1 or 0
    
    if(n==0) return (fm[n]=0);            
    if(n==1) return (fm[n]=1);           //base cases
    
    ll temp;
    if(n%2==0) temp=n/2;                
    else temp=(n+1)/2;                 //even or odd cases
    
    if(n%2==0) return fm[n]=((2*fibo(temp-1)+fibo(temp))*fibo(temp))%mod;
    else return       fm[n]=((fibo(temp-1)*fibo(temp-1)+fibo(temp)*fibo(temp)))%mod;
}

main()
{
	int q;
	scanf("%d",&q);
	long long n;
	cin>>n;
	long long gc=n;
	q=q-1;
	while(q--)
	{
		scanf("%lld",&n);
		gc=__gcd(gc,n);
	}
	printf("%lld\n",fibo(gc));
}
