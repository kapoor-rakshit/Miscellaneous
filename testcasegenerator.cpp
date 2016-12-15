#include<bits/stdc++.h>
#define ll long long
using namespace std;
vector<string> a;
/*void generate1()
{
	int has[1001]={0};
	
	for(int i=0;i<26;i++)
	{
		int l;
		while(1)
		{
			 l=1+rand()%1000;
			if(has[l]==0)                       //to prevent rand() from generating same values.
				break;
		}
		has[l]=1;
		cout<<l<<" ";
	}
	cout<<endl;
}*/
void generate()
{
	ll vl=1+rand()%10000000000;
	ll gl=1+rand()%10000000000;
	cout<<vl<<" "<<gl<<endl;
	int c=rand()%2;
	cout<<a[c]<<endl;
}
	
	
int main()
{
	freopen("inputankurstrings.txt","w",stdout);
a.push_back("Granny");
a.push_back("Vidhi");
	int t=1000;
	cout<<t<<endl;
	for(int i=0;i<t;i++)
	{
		generate();
	}
}
