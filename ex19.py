def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Study Drills
#1. Go back through the script and type a comment above each line explaining in English what it does.
"""
#Define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"

#Numeric arguments given to the function
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#Variables given as parameters to a function 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
#Math preformed in parameters of a function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#Combination of math and variables 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""

#3. Write at least one more function of your own design, and run it 10 different ways.
"""
def addFunc(a,b):
        add = a + b
        print "The addition of numbers is: %r" % add

print "Way#1:"
addFunc(5,7)

print "Way#2:"
a = 4
b = 8
addFunc(a,b)

print "Way#3:"
print "Enter the value of a:"
a = raw_input("> ")
print "Enter the value of b:"
b = raw_input("> ")
addFunc(a,b)

print "Way#4:"
a = (2 + 9)
b = (5 + 6)
addFunc(a,b)

print "Way#5:"
a = 5
b = 8
addFunc(a+2,b+8)

print "Way#6:"
h = 6
j = 8
addFunc(a+h,b+j)

print "Way#7:"
import random
f = random.randrange(1, 10)
r = random.randrange(1, 10)
addFunc(f,r)

print "Way#8:"
def passValue():
  x1 = 100
  x2 = 200
  addFunc(x1,x2)

passValue()
"""

'''
What if I want to ask the user for the numbers of cheese and crackers?
You need to use int() to convert what you get from raw_input().
var1 = int(raw_input("p1: "))
var2 = int(raw_input("p2: "))
addFunc(var1,var2)
'''
