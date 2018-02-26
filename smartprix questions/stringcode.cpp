#include<bits/stdc++.h>
using namespace std;
vector<string> user_fn_queries;
string userfn="";
string function_handler(string);
bool starts_with(string str)
{
    int j=strncmp(str.c_str(), userfn.c_str(), userfn.length());
    if(j==0)
        return true;
    else
        return false;
}
string user_function_handler(string s)
{
    
    string temp=s;
    for(int i=0; i<user_fn_queries.size(); i++)
    {
        string temp1="\"";
        temp1+=temp;
        temp1+="\"";
        temp=temp1;
        string tempStr=user_fn_queries[i];
        int j=0;
        int k=tempStr.length()-3;
        tempStr=tempStr.substr(0, k);
        while(temp[j]!='\0')
        {
            tempStr+=temp[j];
            j++;
        }
        temp=function_handler(tempStr);
        
    }
    return temp;
}
string toupper(string str)
{
    for(int i=0; i<str.length(); i++)
        str[i]=toupper(str[i]);
    return str;
}
string tolower(string str)
{
    for(int i=0; i<str.length(); i++)
        str[i]=tolower(str[i]);
    return str;
}
string reverse(string str)
{
    for(int i=0; i<str.length()/2; i++)
        swap(str[i], str[str.length()-1-i]);
    return str;
}
string function_handler(string str)
{
    if(str[0]=='\"')
    {
        string temp="";
        int i=1;
        while(str[i]!='\"')
            temp+=str[i++];
        //cout<<"Returning the string as "<<temp<<endl;
        return temp;
    }
	else if(str.substr(0, 5)=="print")
	{

		return function_handler(str.substr(6));
	}
	else if(str.substr(0,7)=="toupper")
	{
		 return toupper(function_handler(str.substr(8)));
	}
	else if(str.substr(0,7)=="tolower")
	{
		return tolower(function_handler(str.substr(8)));
	}
	else if(str.substr(0,8)=="append_a")
	{
		return function_handler(str.substr(9))+"a";
	}
	else if(str.substr(0,7)=="reverse")
	{
		return reverse(function_handler(str.substr(8)));
	}
	else if(starts_with(str))
    {
        return user_function_handler(function_handler(str.substr(userfn.length()+1)));
    }
}
int main() {
    string s;
	char ch='a';
	//get the input until the end of file and store it in s.
	while(ch=getchar())
	{
		if(ch==EOF)
			break;
		else
			s+=ch;
	}
	s[s.length()]='\0';
	//cout<<"Given input: "<<s<<endl<<endl;
	vector<string> queries;
	for(int i=0; i<s.length(); i++)
	{
		string temp="";
		while(i<s.length()&&s[i]!='\n'&&s[i]!='\0')
		{
			temp+=s[i];
			i++;
		}
		//cout<<"Pushing query: "<<temp<<endl;
		queries.push_back(temp);
	}
	int funcStart=INT_MAX, funcEnd=INT_MIN;
	for(int i=0; i<queries.size(); i++)
	{
		if(queries[i].substr(0, 6)=="define")
        {
			funcStart=i;
			int j=7;
			while(queries[i][j]!=' '&&queries[i][j]!='\0'){
                userfn+=queries[i][j++];
                //cout<<userfn<<endl;
			}
            //userfn[j-7]='\0';
        }
		else if(queries[i]=="end")
			funcEnd=i;
	}
	//cout<<"\nuser fn name is: "<<userfn<<endl;
	for(int i=funcStart+1; i<funcEnd; i++)
    {
        user_fn_queries.push_back(queries[i]);
    }
	for(int i=0; i<queries.size(); i++)
	{
		if(i<funcStart||i>funcEnd)
		{
		    //cout<<"Calling function_handler with query "<<queries[i]<<endl;
			cout<<function_handler(queries[i])<<endl;
		}
	}
    return 0;
}
