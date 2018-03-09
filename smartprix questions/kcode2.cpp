#include<bits/stdc++.h>
using namespace std;
bool caps=false;
int rtl=0;
void character(vector<string>&te,char s,int curr_row)
{

	if(caps and (s>=97 and s<=122))
	{
		te[curr_row].push_back((char)(s-32));
	}
	else if(caps and (s>=65 and s<=90))
	{
		te[curr_row].push_back((char)(s+32));
	}
	else
	te[curr_row].push_back(s);
}
int main()
{

	string str;
	getline(cin,str);
	int len=str.length();
	int curr_row=0;
	vector<string>te;
	te.push_back("");
	string tmp;
	for(int i=0;i<len;i++)
	{
		if(str[i]<='z'&& str[i]>='a'||str[i]>='A'&& str[i]<='Z')
		{
			character(te,str[i],curr_row);
			
		}
		else if(str[i]>='0'&& str[i]<='9')
		{
			
			te[curr_row].push_back(str[i]);
		}
		else if(str[i]=='#')
		{
			int curr_l;
			if(str[i-1]=='#' && i!=0)
			 curr_l=te[curr_row].size();
            else
             curr_l=te[curr_row].size()-1;
            tmp="";
            for(int j=0;j<curr_l;j++)
            tmp+=" ";
			curr_row++;
			te.insert(te.begin()+curr_row,tmp);
		}
		else if(str[i]=='/')
		{
			if(te[curr_row].length())
			//te[curr_row].pop_back();
			if(te[curr_row].length()==0 && te.size()>1)
			{
				te.erase(te.begin()+curr_row);
				curr_row--;
			}
		}
		else if(str[i]=='?' && i!=len-1)
		{	
                tmp="";
				curr_row++;
				te.insert(te.begin()+curr_row,tmp);
				
		}
		else if(str[i]=='^' && i!=0)
		{
			if(curr_row!=0)
			curr_row--;
		}
		
		else if(str[i]=='@')
		{
			caps=!caps;
		}
	}
    int kk=te.size();
	for(int i=0;i<kk;i++)
	{
		cout<<te[i]<<endl;
	}
   
}
