#A function defined inside another function is called a nested function.
#Nested functions can access variables of the enclosing scope.

#closure_func = some_function(args)

#The technique by which some data gets attached to the code is called closure in Python.
#The value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.
#Closures can avoid the use of global values and provides some form of data hiding. 
#It can also provide an object oriented solution to the problem.

#example:-

def first(msg):
    print(msg)    

first("Hello")                          #first func called

second = first                          #second also becomes a func with same defn as first

second("Hello")                         #second func called

#example:-

def print_msg(msg):                       # This is the outer enclosing function (scope)

    def printer():                        # This is the nested function
        print(msg)

    return printer  

another = print_msg("Hello")               #This is a closure function
another()                                  #OUTPUT : Hello (this data gets attached to code)

"""The print_msg() function was called with the string "Hello" and the returned function was bound to the name another.
On calling another(), the message was still remembered although we had already finished executing (returned from) the print_msg() function.

The criteria that must be met to create closure in Python are summarized in the following points.

We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.
"""

#example:-

>>> del print_msg
>>> another()                                 #No error
Hello
>>> print_msg("Hello")                        #error
Traceback (most recent call last):
...
NameError: name 'print_msg' is not defined

#example:-

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)            #closure func, got definition of multiplier() and value of n

times5 = make_multiplier_of(5)            #closure func, got definition of multiplier() and value of n

print(times3(9))                          # Output: 27

print(times5(3))                          # Output: 15

print(times5(times3(2)))                  # Output: 30

"""
The values that get enclosed in the closure function can be found out using a __closure__ attribute that returns a tuple of cell objects if it is a closure function. 

>>> make_multiplier_of.__closure__
>>> times3.__closure__
(<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
>>> times3.__closure__[0].cell_contents
3
>>> times5.__closure__[0].cell_contents
5
"""
