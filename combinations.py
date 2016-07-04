
"""print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]"""

from itertools import combinations
a=input()
l=a.split(' ')
b=[]
l[0]=sorted(str(l[0]))
for i in range(int(l[1])-1,-1,-1):                                   
    b.append((list(combinations((l[0]),int(l[1])-i))))
    
for i in range(0,len(b),1):
    for j in range(0,len(b[i]),1):
        print(*b[i][j],sep="")
    
    
    
""""print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]"""

from itertools import combinations_with_replacement
a=input()
l=a.split()
l[0]=sorted(l[0])
l[1]=int(l[1])
b=list(combinations_with_replacement(l[0],l[1]))
for i in range(0,len(b),1):
    print(*b[i],sep="")
