
# REFERENCE : https://www.hackerrank.com/challenges/symmetric-difference/problem


# CREATING SETS
  myset = {1, 2}          # Directly assigning values to a set
  myset = set()           # Initializing a set
  myset = set(a)          # Creating set from list



# MODIFYING SETS
  > Using the add() function
   myset.add('c')
   myset.add((5, 4))                        # {'c', (5, 4)}
  
  > Using the update() function, update() only works for iterable objects
   myset.update([1, 2, 3, 4])               # {1, 'c', 4, 2, (5, 4), 3}
   myset.update({1, 7, 8})                  # {1, 'c', 4, 7, 8, 2, (5, 4), 3}
   myset.update({1, 6}, [5, 13])            # {1, 'c', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
  
  
  
# REMOVING ITEMS 
  > Both the discard() and remove() functions take a single value as an argument and removes that value from the set.
  > If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
   myset.discard(10)
   myset.remove(13)
  
  
  
# COMMON SET OPERATIONS 
  > Using union(), intersection() and difference() functions.
   a.union(b)                             # Values which exist in a or b
   a.intersection(b)                      # Values which exist in a and b
   a.difference(b)                        # Values which exist in a but not in b ie remove values from A which are in B also, show remaining in A 
   
  > The union() and intersection() functions are symmetric methods, but difference() is not
   a.union(b) == b.union(a)               # True
   a.intersection(b) == b.intersection(a) # True
   a.difference(b) == b.difference(a)     # False
   
   
