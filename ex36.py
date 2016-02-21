print """
-> Rules for If-Statements
1.) Every if-statement must have an else.
2.) If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.
3.) Never nest if-statements more than two deep and always try to do them one deep.
4.) Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
5.) Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.
"""

print """
-> Rules for Loops
1.) Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
2.) Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.
"""

print """
-> Tips for Debugging
1.) Do not use a "debugger." A debugger is like doing a full-body scan on a sick person. You do not get any specific useful information, and you find a whole lot of information that doesn't help and is just confusing.
2.) The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.
3.) Make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little.
"""

from sys import exit

def end(why):
    print why, "Good job!"
    exit(0)

def start():
    print "Lets begin the game"
    print "Which planet would you like to visit :- 1.) Mars 2.) Jupiter "
    print "Choose One"

    planet = raw_input("> ")

    if planet == "Mars":
        end("You might survive")
    else:
        end("You are doomed.")

start()
