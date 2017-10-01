#include<bits/stdc++.h>
using namespace std;

int findCase(string &b,int index)
{
    if(index+2>=b.size())
        return 1;
    /*
    if(b[index+2]!=':' && b[index+2]!='[')
        return 1;
    */

    if(b[index+2]==':' && index+3<b.size() && b[index+3]>='0' && b[index+3]<='9')
        return 4;
    if(b[index+2]==':')
        return 0;

    if(b[index+2]=='[')
    {
        int i=index+3;
        if(i>=b.size() || b[i]<='0' || b[i]>='9')
            return 0;
        while(i<b.size() && b[i]>='0' && b[i]<='9')
            i++;
        if(i==b.size())
            return 0;           // for case %s[1234
        else if(b[i]==']')
        {
            if(i+1>=b.size() || b[i+1]!=':')
                return 2;
            else if(b[i+1]==':')
            {
                if(i+2>=b.size())
                    return 0;
                else if(b[i+2]>='0' && b[i+2]<='9')
                    return 3;
                else
                    return 0;
            }
        }
        else return 1;
    }
    return 1;
}
int extract(string &b,int index)
{
    int sum=0;
    while(index<b.size() && b[index]>='0' && b[index]<='9')
    {
        sum=sum*10+b[index]-'0';
        index++;
    }
    return sum;
}
void findFormattedString(string &a,string &b)
{
    vector<string>vs;
    int start=0;int len=0;
    for(int i=0;i<a.size();i++)
    {
        if(a[i]==' ')
        {
            vs.push_back(a.substr(start,len));
            while(i<a.size() && a[i]==' ')
                i++;
            start=i;
            len=0;
        }
        len++;
    }
    if(a[a.size()-1]!=' ')
        vs.push_back(a.substr(start,a.size()-start));

    /*
    for(int i=0;i<vs.size();i++)
        cout<<"**"<<vs[i]<<endl;
    */
    int counter=0,startfrom=0;
    while(1)
    {
        int index=b.find("%s",startfrom);
        if(index<0)
            break;
        int c=findCase(b,index);
        if(c==1)
        {
            if(counter>=vs.size())
            {
                startfrom=index+1;
                continue;
            }
            b.erase(b.begin()+index,b.begin()+index+2);
            b.insert(index,vs[counter]);
            counter++;
        }
        else if(c==2)
        {
            int number=extract(b,index+3);
            if(number<0 || number>=vs.size())
            {
                startfrom=index+1;
                continue;
            }
            int i=index+3;
            while(i<b.size() && b[i]>='0' && b[i]<='9')
                i++;
            b.erase(b.begin()+index,b.begin()+i+1);
            b.insert(index,vs[number]);
        }
        else if(c==3)
        {
            int number1=extract(b,index+3);
            if(number1<0 || number1>=vs.size())
            {
                startfrom=index+1;
                continue;
            }
            int i=index+3;
            while(i<b.size() && b[i]>='0' && b[i]<='9')
                i++;
            b.erase(b.begin()+index,b.begin()+i+2);

            int number2=extract(b,index);
            i=index;
            while(i<b.size() && b[i]>='0' && b[i]<='9')
                i++;
            b.erase(b.begin()+index,b.begin()+i);

            if(vs[number1].size()<=number2)
            {
                b.insert(index,vs[number1]);
            }
            else
                b.insert(index,vs[number1].substr(0,number2));
        }
        else if(c==4)
        {
            if(counter>=vs.size())
            {
                startfrom=index+1;
                continue;
            }
            int number=extract(b,index+3);
            int i=index+3;
            while(i<b.size() && b[i]>='0' && b[i]<='9')
                i++;
            b.erase(b.begin()+index,b.begin()+i);
            if(vs[counter].size()<=number)
            {
                b.insert(index,vs[counter++]);
            }
            else
                b.insert(index,vs[counter++].substr(0,number));
        }
        else if(c==0)
            startfrom=index+1;
    }
}
int main()
{
    string a,b;
    getline(cin,a);
    getline(cin,b);
    findFormattedString(a,b);
    cout<<b<<endl;
    return 0;
}
