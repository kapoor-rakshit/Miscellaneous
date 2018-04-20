"""
IOError : python cannot be opened
ImportError : cannot find module
KeyboardInterrupt : user hits interrupt key (ctrl + c)
ValueError : inappropriate value to operation/function
EOFError : when operation (input()) receives EOF
"""

"""
try...
except...
else...          # if exception donot occur in try block, else executes
finally...       # executes irrespective of occurrence of exception

"""

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
        

        
# RAISE statement, user defined exceptions

class Error(Exception):
    """Base class for other exceptions"""
    pass

class vallarge(Error):
    """raised when 'raise vallarge' called"""
    pass

class valsmall(Error):
    """raised when 'raise valsmall' called"""
    pass

try:
    if val<10:
        raise valsmall
    elif val>10:
        raise vallarge
except valsmall:
    print("val is small")
except vallarge:
    print("val is large")



# ASSERT statement                # to check correctness of statement/operation

assert <condition> , "message"    # raises Assertionerror as assert statement evals to False

