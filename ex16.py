from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

#Study Drills
#1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
#Importing a function form a module
"""
from sys import argv

#Script takes command line arguments
script, filename = argv

#Print a few lines
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Take input from the user
raw_input("?")

#Open a file with write mode
print "Opening the file..."
target = open(filename, 'w')

#http://stackoverflow.com/questions/26917197/behaviour-of-truncate-method-in-python
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#Take input from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#Writing to a file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
#Close the file
target.close()
"""

#2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
#http://stackoverflow.com/questions/6394170/very-basic-python-question-strings-formats-and-escapes
"""
from sys import argv

script, filename = argv

target = open(filename, 'r')

print target.read()
"""

#3. There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
'''
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()
'''

#4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
# w -> Opens the file in write mode. Deletes all existing content from the file.

#5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open function and see if that's true.
#If we change line 12 to {target = open(filename, 'r')} then we get the error
'''
root@kali:~/Desktop/LPTHW# python h.py hiest.txt
We're going to erase 'hiest.txt'.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file.  Goodbye!
Traceback (most recent call last):
  File "h.py", line 15, in <module>
    target.truncate()
IOError: File not open for writing
root@kali:~/Desktop/LPTHW#
'''
#This means we have to open he file with 'w' mode, for target.truncate() to work.

#Is the truncate() necessary with the 'w' parameter?
#Yes

"""
What modifiers to the file modes can I use?
The most important one to know for now is the + modifier, so you can do 'w+', 'r+', and 'a+'. This will open the file in both read and write mode, and depending on the character use position the file in different ways.

Does just doing open(filename) open it in 'r' (read) mode?
Yes, that's the default for the open() function.
"""
