# given N find count of values x such that     N ^ x > N        and    0 < x < N

n=int(input())
while n:
	a=int(input())
	temp=a

	a=a-1
	a|=a>>1
	a|=a>>2
	a|=a>>4
	a|=a>>8
	a|=a>>16
	a+=1                                       # get next power of two

	if temp==a:
		ans=(1<<a)-1-temp                      # get all set bits in bitlength of N and subtract count of values that are less
	else:
		ans=a-1-temp
	print(ans)

	n=n-1
