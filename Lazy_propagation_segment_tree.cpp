/*Approach is to stop at the total overlap node and return, simulataneously maintain a lazy tree.
  Use the lazy tree in both update and query functions to optimize segment tree where we need to traverse till the leaf node*/

#include<bits/stdc++.h>
using namespace std;
long long a[1000010];
long long tree[1000010];
long long lazy[1000010];
void build(int low,int high,int pos)
{
	if(low==high) {tree[pos]=a[high];return;}
	int mid=(low+high)/2;
	build(low,mid,2*pos+1);
	build(mid+1,high,2*pos+2);
	tree[pos]=min(tree[2*pos+1],tree[2*pos+2]);          //here the operation is equal to query operation (here min)
}
void update(int low,int high,int l,int r,long long val,int pos)
{
	if(lazy[pos]!=0)                                       //check for lazy tree node, if not zero then first operate that value on segtree node 
	{
		tree[pos]+=lazy[pos];                //here the operation is equal to update operation (here val is to be added,so + )
		if(low!=high)
		{
			lazy[2*pos+1]+=lazy[pos];                    //operate the lazy node value to its children, indicating that the children are not uptodate
			lazy[2*pos+2]+=lazy[pos];                   //and if required in future, will be updated with reference from lazy tree
		}
		lazy[pos]=0;                                //make current node updated 
	}
	if(high<l||low>r) return;
  
	if(low>=l&&high<=r)                          //complete overlap so, stop here and operate value to segtree 
	{
		tree[pos]+=val;                    //here the operation is equal to update operation (here val is to be added,so + )
		if(low!=high)
		{
			lazy[2*pos+1]+=val;                    //operate the value to children in lazy tree, so that can be referred in future
			lazy[2*pos+2]+=val;
		}
		return;
	}
	int mid=(low+high)/2;
	update(low,mid,l,r,val,2*pos+1);
	update(mid+1,high,l,r,val,2*pos+2);               
	tree[pos]=min(tree[2*pos+1],tree[2*pos+2]);   //here the operation is equal to query operation (here min)
}
long long query(int low,int high,int l,int r,int pos)
{
	if(lazy[pos]!=0)
	{
		tree[pos]+=lazy[pos];              //here the operation is equal to update operation (here val is to be added,so + )
		if(low!=high)
		{
			lazy[2*pos+1]+=lazy[pos];  //here the operation is equal to update operation (here val is to be added,so + )
			lazy[2*pos+2]+=lazy[pos];
		}
		lazy[pos]=0;
	}
if(high<l||low>r) return INT_MAX;
if(low>=l&&high<=r) return tree[pos];
int mid=(low+high)/2;
return min(query(low,mid,l,r,2*pos+1),query(mid+1,high,l,r,2*pos+2)); //here the operation is equal to query operation (here min)
}
main()
{
	int n,q;
	scanf("%d%d",&n,&q);
	for(int i=0;i<n;i++) scanf("%lld",&a[i]);

	build(0,n-1,0);

	while(q--)
	{
		int t,l,r;
		scanf("%d%d%d",&t,&l,&r);
		l=l-1;
		r=r-1;
		if(t==1)
		{
			long long val;
			scanf("%lld",&val);
			update(0,n-1,l,r,val,0);
		}
		else
		{
			long long mn;
			mn=query(0,n-1,l,r,0);
			printf("%lld\n",mn);
		}
	}
}
