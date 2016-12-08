/*Source : GeeksforGeeks
To find maximum element in subarrays of all window sizes of a given array.*/

#include"bits/stdc++.h"
using namespace std;
void pre(int a[],int m);
void makeans(int l,int m,int *a);
int ans[5000001];
int ind=0;
main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int m;
        int q;
        ind=0;
        scanf("%d%d",&m,&q);
        int a[m];
        int mx=INT_MIN;
        for(int i=0; i<m; i++)
        {
            scanf("%d",&a[i]);
            ans[ind++]=a[i];      //includes element when subarray is a single element
            if(a[i]>mx) mx=a[i];
        }
        ans[ind++]=mx;           //includes element when subarray is complete array
        pre(a,m);
        sort(ans,ans+ind);
        reverse(ans,ans+ind);
        while(q--)
        {
            int pos;
            scanf("%d",&pos);
            printf("%d\n",ans[pos-1]);
        }
    }
}
void makeans(int l,int m,int *a)
{
    deque<int>dq;                                         //deque will have index of elements in decreasing order
    int i;
    for(i=0; i<l; i++)                                     //consider the first subarray (window) of size l
    {
        while(dq.empty()==false&&a[i]>=a[dq.back()]) dq.pop_back();
        //the front of the queue must be max of elements of window
        //so pop from back until we get max or queue is empty
        //as smaller elements are useless in that window

        dq.push_back(i);                                  //push index of max element from window
    }
    for(; i<m; i++)
    {
        ans[ind++]=a[dq.front()];                          //include front element ie max element from window
        while(dq.empty()==false&&i-dq.front()>=l) dq.pop_front();    //if that max element(front) is out of window range then pop it
        while(dq.empty()==false&&a[i]>=a[dq.back()]) dq.pop_back(); //pop till we get position of a[i] in queue
        dq.push_back(i);                                     //push index
    }
    ans[ind++]=a[dq.front()];
    dq.clear();
}
void pre(int a[],int m)
{
    for(int l=2; l<m; l++) makeans(l,m,a);                   //includes elements when subarray is of size 2 3 4 5 6 7 ...m-1
}
