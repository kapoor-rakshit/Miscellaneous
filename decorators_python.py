# A decorator takes in a function, adds some functionality and returns it.
# This is also called METAprogramming as a part of the program tries to modify another part of the program at compile time.

# IMPORTANT :  everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. 
#              Functions are no exceptions, they are objects too (with attributes). 
#              Various different names can be bound to the same function object.

#  function that take other functions as arguments are also called HIGHER ORDER functions. 

#  use the @ symbol along with the name of the decorator function and
#  place it above the definition of the function to be decorated. 

#For example:-

@make_pretty
def ordinary():
    print("I am ordinary")
#-----------------------------------------is equivalent to-------------------------------
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

#example:-

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return
      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
    
"""
>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide

 No. of parameters of the nested inner() function inside the decorator is same as the parameters of functions it decorates. 
 Now General decorators that work with any number of parameter using some_function(*args, **kwargs).:-
"""
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
    
# Multiple decorators can be chained in Python.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")
#----------------------------------is equivalent to------------------------------------
def printer(msg):
    print(msg)
printer = star(percent(printer))

"""
NOTE : order matters of giving decorators, here #star uses #percent's inner and #percent uses #printer

OUTPUT :
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
"""
