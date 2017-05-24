#include<stdio.h>
int main()
{
    FILE *fp,*fpp;
    char ch;
    char tempfreq[10];
    int i;
    for(i=0; i<10; i++) tempfreq[i]='\0';
    int ind=0;
    fp = fopen("dummy.txt", "r");
    fpp=fopen("lpf_ANKIT.txt","w");
    while((ch = getc(fp))!=EOF)
    {
        if(ch=='\n')
        {
            int flg=0;
            double freq=0;
            int decind=0;
            if(tempfreq[0]=='-') flg=1;
            for(i=0; i<ind; i++)
            {
                if(tempfreq[i]!='-' && tempfreq[i]!='.') freq=freq*10+(tempfreq[i]-48);
            }
            for(i=0; i<ind; i++) if(tempfreq[i]=='.')
                {
                    decind=i;
                    break;
                }
            int tenpower=1;
            for(i=1; i<=ind-1-decind; i++) tenpower*=10;
            freq=freq/(double)tenpower;
            if(flg) freq=freq*-1;
            if(freq<=(double)10) fprintf(fpp,"%lf\n",freq);
            ind=0;
        }
        else tempfreq[ind++]=ch;
    }

    fclose(fp);
    fclose(fpp);
}
