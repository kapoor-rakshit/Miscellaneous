n=int(input())
while n:
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as v:
        print("Error Code:",v)
    except ValueError as v:
        print("Error Code:",v)
    n=n-1
    
 #--------------------------------------OR------------------------------------
 try:
     print(int(a)//int(b))
 except (ZeroDivisionError, ValueError, NameError, TypeError, RuntimeError) as v:
     print("Error Code:",v)
 
#----------------------------------------OR------------------------------------
try:
    print(a/b)
except Exception as e:
    print(str(e))
        
