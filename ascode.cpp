#include<bits/stdc++.h>
using namespace std;
map<string,int>var;
void sett(string s,string ss){
    if(var.find(ss) != var.end()){
        var[s]=var[ss];
    }else if(ss[0]>=48 && ss[0]<=57){
        var[s]=stoi(ss);
    }else{
        var[s]=0;
    }
}
void add(string a,string b,string c){
        if(var.find(a) != var.end()){
            var[c] = var[a];
        }else{
            var[c] = stoi(a);
        }
        if(var.find(b) != var.end()){
            var[c] += var[b];
        }else{
            var[c] += stoi(b);
        }
}
void echho(string s){
    if(var.find(s) != var.end()){
        cout<<var[s]<<"\n";
    }else if(s[0] >= 48 && s[0]<= 57){
        cout<<s<<"\n";
    }else{
		cout<<"0\n";
	}
}
int main(){
    string code[1000][4],s,a,b,c;
    int p=0;
    map<string,int>label;
    while((cin>>s)){
        if(s == "SET"){
            cin>>a>>b;
            code[p][0]=s;
            code[p][1]=a;
            code[p][2]=b;
        }else if(s == "ECHO"){
            cin>>a;
            code[p][0]=s;
            code[p][1]=a;
        }else if(s == "EXIT"){
            code[p][0]=s;
        }else if(s == "ADD"){
            cin>>a>>b>>c;
            code[p][0]=s;
            code[p][1]=a;
            code[p][2]=b;
            code[p][3]=c;
        }else if(s == "LABEL"){
            string val;
            cin>>val;
            label[val]=p;
        }else if(s == "GOTO"){
            string val;
            cin>>val;
            code[p][0]=s;
            code[p][1]=val;
        }else if(s == "IF"){
            cin>>a>>b;
            code[p][0]=s;
            code[p][1]=a;
            code[p][2]=b;
        }else if(s == "END"){
            code[p][0]=s;
			
        }else if(s == "CONTINUE"){
            code[p][0]=s;
        }
        if(s != "LABEL")
        p++;
    }
    int n=p;
   	p=0;
    stack<bool>flagg;
    int curif;
	stack<int>stc;
	flagg.push(true);
    while(p < n){
        s=code[p][0];
		bool flag=flagg.top();
		//cout<<s<<"  "<<flag<<"\n";
        if(s == "SET" && flag){
            sett(code[p][1],code[p][2]);
            p++;
        }else if(s == "ECHO" && flag){
            echho(code[p][1]);
            p++;
        }else if(s == "EXIT" && flag){
            return 0;
        }else if(s == "ADD" && flag){
            add(code[p][1],code[p][2],code[p][3]);
            p++;
        }else if(s == "GOTO" && flag){
            p = label[code[p][1]];
        }else if(s == "IF"){
			int ty,yu;
			if(!flag){
				flagg.push(false);
			}else{
            	if(var.find(code[p][2]) != var.end()){
                	yu=var[code[p][2]];
            	}else if(code[p][2][0] >= 48 && code[p][2][0] <= 57){
                yu=stoi(code[p][2]);
            	}else{
					yu=0;
				}
            	if(var.find(code[p][1]) != var.end()){
                	ty=var[code[p][1]];
            	}else if(code[p][1][0] >= 48 && code[p][1][0] <= 57){
                	ty=stoi(code[p][1]);
            	}else{
					ty=0;
				}
            	if(ty != yu){
                	flagg.push(false);
            	}
			}
            stc.push(p);
            p++;
		}else if(s == "END"){
			flagg.pop();
			if(flagg.empty()){
				flagg.push(true);
			}
            p++;
			stc.pop();
        }else if(s == "CONTINUE" && flag){
            p=stc.top();
        }else{
            p++;
        }
    }
    return 0;
}
