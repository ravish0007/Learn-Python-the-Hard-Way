# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#Study Drills
#Function Checklist
"""
Did you start your function definition with def?
Does your function name have only characters and _ (underscore) characters?
Did you put an open parenthesis ( right after the function name?
Did you put your arguments after the parenthesis ( separated by commas?
Did you make each argument unique (meaning no duplicated names)?
Did you put a close parenthesis and a colon ): after the arguments?
Did you indent all lines of code you want in the function four spaces? No more, no less.
Did you "end" your function by going back to writing with no indent (dedenting we call it)?
"""
#When you run ("use" or "call") a function, check these things:
"""
Did you call/use/run this function by typing its name?
Did you put the ( character after the name to run it?
Did you put the values you want into the parenthesis separated by commas?
Did you end the function call with a ) character?
"""

'''
What does the * in *args do?
That tells Python to take all the arguments to the function and then put them in args as a list. It's like argv that you've been using, but for functions. It's not normally used too often unless specifically needed.
'''
