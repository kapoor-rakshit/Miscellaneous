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
