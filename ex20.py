from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#Study Drills
#1. Write English comments for each line to understand what that line does.
"""
#Importing a module
from sys import argv

#Command line arguments
script, input_file = argv

#Function that reads a file
def print_all(f):
    print f.read()

#Function sets the files current position at the beginning
def rewind(f):
    f.seek(0)

#Function that prints one line at a time
def print_a_line(line_count, f):
    print line_count, f.readline()

#Opening a file and assigning it to a variable
current_file = open(input_file)

print "First let's print the whole file:\n"

#Using the function defined above to print the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Using the function to point the file to the beginning
rewind(current_file)

print "Let's print three lines:"

#Printing one line at a time.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
"""

#2. Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line. 
"""
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
print current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
print current_line
print_a_line(current_line, current_file)
"""

#3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.

#4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there. Then try pydoc file.seek to see what seek does.
"""
pydoc file
pydoc file.seek
 |  seek(...)
 |      seek(offset[, whence]) -> None.  Move to new file position.
 |
 |      Argument offset is a byte count.  Optional argument whence defaults to
 |      0 (offset from start of file, offset should be >= 0); other values are 1
 |      (move relative to current position, positive or negative), and 2 (move
 |      relative to end of file, usually negative, although many platforms allow
 |      seeking beyond the end of a file).  If the file is opened in text mode,
 |      only offsets returned by tell() are legal.  Use of other offsets causes
 |      undefined behavior.
 |      Note that not all file objects are seekable.

"""

#5. Research the shorthand notation += and rewrite the script to use += instead.
"""
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
"""

'''
What is f in the print_all and other functions?
The f is a variable just like you had in other functions in Exercise 18, except this time it's a file. A file in Python is kind of like an old tape drive on a mainframe, or maybe a DVD player. It has a "read head," and you can "seek" this read head around the file to positions, then work with it there. Each time you do f.seek(0) you're moving to the start of the file. Each time you do f.readline() you're reading a line from the file, and moving the read head to right after the \n that ends that line. This will be explained more as you go on.

Why does seek(0) not set the current_line to 0?
First, the seek() function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte (first byte) in the file. Second, current_line is just a variable and has no real connection to the file at all. We are manually incrementing it.

How does readline() know where each line is?
Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far. The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.

Why are there empty lines between the lines in the file?
The readline() function returns the \n that's in the file at the end of that line. Add a , at the end of your print function calls to avoid adding double \n to every line.
'''
