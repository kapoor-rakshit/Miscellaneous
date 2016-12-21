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
'''shape and reshape'''
import numpy
a=list(map(int,input().split()))
a=numpy.array(a)

print(a.shape)                               # to get array dimensions #(5,)->5 rows and 0 columns #(3, 2) -> 3 rows and 2 columns

a.shape=(3,3)                                # to change array dimensions
print(a)

print(numpy.reshape(a,(3,3)))                # It creates a new array and does not modify the original array itself.

#The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
#   [[1 2]
#    [3 4]
#    [5 6]]
'''transpose and flatten'''
import numpy
n,m=map(int,input().split())
t=[]
for i in range(0,n,1):
    a=list(map(int,input().split()))
    t.append(a)
print(numpy.transpose(t))         # transposition of an array using the tool numpy.transpose. 
                                  # It will not affect the original array, but it will create a new array.
    
print(numpy.array(t).flatten())   # The tool flatten() creates a copy of the input array flattened to one dimension.
                                  # does not effect original array
'''concatenate'''
import numpy
n,m,c=map(int,input().split())
fa=[]
fe=[]
for i in range(0,n,1):
    a=list(map(int,input().split()))
    fa.append(a)
for i in range(0,m,1):
    a=list(map(int,input().split()))
    fe.append(a)
print(numpy.concatenate((fa,fe),axis=0))   #axis = 0,no. of rows increases   #axis = 1 ,no. of columns increases

# it is possible to specify the axis along which multiple arrays are concatenated.By default, it is along the first dimension(1).
# all the input array dimensions except for the concatenation axis must match exactly
'''zeros and ones'''
import numpy
a=list(map(int,input().split()))
print(numpy.zeros((a),dtype=numpy.int))
print(numpy.ones((a),dtype=numpy.int))

#a is a list of dimensions to array to be generated. It can be two,three,... dimensional
#The zeros and ones tool returns a new array with a given shape and type filled with 0's and 1's.
#Default type is float                    #Type changes to int using dtype= arg

