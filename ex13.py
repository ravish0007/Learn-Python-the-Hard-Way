from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Study Drills
#1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it. 
'''
root@kali:~/Desktop/LPTHW# python ex13.py first second
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack
root@kali:~/Desktop/LPTHW#
'''

#2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
"""
print "---Few Arguments---" 
from sys import argv

script, first  = argv

print "The script is called:", script
print "Your first variable is:", first

print "---More Arguments---"
from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
"""

#3. Combine raw_input with argv to make a script that gets more input from a user.
#13_StudyDrill_3.py

"""
What's the difference between argv and raw_input()?
The difference has to do with where the user is required to give input. If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use raw_input().

What's the difference between argv and raw_input()?
The difference has to do with where the user is required to give input. If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use raw_input().

Why can't I do this raw_input('? ') = x?
Because that's backward to how it should work. Do it the way I do it and it'll work.
"""
