from collections import Counter

n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
d = Counter(a)
q = int(input())

while q:
    t,v = map(int,input().split())
    beg = 0
    end = n-1
    mid = (beg + end)//2                  # to search for greater than or equal to key
    while beg<=end and a[mid]!=v:
        if a[mid]>v:                      # move left if mid greater than key
            end = mid-1
        else:                             # move right if mid is less than key
            beg = mid + 1
        mid = (beg + end)//2
    if a[mid]==v:                         # remove dupliactes to have pos of first occurrence
        while mid>=0 and a[mid]==v:
            mid-=1
    if t==0:                               # elements greater than or equal to key 
        print(n-mid-1)
    else:                                  # elements greater than key
        print(n-mid-d[v]-1 if v in d.keys() else n-mid-1)
    q = q-1
    
    
