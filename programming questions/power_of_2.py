n=int(input())
temp=n
n=n-1                                 # toggle bits after rightmost set bit including rightmost set bit

                                      # set all bits after the leftmost set bit
                                      # here it works for 32 bit number as max shift done is 16
n = n | (n >> 1)
n = n | (n >> 2)
n = n | (n >> 4)
n = n | (n >> 8)
n = n | (n >> 16)

n=n+1

print(n)                               # power of two GREATER or EQUAL than n
print(n<<1 if temp==n else n)          # power of two GREATER than n
print(n>>1)                            # power of two LESS than n

