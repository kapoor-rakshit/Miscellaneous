# MODULE

chkvar = 12.56

def chkfunc():
	for _ in range(3):
		print("bonjour!")

# SOURCE CODE for using this module "py_package_modules"

		# import py_package_modules as p

		# print(p.chkvar)
		# p.chkfunc()



# PACKAGE
# a package is a collection of modules
# it is a directory that must have a special file called "__init__.py"

# eg:-   A dir named pytestpackage is a package, having files:
#        1. __init__.py
#        2. module1.py
#        3. module2.py

# SOURCE CODE for __init__.py
		#  from module1 import *
		#  from module2 import *
		#  print("first package")

# SOURCE CODE for module1.py
        #  def sum(a,b):
        #   return a+b

# SOURCE CODE for module2.py
       #  def prod(a,b):
       #    return a*b

# SOURCE CODE for using this package "pytestpackage"
       #  import pytestpackage as pp
       #  print(pp.sum(5,6))
       #  print(pp.prod(11,2))