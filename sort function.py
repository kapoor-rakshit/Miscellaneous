'''Use of sort() and sorted() functions in python
   sort() modifies original list but sorted() does not'''

a=list(map(int,input().split()))

a.sort(reverse=True)             #sort in descending order
b=sorted(a,reverse=True)

a.sort(key=len)                 #sort in accordance with length of strings
b=sorted(a,key=len)

a.sort(key=str.lower)           #sort by treating all elements as lower case
b=sorted(a,key=str.lower)              #a similar is str.upper

a.sort(key=func)                #key can accept any user defined function
b=sorted(a,key=func)              #this func must return a value to guide sorting

        #Eg: def func(s):
        #        return s[-3]     #returns third last character of string 
                                  #sorts acc to third last character
