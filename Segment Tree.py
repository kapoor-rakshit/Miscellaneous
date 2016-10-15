def build(low,high,pos):                    #build the segment tree (tree)
    if low==high:
        tree[pos]=a[high]
        return
    mid=(low+high)//2
    build(low,mid,2*pos+1)
    build(mid+1,high,2*pos+2)
    tree[pos]=(tree[2*pos+1]*tree[2*pos+2]) #operation here must be same of query
    
def update1(l,r,low,high,val,pos):          #update the tree with range multiplied with val
    if high<l or low>r:
        return
    if low==high:
        tree[pos]*=val
        return
    mid=(low+high)//2
    update1(l,r,low,mid,val,2*pos+1)
    update1(l,r,mid+1,high,val,2*pos+2)
    tree[pos]=(tree[2*pos+1]*tree[2*pos+2]) #operation here must be same of query
    
def update2(l,r,low,high,val,pos):          #update the tree with range replaced with val
    if high<l or low>r:
        return
    if low==high:
        tree[pos]=val
        return
    mid=(low+high)//2
    update2(l,r,low,mid,val,2*pos+1)
    update2(l,r,mid+1,high,val,2*pos+2)
    tree[pos]=(tree[2*pos+1]*tree[2*pos+2]) #operation here must be same of query
    
def query(l,r,low,high,pos):       
    if high<l or low>r:
        return 1
    if low>=l and high<=r:
        return  tree[pos]
    mid=(low+high)//2
    return(query(l,r,low,mid,2*pos+1)*query(l,r,mid+1,high,2*pos+2))
    
a=[]
tree=[]

n=int(input())
while n:
    an=0
    m,q=map(int,input().split())
    for i in range(0,10010,1):
        tree.append(0)
    a=list(map(int,input().split()))
    build(0,m-1,0)
    while q:
        b=list(map(int,input().split()))
        if b[0]==1:
            update1(b[1]-1,b[2]-1,0,m-1,b[3],0)
        elif b[0]==2:
            for i in range(0,b[2]-b[1]+1,1):
                update2(b[1]-1+i,b[1]-1+i,0,m-1,b[3],0)
        else:
            s=query(b[1]-1,b[2]-1,0,m-1,0)
            print(s)
        q=q-1
    n=n-1
 
