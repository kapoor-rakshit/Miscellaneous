# *tupleofargs is used to send a non-keyworded variable length argument tuple to the function.
# **dictofargs allows you to pass keyworded variable length of arguments to a function. 
# Use **dictofargs if you want to handle named arguments in a function.

# IMPORTANT : Order of using *args **kwargs and formal args is
# some_func(farg1,farg2,*args,**kwargs)


def first(*tupleofargs,**dictofargs):
    an=1
    for i in tupleofargs:
        an/=i
        print(an)
    for key,value in dictofargs.items():                #use dict.iteritems() for python 2.x to iterate a dictionary
        print(key,":",value)
        
        
def defarg(x, y=9)                                     #use of y=9 when second arg for y not supplied in func call

if __name__ == '__main__':
    first(2,3,4,naam="kapoor-rakshit")
    print()
    first(2,pata="amritsar",intern="true at WIPRO")

    
