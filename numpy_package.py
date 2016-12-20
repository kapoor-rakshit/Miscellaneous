import numpy                    
a=list(map(float,input().split()))
a.reverse()
b=numpy.array(a,float)
print(b)

#The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.                    
#A NumPy array is a grid of values. 
#They are similar to lists, except that every element of an array must be the same type.
#numpy.array() is used to convert a list into a NumPy array. 
#The second argument (float) can be used to set the type of array elements.

import numpy
a=list(map(int,input().split()))
a=numpy.array(a)

print(a.shape)                               # to get array dimensions #(5,)->5 rows and 0 columns #(3, 2) -> 3 rows and 2 columns

a.shape=(3,3)                                # to change array dimensions
print(a)

print(numpy.reshape(a,(3,3)))                #It creates a new array and does not modify the original array itself.

#The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
#   [[1 2]
#    [3 4]
#    [5 6]]
