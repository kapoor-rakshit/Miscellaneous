#SOURCE : https://www.tutorialspoint.com/python/python_classes_objects.htm

"""The variable name, age is a class variable whose value is shared among all instances of a this class. 
This can be accessed as student.name, student.age from inside the class or outside the class."""

"""The first method __init__() is a special method, which is called class constructor or initialization method.
Python calls it when you create a new instance of this class."""

class student:
    name=""
    age=0
    def __init__(self,name,age,mark,jagah):    #constructor
        student.name=name
        student.age=age
        self.place=jagah
        self.marks=mark            #variables only for object of class, accessed as self.variable
    def setdata(self,naam,umar):
        student.name=naam
        student.age=umar
    def printdata(self):
        print("Name is :",student.name)
        print("Self Name is :",self.name)    #class atribute is self attribute too
        print("Age is :",student.age)
        print("Marks are :",self.marks)
        print("Class Section is :",student.section)
        print("Self Section is:",self.section)
    def __del__(self):                          #destructor
        print(self.__class__.__name__,"destructed")
name=input()
age=int(input())
mk=int(input())



"""Add, remove, or modify Attributes of classes and objects.
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

Instead of using the normal statements to access attributes, use the following functions
NOTE : first argument can be object or a class
hasattr(emp1, 'age')      # Returns true if 'age' attribute exists
getattr(emp1, 'age')      # Returns value of 'age' attribute
setattr(emp1, 'age', 8)   # Set attribute 'age' at 8
delattr(empl, 'age')      # Delete attribute 'age'"""

student.section=10                  #adds class atribute, becomes self attribute too

s1=student(name,age,mk,"Amritsar")             #first object of student class
s1.printdata()

s2=student("Rohit",16,90,"Ludhiana")           #second object of student class
s2.section=9                        #adds self attribute, cannot become class attribute
s2.printdata()

s3=student("Temporaryname",45,5632,"Jalandhar") #third object, temp args passed as it must have same args as constructor
s3.setdata("adhkkrak",1589)         #assign new values
s3.section=8                        #adds self attribute, cannot become class attribute
setattr(s3,'marks',500)
s3.printdata()

delattr(student,'section')
print(hasattr(student,'section'))
print(student.name)                #class variables get overriden
print(student.age)                 #So result is adhkkrak 1589

#print(self.marks)                 #Invalid as self is not a class defined
#print(student.marks)              Invalid as marks are not class variable



"""STATIC METHODS
decorate a method with keyword 'staticmethod' """
class test:
    
    @staticmethod
    def mthd(self):
        print("static method")

test.mthd()                         # call to static method using class name
obj = test()
obj.mthd()                          # call to static method using object
        

        
"""Python class keeps built-in attributes and can be accessed like any other attribute
CLASSNAME.__doc__: Class documentation string or none, if undefined.

CLASSNAME.__name__: student (Class name)

CLASSNAME.__module__: __main__ (Module name in which the class is defined. This attribute is "__main__" in interactive mode.)

CLASSNAME.__bases__: () (A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.)

CLASSNAME.__dict__: {'__module__': '__main__', 'displayCount':
<function displayCount at 0xb7c84994>, 'empCount': 2, 
'displayEmployee': <function displayEmployee at 0xb7c8441c>, 
'__doc__': 'Common base class for all employees', 
'__init__': <function __init__ at 0xb7c846bc>} 
(Dictionary containing the class's namespace.)"""

print(s3.__class__.__name__)       #return classname for object



"""a class can implement the special method __del__(), called a destructor.
That is invoked when the instance is about to be destroyed."""
del s1



"""Class INHERITANCE
class A:        # define your class A
.....

class B:         # define your class B
.....

class C(A, B):   # subclass of A and B
....."""
"""
NOTE : Constructor of parent class is not called.
The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class"""


"""SUPER keyword in MULTIPLE INHERITANCE
using super(CLASSNAME, self).METHODNAME()       # here METHODNAME can be __init__() too ie we can call constructor of parentclass 

class C(A,B):
   def __init__(self):
       super(C, self).__init__()               # constructor of A called first then of B """            



"""OVERRIDING METHODS
When parent class and child class have same name of methods then child class methods get preferece.
ie it overrides the parent class methods (overridden methods).
To call method of parent class from within overriding method use : ParentClassName.methodname(self,args,args) """

"""OVERLOADING METHODS
Python does not support overloading methods"""

"""OPERATOR OVERLOADING
It can be performed using specific keywords only
__add__ : call for + operator
__sub__ : call for - operator
__mul__ : call for * operator
__div__ : call for / operator
__str__ : output that is supposed to be human readable
__repr__: representation readable for the Python interpreter

eg:-
class RationalNumber():
     n = 0
     d = 0
     def __init__(self,n,d):
        self.n = n
        self.d = d
        
     def __mul__(self,other):
         if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
            
         n1,d1 = self.n  , self.d
         n2,d2 = other.n , other.d
         return RationalNumber(n1*n2 , d1*d2)
         
     def __str__(self):
         return '%s/%s' % (self.n,self.d) 
         
     __repr__ = __str__ 
     
a = RationalNumber(5,6)
b = RationalNumber(4,2)
print(a/b)                  # overloaded  __div__  called       # output : 20/12 """



"""DATA HIDING (ACCESS SPECIFIERS)
An object's attributes may or may not be visible outside the class definition.
public    : varmethodname , (default)
private   : __varmethodname , Name attributes with a double underscore prefix.
protected : _varmethodname , (it's a convention not a rule as py does not support protected data. 
                             They are public but must be treated as protected and should not be accessed from outside.)

Example :-
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount
      JustCounter.__mymethod(self)
      
   def __mymethod(self):
      print("private method")

counter = JustCounter()
counter.count()
counter.count()
print counter.__secretCount

When the above code is executed, it produces the following result −
1
2
Traceback (most recent call last):
  File "test.py", line 12, in <module>
    print counter.__secretCount
AttributeError: JustCounter instance has no attribute '__secretCount'

Solution :-
Python protects those members by internally changing the name to include the class name. 
Can access such attributes as object._className__attrName. ie

print counter._JustCounter__secretCount

When the above code is executed, it produces the following result −

1
2
2"""
