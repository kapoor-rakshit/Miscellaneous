# Iterators are objects that can be iterated upon.
# Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
# use the next() function to manually iterate through all the items of an iterator. 
# When we reach the end and there is no more data to be returned, it will raise StopIteration.

my_list = [4, 7, 0, 3]

# get an iterator object using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)


# how the for loop is actually implemented in Python.

for element in iterable:
    # do something with element
    
# is equivalent to-----------------------

iter_obj = iter(iterable)
# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
        
       
# Building own iterators

class PowTwo:                                       
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteratio
 """
>>> a = PowTwo(4)
>>> i = iter(a)
>>> next(i)
1
>>> next(i)
2
>>> next(i)
4
>>> next(i)
8
>>> next(i)
16
>>> next(i)
Traceback (most recent call last):
...
StopIteration
"""   

# Another example

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
"""
 >>> a = iter(InfIter())
>>> next(a)
1
>>> next(a)
3
>>> next(a)
5
>>> next(a)
7
 """
