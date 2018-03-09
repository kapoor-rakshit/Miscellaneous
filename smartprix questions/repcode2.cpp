#include<bits/stdc++.h>
using namespace std;
vector<string>va,vb,vc;
int main()
{
    string a,b;
    getline(cin,a);
    getline(cin,b);
    int la=a.size();
    int lb=b.size();
    string tmpa="";
    string tmpb="";
    for(int i=0;i<la;i++)
    {
        if(a[i]==' ')
        {
            va.push_back(tmpa);
            tmpa="";

        }
        else{
            tmpa+=a[i];
        }
    }
    va.push_back(tmpa);
    for(int i=0;i<lb;i++)
    {
        if(b[i]==' ')
        {
            vb.push_back(tmpb);
            tmpb="";

        }
        else{
            tmpb+=b[i];
        }
    }
    vb.push_back(tmpb);
    int lvb=vb.size();
    int j=0;
    for(int i=0;i<lvb;i++)
    {
        if(vb[i]=="{}")
        {
            vc.push_back(va[j]);
            j++;
        }
       else if(vb[i][0]=='{'){
        if(vb[i][1]>='0' and vb[i][1]<='9'){
            int k=1;
            string numstr="";
            while(vb[i][k]!='}') {numstr+=vb[i][k];k++;}
            int aind=stoi(numstr);
            vc.push_back(va[aind]);
        }
        else if(vb[i][1]>='a' and vb[i][1]<='z'){
            int k=1;
            string numstr="";
            while(vb[i][k]!='}') {numstr+=vb[i][k];k++;}
            vc.push_back(numstr);
        }
       }
        else{
            vc.push_back(vb[i]);
        }
    }
    int lvc=vc.size();
    for(int i=0;i<lvc;i++)
        cout<<vc[i]<<" ";
}
