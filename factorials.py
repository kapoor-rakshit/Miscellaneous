"""Python implementation to find factorial of a number as large as 100"""

from math import *
n=int(input())
print(factorial(n))


"""C/CPP Implementation of finding factorials.
We need to write additional code to handle big integer values. We can store the factorials in an array with one digit at each index of the array. 
For example : To store 245 in the array, a[2]=2, a[1]=4, a[0]=5. To multiply a number say k to this value, we start off from the index 0 of the array. 
At every iteration, we calculate k * a[index]. 
We also maintain a carry from the previous index which is initialized to 0. 
Now, at every step, we calculate product = a[index] * k + carry. 
The new value of a[index] will be product % 10 and the new value of carry will be product/10. 
We propogate this carry to higher order digits."""

#include "bits/stdc++.h"
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> ans(200,0);             //initialise array with 0
    ans[0]=1;                          //initial product
    int ind=0;                        //initial size
    int carry=0;
    for(int i=1;i<=n;i++)
        {
        for(int j=0;j<=ind;j++)
            {
            ans[j]=ans[j]*i+carry;
            carry=ans[j]/10;
            ans[j]=ans[j]%10;
        }
        while(carry)                  //propagate carry to higher index of answer
            {
            ind++;
            ans[ind]=carry%10;
            carry/=10;
        }
    }
    for(int i=ind;i>=0;i--) printf("%d",ans[i]);
}
