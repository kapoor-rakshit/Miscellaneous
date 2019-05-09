
from math import *
from random import *
import cmath                          # complex math lib for handling complex number operations, eg: cmath.sqrt(-4) = 2i
from fractions import Fraction        # fractions package

a=156
b=84454

del a,b                 #delete the reference to a number object by using the del statement.

a=0x57a7                #hexadecimal (0 to F digits)
b=0o77                  #octal       (0 to 7 digits)
print(a)
print(b)

print(bin(7), oct(7), hex(7))     # binary, octal, hexadecimal representation

print(pi)              #math module
print(e)
print(gcd(a, b))       #math module




                       #random module
for i in range(8):
    print(choice([1,5,9,89]),choice("Hello kapoor-rakshit"),choice(range(2)))
    #returns random element from list,string,range(0 to arg-1) ie (0 to 1 here)
    
    print(randrange(0,9,3))
    #randrange(start,stop,step)
    #generates a number from list [0,3,6]...upper limit (stop) not included (9 here)
    
    print(random())
    #The random() method returns a random floating point number in the range [0.0, 1.0].

print()

seed(0)
print(random())
seed(0)
print(random())

seed(1)
print(random())
#The seed() method initializes the basic random number generator.
#To repeat the same random number we have seeded it to a number OR a string.

a=[12,56,8,63,.058]            #can be a tupple also
shuffle(a)
print(a)
#The shuffle() method randomizes the items of a list/tupple in place.

print(uniform(2,4))
#The uniform() method returns a random float r, such that x <= r < y




                               #fractions module
  
Fraction(16, -10)              # >> Fraction(-8, 5)

k = Fraction(16, -10)
k.numerator                    # -8
k.denominator                  # 5

Fraction(123)                  # >> Fraction(123, 1)
Fraction()                     # >> Fraction(0, 1)
Fraction('3/7')                # >> Fraction(3, 7)                                   # NOTE : use of ''
Fraction('-3/7')               # >> Fraction(-3, 7)
Fraction('-.125')              # >> Fraction(-1, 8)
Fraction(1.1)                  # >> Fraction(2476979795053773, 2251799813685248)     # NOTE : without ''
float(Fraction(355, 113))      # >> 3.1415929203539825                               # typecasting to float, else will show Fraction(355, 113)

