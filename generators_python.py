"""SOURCE : https://www.programiz.com/python-programming/generator"""

# Python generators are a simple way of creating iterators.
# a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# __iter__() and __next__() method, keep track of internal states, raise StopIteration when there are no values to be returned
# are automatically handled by generators in Python.

# a function which contains at least one yield statement becomes a generator function.
# Both yield and return will return some value from a function.
# The difference is that, a return statement terminates a function entirely, 
# yield statement pauses the function saving all its states and later continues from there on successive calls.

# Generator function contains one or more yield statement.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

#example:-

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
"""
>>> # It returns an object but does not start execution immediately.
>>> a = my_gen()
>>> # We can iterate through the items using next().
>>> next(a)
This is printed first
1
>>> next(a)
This is printed second
2
>>> next(a)
This is printed at last
3
>>> next(a)
Traceback (most recent call last):
...
StopIteration
"""

#above example is equivalent to:-

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item)    
    
#example:-

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

for char in rev_str("hello"):
     print(char)
     
"""
# Output:
# o
# l
# l
# e
# h
"""

#Python Generator Expression
# list comprehension produces the entire list, generator expression produces one item at a time.
# They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than list comprehension.

# square each term using list comprehension, [] bracket
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# square each term using generator expression, () bracket, which returns generator object
a=(x**2 for x in my_list)
print(next(a)).....so on

#example:-

def gen(arg):                #give powers of two
...  n=0
...  while n<arg:
...   yield 2**n
...   n+=1

"""
>>> a=gen(6)
>>> next(a)
1
>>> print(next(a))
2
>>> next(a)
4
.......so on upto StopIterartion
"""

# Pipelining generators
"""
The log file has a column (4th column) that keeps track of the number of pizza sold every hour and 
we want to sum it to find the total pizzas sold in 5 years.
Assume everything is in string and numbers that are not available are marked as 'N/A'. 
A generator implementation of this could be as follows:-
"""
with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))
    
    
