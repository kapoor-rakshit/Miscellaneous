/*Source : https://deepanshubhatti.blogspot.in/2015/12/matrix-rotation-anticlockwise.html*/

#include<bits/stdc++.h>
int l,m,Row,Col,mat[300][300];
void rotation(int l, int m, int Row, int Col)
{
       int si,sj,i,j,t,f;
       si = l;
       sj = m;
      
       t = mat[l][m];
      
       for(i=l+1;i<=Row;i++)
       {
              f = mat[i][m];                 //act on first column in a set matrix
              mat[i][m] = t;
              t = f;
       }
       l++;
       for(i=m+1;i<=Col;i++)
       {
              f = mat[Row][i];
              mat[Row][i] = t;             //act on last row in a set matrix
              t = f;
       }
       m++;
       if(l-1 < Row)
       {
              for(i=Row-1;i>=l-1;i--)
              {
                     f = mat[i][Col];     //act on last column in a set matrix
                     mat[i][Col] = t;
                     t = f;
              }
       }
       if(m-1 < Col)
       {
              for(i=Col-1;i>=m;i--)
              {
                     f = mat[l-1][i];
                     mat[l-1][i] = t;    //act on first row in a set matrix
                     t = f;
              }                         
       }
       mat[si][sj] = t;
       return;
}


int main()
{
       int r,c,k,i,j;
       scanf("%d%d%d",&r,&c,&k);
       int f,K;
       for(i=0;i<r;i++)
       {
              for(j=0;j<c;j++)
              {
                     scanf("%d",&mat[i][j]);
              }
       }
       l = 0;
       m = 0;
       Row = r-1;
       Col = c-1;
       while(l < Row && m < Col)
       {
              int rot = 2*(Row-l)+2*(Col-m);         //total no. of elements to act upon
              
              f = k%rot;                            //rotations=rotations % elements
              
              for(i=1;i<=f;i++)
              {
                     rotation(l,m,Row,Col);
              }
              l++;
              m++;
              Row--;
              Col--;
       }     
       for(i=0;i<r;i++)
       {
              for(j=0;j<c;j++)
              {
                     printf("%d ",mat[i][j]);
              }
              printf("\n");
       }
    return 0;
}
