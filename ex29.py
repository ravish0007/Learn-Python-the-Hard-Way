people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."

"""
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
"""

#Study Drills
#1. What do you think the if does to the code under it?
#If the if condition is satisfied then the code under it is run.

#2. Why does the code under the if need to be indented four spaces? 
#Python is very particular about indentation.

#3. What happens if it isn't indented?
#If not indented it gives the error -> "IndentationError: expected an indented block"

#4. Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
'''
cats = 10
dogs = 30
people = 70

if cats != dogs:
	print "Inequal number of dogs and cats"

if dogs <= people:
	print "Dogs are less than or equal to people"

if dogs >= cats:
	print "Dogs are greater than or equal to cats"

Output ->
Inequal number of dogs and cats
Dogs are less than or equal to people
Dogs are greater than or equal to cats
'''

#5. What happens if you change the initial values for people, cats, and dogs?
"""
people = 50
cats = 2
dogs = 7


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."

Output ->
Not many cats! The world is saved!
The world is dry!
People are greater than or equal to dogs.
"""
