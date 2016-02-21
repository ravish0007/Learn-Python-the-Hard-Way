from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#Study Drills
#1. Above each line, write out in English what that line does.
'''
#Importing from modules
from sys import argv

#Unpacking
script, filename = argv

#Opening a file and assigning it to a variable
txt = open(filename)

print "Here's your file %r:" % filename
#Reads the contents of the file
print txt.read()

print "Type the filename again:"
#Takes input from the user as filename
file_again = raw_input("> ")
#Opens the file
txt_again = open(file_again)
#Prints the contents of the file.
print txt_again.read()
'''

#4. Get rid of the lines 10-15 where you use raw_input and run the script again.
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

#5. Use only raw_input and try the script that way. Why is one way of getting the filename better than another?
'''
prompt = '> '

file = raw_input(prompt)

file_open = open(file)
print file_open.read()
'''

#6. Start python to start the python shell, and use open from the prompt just like in this program. Notice how you can open files and run read on them from within python?
#7. Have your script also call close() on the txt and txt_again variables. It's important to close files when you are done with them. 
'''
root@kali:~/Desktop/LPTHW# python
Python 2.7.3 (default, Mar 14 2014, 11:57:14)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> foo = open("ex15_sample.txt")
>>> foo.read()
'This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.\n'
>>> foo.close()
>>>
root@kali:~/Desktop/LPTHW#
'''

"""
What does from sys import argv mean?
For now just understand that sys is a package, and this phrase just says to get the argv feature from that package. You'll learn more about these later.

Does txt = open(filename) return the contents of the file?
No, it doesn't. It actually makes something called a "file object." 
"""
