m,o=b.split(',')                #splits the string according to character in ' ' ,args before = must be same as splits reqd 
m,o=b.split()                   #default value is space

a.find("CONTEST_WON")           #finds substring in a and Returns -1 if not found else return first index where character match

'''Tuples are like lists, except they are immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be mutable).
Tuples play a sort of "struct" role in Python -- a convenient way to pass around a little logical, fixed size bundle of values.
A function that needs to return multiple values can just return a tuple of the values.'''

tuple = (1, 2, 'hi')
print (len(tuple))                ## 3
print (tuple[2])                  ## hi
tuple[2] = 'bye'                  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')             ## this works

'''To create a size-1 tuple, the lone element must be followed by a comma.
Comma is necessary to distinguish the tuple from the ordinary case of putting an expression in parentheses.'''

tuple = ('hi',)                    ## size-1 tuple

(x, y, z) = (42, 13, "hike")
print z                            ## hike
(err_string, err_code) = Foo()     ## Foo() returns a length-2 tuple

nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]                  ## [1, 4, 9, 16]

'''The syntax is [ <expression> for var in list ] The expr to its left is evaluated once for each element to give the values for the new list.
Here is an example with strings, where each string is changed to upper case with '!!!' appended:'''

strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]    ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]            ## [2, 1]

fruits = ['apple', 'cherry', 'bannana', 'lemon']      ## Select fruits containing 'a', change to upper case
afruits = [ s.upper() for s in fruits if 'a' in s ]   ## ['APPLE', 'BANNANA']
  
