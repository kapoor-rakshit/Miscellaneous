# commandline arguments
import sys

naam, arg1, arg2 = sys.argv     # first val in argv is filename, and remaining values are supplied by user
arg2 = sys.argv[2]              # 2 index arg in argv

print(naam)
print(arg1)
print(arg2)


# sys module
sys.platform                  # platform details
sys.getwindowsversion()       # windows version
sys.version                   # python version
sys.path                      # python path
sys.builtin_module_names      # name of builtin modules
sys.copyright                 # copyright of python
sys.executable                # location of python interpreter
sys.exit()                    # exit
sys.getsizeof                 # memory used in bytes for current interpreter
sys.modules                   # all loaded modules


# os module
os.name                      # name of operating system (not for Windows)
os.environ                   # dict for env variables
os.getcwd()
os.listdir()
os.mkdir()
os.rmdir()
os.remove()
os.system('notepad')        # execute command from terminal , os.system('calc')


# escape sequence
print(r"this is \n \a ignored")   # use r or R to ignore escape sequence


# find()
string.find("i")                 # returns index of first occurrence of "i" from left
                                 # default startindex=0 , [endindex=len
string.find("i",startindex,endindex)
string.find("i",startindex)


# replace()
string.replace("oldstr","newstr")
string.replace("oldstr","newstr",3)    # no. of occurrence of oldstr to be replaced with newstr


# list operation
a.extend(b)                           # append elements of b list to list a     [23,45,56]
a.append(b)                           # append list b as an element to list a   [23,[45,56]]
a.pop()                               # remove last element
a.remove(elem)                        # remove specific element elem


# dir()
import math
dir(math)                            # lists available packages/functions in a module


# globals() and locals()
# returns a dictionary containing names that can be accessed locally / globally from within function.


# reload()
reload(modulename)     # reload a module, useful when a module is edited but to try this new version without leaving interpreter


# misc.
# use asterisk (*) symbol to repeat    eg:    print("thank you" * 3)     prints the str "3" times

