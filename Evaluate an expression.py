x,k=map(int,input().split())            
p=eval(input())
print(p==k)

''' NOTE : The variables in expression must be available ie must be defined for input in expression '''
''' This code checks if p(x)==k , where p is an input expression of form  p(x) = x**4 - 1*x**3 + 5*x**2  and store result as a string'''
''' The eval() function can evaluate even the inbuilt keywords as: eval(print(abs(-1)+1)) gives 2 '''
