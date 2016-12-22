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
a=numpy.array(a)                             # [1 2 4 6] is (4,) ie 4 rows and 0 columns
print(a.shape)                               # to get array dimensions #(5,) ie 5 rows and 0 columns #(3, 2) ie 3 rows and 2 columns
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
'''eye and identity'''
import numpy
n,m=map(int,input().split())
print(numpy.eye(n,m,k=2,dtype=numpy.float))  
#The eye tool returns a 2-D array with 1 as the diagonal and 0 elsewhere. 
#The default type of elements is float.
#k is a keyword to specify diagonal no. (k=1 for first upper ,k=-2 for second lower)
#The diagonal can be main(k=0) default, upper(k=+ve) or lower(k=-ve) depending on the optional parameter . 
print(numpy.identity((4),dtype=numpy.int))
#The identity tool returns an identity array. 
#An identity array is a '''SQUARE matrix''' with all the main diagonal elements as 1 and the rest as 0.
'''arithmetic operations'''
import numpy
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=numpy.array(a)
b=numpy.array(b)
print(a+b)                           # numpy.add(a,b)
print(numpy.subtract(a,b))           # a-b   not reqd to convert to numpy.array if using functions
print(a*b)                           # numpy.multiply(a,b)     '''corresponding multiply, not matrix product'''
print(a//b)                          # numpy.divide(a,b) in float type    '''corresponding divide'''
print(numpy.mod(a,b))                # a%b
print(numpy.power(a,b))              # a**b
'''ceil, floor and rint'''
import numpy
a=list(map(float,input().split()))
print(numpy.array(numpy.floor(a),int))
print(numpy.array(numpy.ceil(a),int))
print(numpy.array(numpy.rint(a),int))
# ceil ,floor, rint(to nearest integer) functions results in float values.
# dtype=numpy.int does not work with it
# converted to int using numpy.array(a,int)
'''sum and prod'''
import numpy
n,m=map(int,input().split())
a=[]
for i in range(0,n,1):
    tp=list(map(int,input().split()))
    a.append(tp)
s=numpy.sum(a,axis=0)          
p=numpy.prod(s)
print(p)
#The sum tool returns the sum of array elements over a given axis. #axis=0, gives array of size=no of columns  #axis=1, size=no. of rows
#The prod tool returns the product of array elements over a given axis.
#By default,the axis=None.Therefore,it performs a sum/product over all the dimensions of the input array.
'''min and max'''
import numpy
n,m=map(int,input().split())
a=[]
for i in range(0,n,1):
    tp=list(map(int,input().split()))
    a.append(tp)
mn=numpy.min(a,axis=1)
print(numpy.max(mn,axis=None))
#The tool min returns the minimum value along a given axis.
#The tool max returns the maximum value along a given axis.
'''mean, std and var'''
import numpy
import numpy
n,m=map(int,input().split())
a=[]
for i in range(0,n,1):
    tp=list(map(int,input().split()))
    a.append(tp)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,axis=None))
#The mean tool computes the arithmetic mean along the specified axis.
#The std tool computes the arithmetic standard deviation along the specified axis.
'''Standard Deviation is a measure of how spread out numbers are.It is the square root of the Variance.'''
#The var tool computes the arithmetic variance along the specified axis.
'''Variance:average of squared differences.'''
'''(squared difference):(subtract the Mean and individual no.s) square the result.'''
