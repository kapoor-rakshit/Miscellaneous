from collections import *
n=int(input())
d=OrderedDict()                                  #An ordered dictionary to return items in the order which they appear

for i in range(0,n,1):
    a=input()
    a=a.rpartition(' ')                         #1) Partition from right with separator specified (necessary) 2) returns a tuple
    d[a[0]]=d.get(a[0],0)+int(a[len(a)-1])      #get() method returns the specified key value or default if key not found ie get(key, default) 
    
for i,j in d.items():                          #Returns key , value pair
    print(i,j)
