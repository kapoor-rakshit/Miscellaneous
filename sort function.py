'''Use of sort() and sorted() functions in python
   sort() modifies original list but sorted() does not'''

a=list(map(int,input().split()))

a.sort(reverse=True)             #sort in descending order
b=sorted(a,reverse=True)
                                #key always accept a callable function (can be by lambda or def)
a.sort(key=len)                 #sort in accordance with length of strings
b=sorted(a,key=len)

a.sort(key=str.lower)           #sort by treating all elements as lower case
b=sorted(a,key=str.lower)              #a similar is str.upper

a.sort(key=abs)
print(*sorted(a,key=abs))       #sort according to absolute values

a.sort(key=func)                #key can accept any user defined function
b=sorted(a,key=func)              #this func must return a value to guide sorting

        #Eg: def func(s):
        #        return s[-3]     #returns third last character of string 
                                  #sorts acc to third last character
         
'''sort() function does not work with strings, use sorted()'''
print("".join(sorted(string)))
print(*sorted(string),sep='')        #sep is the separator parameter of print

'''sorted() function with key having parameters'''
a=input()
print(*(sorted(a,key=lambda character:(character.isdigit() and int(character)%2==0,character.isdigit(),character.isupper(),character.islower(),character))),sep='')
#sorts acc to key values where parametrs to lambda are: first param is given higher priority,then second param and so on.
#higher the priority means it will be placed at last ie here first will be lower,upper,odd digit,even digit.
#the last argument is a variable which specifies that sort acc to caracters of string.

'''sort the matrix rows according to kth column ie rows are adjusted preserving their elements wrt to kth element of each row''' 
n,m=map(int,input().split())
mat=[]
for i in range(0,n,1):
    tp=[]
    tp=list(map(int,input().split()))
    mat.append(tp)
k=int(input())
mat.sort(key=lambda element:element[k])    #lambda returns the kth element of each element(lists or rows here) in every row
for i in range(0,n,1):                     #it is applied to every row to get kth element as a key
    print(*mat[i])

    
    
