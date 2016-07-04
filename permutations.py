from itertools import permutations
a=input()                                        #RAKSHIT 3 ie the string need to be permuted with the length 3
l=a.split(' ')
b=sorted(list(permutations(l[0],int(l[1]))))     # if second argument is empty im permutations(,) it gives permutations of length of string
for i in range(0,len(b),1):
    print(*b[i],sep="")

