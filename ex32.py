the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i


#Study Drills
#1. Take a look at how you used range. Look up the range function to understand it.
"""
pydoc range
Help on built-in function range in module __builtin__:

range(...)
    range([start,] stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
"""

#2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
"""
Yes
root@kali:~/Desktop/LPTHW# python
Python 2.7.3 (default, Mar 14 2014, 11:57:14)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> ele = range(0,6)
>>> print ele
[0, 1, 2, 3, 4, 5]
>>>
root@kali:~/Desktop/LPTHW#
"""

#3. Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?
"""
pydoc list

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |
 |  Methods defined here:
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |
 |  __delslice__(...)
 |      x.__delslice__(i, j) <==> del x[i:j]
 |
 |      Use of negative indices is not supported.
 |
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |
 |      Use of negative indices is not supported.
 |
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |
 |  __setslice__(...)
 |      x.__setslice__(i, j, y) <==> x[i:j]=y
 |
 |      Use  of negative indices is not supported.
 |
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |
 |  append(...)
 |      L.append(object) -- append object to end
 |
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None
 |
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
"""

'''
How do you make a 2-dimensional (2D) list?
That's a list in a list like this: [[1,2,3],[4,5,6]]

Why is a for-loop able to use a variable that isn't defined yet?
The variable is defined by the for-loop when it starts, initializing it to the current element of the loop iteration, each time through.

Why does for i in range(1, 3): only loop two times instead of three times?
The range() function only does numbers from the first to the last, not including the last. So it stops at two, not three in the above. This turns out to be the most common way to do this kind of loop.

What does elements.append() do?
It simply appends to the end of the list. Open up the Python shell and try a few examples with a list you make. Any time you run into things like this, always try to play with them interactively in the Python shell.
root@kali:~/Desktop/LPTHW# python
Python 2.7.3 (default, Mar 14 2014, 11:57:14)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> elements = range(0, 6)
>>> elements
[0, 1, 2, 3, 4, 5]
>>> elements.append(111111111111)
>>> elements
[0, 1, 2, 3, 4, 5, 111111111111L]
>>>
root@kali:~/Desktop/LPTHW#
'''
