/*Check if a string is a subsequence of another string   O(n)*/

#include <bits/stdc++.h>
using namespace std;
char tobsearched[1001];
char searchfrom[1001];
int main() {
    
scanf("%s",tobsearched);
scanf("%s",searchfrom);

int l_tobsearched=strlen(tobsearched);
int l_searchfrom=strlen(searchfrom);

int matched_till_now=0;

for(int i=0; i<l_searchfrom && matched_till_now<l_tobsearched ;i++)
{
    if(tobsearched[matched_till_now]==searchfrom[i]) matched_till_now++;
}
if(matched_till_now==l_tobsearched) printf("Yes");
else printf("No");
}
