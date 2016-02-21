print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "\n"

#Study Drills
#1. Above each line, use the # to write a comment to yourself explaining what the line does.
#Normal print statement
print "Study Drill -> 1"
print "I will now count my chickens:"
#Print with math in the end
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
#Print and math in new line
print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#Print with boolean output
print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7
#Cross verify
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
#Realization
print "Oh, that's why it's False."

print "How about some more."
#Boolean
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#2. Remember in Exercise 0 when you started python? Start python this way again and using the math operators, use Python as a calculator.
"""
root@kali:~/Desktop/LPTHW# python
Python 2.7.3 (default, Mar 14 2014, 11:57:14)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2-2
0
>>> 2+7
9
>>> 7*5
35
>>> 5/8
0
"""

print "\n"

#3. Find something you need to calculate and write a new .py file that does it.
#3_StudyDrill_3.py

#4. Notice the math seems "wrong"? There are no fractions, only whole numbers. You need to use a "floating point" number, which is a number with a decimal point, as in 10.5, or 0.89, or even 3.0.
print "Study Drill -> 4"
print "3.0/7.0 :", 3.0/7.0

print "\n"

#5. Rewrite ex3.py to use floating point numbers so it's more accurate. 20.0 is floating point.
print "Study Drill -> 5"
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6.0
print "Roosters", 100 - 25 * 3 % 4.0

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7.0

print "What is 3 + 2?", 3 + 2.0
print "What is 5 - 7?", 5 - 7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2.0
print "Is it greater or equal?", 5 >= -2.0
print "Is it less or equal?", 5 <= -2.0

print "\n"

#6. Why does / (divide) round down?  ->  Id does'nt
print "7.0 / 4.0 :", 7.0 / 4.0
print "7 / 4 :", 7 / 4
