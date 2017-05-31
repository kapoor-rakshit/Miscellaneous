from math import *
from random import *

a=156
b=84454

del a,b                #delete the reference to a number object by using the del statement.

a=0x57a7                #hexadecimal (0 to F digits)
b=0o77                  #octal       (0 to 7 digits)
print(a)
print(b)

print(pi)              #math module
print(e)

                      #random module
for i in range(8):
    print(choice([1,5,9,89]),choice("Hello kapoor-rakshit"),choice(range(2)))
    #returns random element from list,string,range(0 to arg-1) ie (0 to 1 here)
    
    print(randrange(0,9,3))
    #randrange(start,stop,step)
    #generates a number from list [0,3,6]...upper limit (stop) not included (9 here)
