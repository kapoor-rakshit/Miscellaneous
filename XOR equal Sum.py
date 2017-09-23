# given n find the count of x where n^x == n+x   such that  0<=x<=n

n=int(input())

l=0                                
setbits=0                           # setbits in binary str
nagain=n

while n:
	if n&1:
		setbits+=1
	n=n>>1
	l+=1                           # length of binary str

# Brian Kernighan’s Algorithm for checking set bits   O(logn)

# Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set bit(including the righmost set bit).
# So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the righmost set bit. 
# If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
# Beauty of the this solution is number of times it loops is equal to the number of set bits in a given integer.

setbitsagain=0

while nagain:
	nagain=nagain&(nagain-1)
	setbitsagain+=1


# Considering the unset bits coz XOR is a binary addition without carry so 0 in n would make no change in the addition result.
# whereas 1 in n causes the corresponding bit in x to be 0 for no change in addition result , which is not always the case.
# so corresponding to 0 in n we have 2 possibilities , hence pow(2,unsetbits_in_n).   

unsetbits=l-setbitsagain
print(1<<unsetbits)