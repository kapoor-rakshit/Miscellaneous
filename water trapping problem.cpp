#include <bits/stdc++.h>
using namespace std;
int main() {
	int n;
	scanf("%d",&n);
	while(n--)
	{
	    int m;
	    scanf("%d",&m);
	    int a[m];
	    int ans=0;
	    
	    int mx_height=INT_MIN;
	    int mx_height_index;
	    int temp=INT_MIN;
	    
	    for(int i=0;i<m;i++) 
	    {
	        scanf("%d",&a[i]);
	        if(a[i]>mx_height) 
	        {
	            mx_height=a[i];          //find max height wall
	            mx_height_index=i;
	        }
	    }
	    for(int i=0;i<mx_height_index;i++)
	    {
	        if(a[i]>temp) temp=a[i];       //traverse from starting to index
	        else ans+=temp-a[i];          //add the difference of (max_till_now-current_height)
	    }
	    for(int i=m-1;i>mx_height_index;i--)
	    {
	        if(a[i]>temp) temp=a[i];      //traverse from last to index
	        else ans+=temp-a[i];         //add the difference of (max_till_now-current_height)
	    }
	    printf("%d\n",ans);
	}
}
