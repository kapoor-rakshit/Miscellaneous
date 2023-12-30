#include<bits/stdc++.h>
char a[1000];
main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int ec=0,oc=0;
        int hash[26]= {0};
        scanf("%s",a);
        int l=strlen(a);

        for(int i=0; i<l; i++)
            hash[a[i]-97]++;                                    //make hash of each character

        for(int i=0; i<26; i++)
        {
            if(hash[i]%2==0&&hash[i]!=0)
                ec+=hash[i];                                   //count the characters in pairs||quads||....etc.
            else
                oc+=hash[i];                                   //count not in pairs||quads....etc.
        }
        if(l%2==0)
        {
            if(l-ec==0)
            {
                printf("YES\n");                              //eg:-aaaabbbb
                continue;
            }
        }

        else
        {
            if(l-ec==1||l-oc==0)
            {
                printf("YES\n");                             //eg:-aabhaab     eg:-aaa
                continue;
            }

        }
        printf("NO\n");                                      //eg:-aaaaaaaaaaaaanm
    }
}
