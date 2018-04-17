x,k=map(int,input().split())            
p=eval(input())                           #expression must have x or k or both as a variable
print(p==k)

''' NOTE : The variables in expression must be available ie must be defined for input in expression '''
''' This code checks if p(x)==k , where p is an input expression of form  p(x) = x**4 - 1*x**3 + 5*x**2  and store result as a string'''
''' The eval() function can evaluate even the inbuilt keywords as: eval(print(abs(-1)+1)) gives 2 '''

import numpy
a=list(map(float,input().split()))
x=float(input())
print(numpy.polyval(a,x))
'''The polyval tool evaluates the polynomial at specific value. Here a[] is a list of coefficients of polynomial'''

'''The polyder tool returns the derivative of the specified order of a polynomial.  #numpy.polyder([1, 4, 1, 1])   #Output : [3 8 1]'''

'''The polyint tool returns antiderivative (indefinite integral) of a polynomial.   #numpy.polyint([1, 1, 1])      #Output : [0.33333333 0.5 1. 0.]'''

'''The roots tool returns the roots of a polynomial with the given coefficients.   #numpy.roots([1, 0, -1])        #Output : [-1.  1.]'''

'''The poly tool returns the coefficients of a polynomial with the given sequence of roots. #numpy.poly([-1, 1, 1, 10])  #Output : [1 -11 9 11 -10]'''
