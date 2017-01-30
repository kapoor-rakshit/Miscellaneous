/*Overall complexity is O(N^(1/3))
We write N as product of three numbers P, Q and R. P*Q*R=N, where P<=Q<=R and Max value of P is N^(1/3)
We can loop over all prime numbers in range [2,N^(1/3)] and try to reduce N to it's prime factorisation,
which would help us count the number of factors of N.

To know how to calculate divisors using prime factorisation : 
We begin by writing the number as a product of prime factors: n = p^a * q^b * r^c...
then the number of divisors, d(n) = (a+1)(b+1)(c+1)...

We will split our number N into two numbers X and Y such that X * Y = N. Further, X contains only prime factors in range [2,N^(1/3)].
Y deals with higher prime factors (>N^(1/3)). Thus, gcd(X , Y) = 1. 
Let the count of divisors of a number N be denoted by the function F(N). 
It is easy to prove that this function is multiplicative in nature, i.e., F(m * n) = F(m) * F(n), if gcd(M,N) = 1. 
So, if we can find F(X) and F(Y), we can also find F(X * Y) or F(N) which is the required quantity.
For finding F(X), we use the naive trial division to prime factorise X and calculate the number of factors. 
Once this is done, we have Y = N / X remaining to be factorised. There are only three cases which will cover all possibilities of Y :

Y is a prime number : F(Y) = 2.
Y is square of a prime number : F(Y) = 3.
Y is product of two distinct prime numbers : F(Y) = 4.

If Y is a prime it will have 2 divisors: 1 and y itself. 
If Y is a square of a prime it will have 3 divisors: 1, sqrt(y) and y itself. 
If Y is a product of two distinct primes(suppose p1, p2) it will have 4 divisors: 1, p1, p2 and y itself which is equal to p1*p2.

We have only these three cases since there can be at max two prime factors of Y. 
If it would have had more than two prime factors, one of them would surely have been <=N^(1/3),
hence it would be included in X and not in Y.
*/

#include <bits/stdc++.h>
#define LL long long
using namespace std;

#define MAXN 1000003

bool is_prime[MAXN] = {false};
vector<LL> primes;
void sieve_eratosthenes() {
	for(int i = 0; i < MAXN; i++)	is_prime[i] = true;
	is_prime[1] = false;
	for(int i = 2; i*i <= MAXN; i++){
		if(is_prime[i]){
			for(int j = i*i; j < MAXN; j += i){
				is_prime[j] = false;
			}
		}
	}
	for(int i = 2; i < MAXN; i++)
		if(is_prime[i])
			primes.push_back(i);
}

/* Miller Rabbin,
 * Complexity: O(k * log2^3(n))
 * * * * * * * * * * * */
inline LL multiply(LL a, LL b, const LL &m) {
	a %= m, b %= m; 
	long double res = a;res *= b;
	LL c = (LL)(res/m); 
	a *= b, a -= c*m, a %= m;
	if(a < 0)	
		a += m; 
	return a;
}

inline LL power(LL a, LL b, const LL &m) {
	LL ans = 1;  
	while(b) {
		if(b & 1) {
			ans = multiply(ans, a, m);
		}
		a = multiply(a, a, m);
		b >>= 1;
	}
	return ans;
}

// Returns true if p is prime
inline bool Miller(LL p) {
	if(p < 2)	return false;  
	if(p != 2 && !(p&1))	return false;
	int cnt = 0;
	LL s = p-1;
	while(!(s&1)) {
		s /= 2;  
		cnt++;
	}
	LL accuracy = 2, m;
	for(int i = 0; i < accuracy; i++) {
		LL a = rand() % (p-1) + 1;
		m = p;
		LL x = power(a, s, m);
		if(x == 1 || x == p-1)	continue;
		int flag = 0;
		for(int i = 1; i < cnt; i++) {
			x = multiply(x, x, m);  
			if(x == 1)	return false;
			if(x == p-1) {
				flag = 1;  
				break;
			}
		}
		if(flag)	continue;
		return false;
	}
	return true;
}
LL count_divisors(LL n)
{
	LL ans = 1;
	int sze=primes.size();
	for(int i=0;i<sze;i++) {
	     LL p=primes[i];
		if(p*p*p > n)	break;
		LL count = 1;
		while(n % p == 0) {
			n /= p;
			count++;
		}
		ans = ans*count;
	}
	LL sq = sqrt(double(n));
	if(Miller(n)) {
		ans = ans*2;
	}
	else if(sq*sq == n && Miller(sq)) {
		ans *= 3;
	}
	else if(n != 1) {
		ans *= 4;
	}
	return ans;
}

int main() {
    sieve_eratosthenes();
    LL n;
    cin >> n;
    cout << count_divisors(n) << endl;
    return 0;
}
