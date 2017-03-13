import sys
n=int(input())
sz=sys.getsizeof(int)
res=0
for i in range(0,32,1):      #replace 32 with required size of bits
    temp=(1<<i)
    if temp&n:               #check if current bit of number is set(1)
        res|=(1<<(32-1-i))   #move this bit to desired position
print(res)        
