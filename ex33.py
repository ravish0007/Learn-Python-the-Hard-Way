i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

#Study Drills
#1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#2. Use this function to rewrite the script to try different numbers.
#3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
#4. Rewrite the script again to use this function to see what effect that has.
"""
i = 0
numbers = []

def funWhile(num, sumNum):
        global i
        while i < num:
                print "At the top i is %d" % i
                numbers.append(i)

                i = i + sumNum
                print "Numbers now: ", numbers
                print "At the bottom i is %d" % i


	print "The numbers: "

	for nums in numbers:
		print nums

funWhile(10,1)

If "global i" is not defined we get the error ->
Traceback (most recent call last):
  File "bat.py", line 19, in <module>
    funWhile(7,2)
  File "bat.py", line 5, in funWhile
    while i  < num:
UnboundLocalError: local variable 'i' referenced before assignment
"""

#5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
"""
elements = []

for i in range(0, 10):
    print "Adding %d to the list elements" % i
    elements.append(i)

print "List elements: %r" % elements
"""
