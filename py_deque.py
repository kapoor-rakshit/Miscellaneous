
# REFERENCE : https://www.hackerrank.com/challenges/py-collections-deque/problem

# collections.deque()
#  A deque is a double-ended queue.
#  It can be used to add or remove elements from both ends.
#  Deque support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. 

from collections import deque
d = deque()                                  # initialize deque()

d.append(1)                                  # deque([1])

d.appendleft(2)                              # deque([2, 1])

d.clear()                                    # deque([])

d.extend('1')                                # deque(['1'])

d.extendleft('234')                          # deque(['4', '3', '2', '1'])

d.count('1')                                 # 1

d.pop()                                      # deque(['4', '3', '2'])

d.popleft()                                  # deque(['3', '2'])

d.extend('7896')
d.remove('2')                                # deque(['3', '7', '8', '9', '6'])

d.reverse()                                  # deque(['6', '9', '8', '7', '3'])


