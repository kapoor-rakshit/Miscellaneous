#include <bits/stdc++.h>
using namespace std;
char upper(char a){
    if(a >= 97 && a<= 122){
        return (char)((int)a-32);
    }
    return a;
}
int main() {
    string s="",t;
    while((cin>>t)){
        s = s+t+' ';
    }
    s=s.substr(0,s.length()-1);
    int l=s.length();
    string out[100000];
    for(int i=0;i<100000;i++){
        out[i]="";
    }
    int p=0;
    int cur=0;
    int las=0;
    bool caps=false;
    for(int i=0;i<l;i++){
        if(s[i] == '@'){
            caps = !caps;
        }else if(s[i] == '#'){
            for(int j=las+1;j>=p+2;j--){
                out[j]=out[j-1];
            }
            string temp = out[p].substr(cur);
            out[p]=out[p].substr(0,cur);
            out[p+1]=temp;
            p++;
            cur=0;
            las++;
        }else if(s[i] == '<'){
            if(cur != 0){
                cur--;
            }else{
                if(p-1 >= 0){
                    cur = out[p-1].length();
                }
            }
        }else if(s[i] == '>'){
            if(cur != out[p].length()){
                cur++;
            }else{
                if(p+1 <= las){
                    cur=0;
                    p++;
                }
            }
        }else if(s[i] == '/'){
            if(cur != 0){
                out[p] = out[p].substr(0,cur-1) + out[p].substr(cur,out[p].length()-cur);
                cur--;
            }else if(p-1 >= 0){
                p--;
                cur=out[p].length();
                out[p] = out[p]+out[p+1];
                for(int j=p+2;j<=las;j++){
                    out[j-1]=out[j];
                }
                out[las]="";
            }
        }else if(s[i] == '?'){
            int count=1;
            for(int j=i+1;j<l;j++){
                if(s[j] == '?'){
                    count++;
                }else{
                    break;
                }
            }
            if(p != las){
                while(p+count > las){
                    count--;
                }
                if(cur > out[p+count].length()){
                    cur=out[p+count].length();
                }
                p+=count;
            }
            i=i+count-1;
        }else if(s[i] == '^'){
            int count=1;
            for(int j=i+1;j<l;j++){
                if(s[j] == '^'){
                    count++;
                }else{
                    break;
                }
            }
            if(p != 0){
                while(p-count < 0){
                    count--;
                }
                if(cur > out[p-count].length()){
                    cur=out[p-count].length();
                }
                p-=count;
            }
            i=i+count-1;
        }else{
            if(caps){
                s[i]=upper(s[i]);
            }
            int ll=out[p].length();
            string tt=out[p].substr(cur,ll-cur);
            string tt2=out[p].substr(0,cur);
            out[p] = tt2 + s[i] + tt;
            cur++;
        }
        las=max(las,p);
    }
    for(int i=0;i<=las;i++){
       if(true){
            cout<<out[i]<<"\n";
       }
    }
    return 0;
}
