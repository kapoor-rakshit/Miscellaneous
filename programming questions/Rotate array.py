def leftrotate():
    reverse(0,op-1)          #reverse first op elements
    reverse(op,n-1)          #reverse remaining elements
    reverse(0,n-1)           #revese entire list

def rightrotate():
    reverse(n-op,n-1)        #reverse last op elements
    reverse(0,n-op-1)        #reverse remaining elements
    reverse(0,n-1)           #reverse entire list
    
def reverse(start,end):
    tp=0
    while start<end:          #function to reverse
        tp=a[start]
        a[start]=a[end]
        a[end]=tp
        start+=1
        end-=1
    
n=int(input())
a=list(map(int,input().split()))
op=int(input())              #no. of rotations
op=op%n                      #if rotations are greater than no. of elements

rightrotate()                #call to rightrotate
print(*a)

#leftrotate()
#print(*a)                   #call to leftrotate
