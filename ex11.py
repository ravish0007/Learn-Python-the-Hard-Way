print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Study Drill
#1. Go online and find out what Python's raw_input does.
#http://www.cyberciti.biz/faq/python-raw_input-examples/

#2. Can you find other ways to use it? Try some of the samples you find.

print "\n"

#3. Write another "form" like this to ask some other questions.
print "Which language are you learning?",
language = raw_input()
print "How many days will it take for you to learn it?",
days = raw_input()

print "So, you're learning %r, and it will take %r days to learn it." % (language, days)

"""
What's the difference between input() and raw_input()?
The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.

When my strings print out there's a u in front of them, as in u'35'.
That's how Python tells you that the string is Unicode. Use a %s format instead and you'll see it printed like normal.

How do I get a number from someone so I can do math?
That's a little advanced, but try x = int(raw_input()) which gets the number as a string from raw_input() then converts it to an integer using int().
"""

print "\n"

print "Weight in float?",
weight = int(raw_input())
print "Weight in int is : %r",  weight
