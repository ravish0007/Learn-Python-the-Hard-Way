people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

"""
Output ->
We should take the cars.
Maybe we could take the trucks.
Alright, let's just take the trucks.
"""

"""
What happens if multiple elif blocks are True?
Python starts and the top runs the first block that is True, so it will run only the first one.
"""

#Study Drills
#2. Change the numbers of cars, people, and trucks and then trace through each if-statement to see what will be printed.
'''
people = 3 
cars = 4
trucks = 5


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

Output ->
We should take the cars.
That's too many trucks.
Fine, let's stay home then.
'''

#3. Try some more complex boolean expressions like cars > people or trucks < cars.
'''
people = 3
cars = 4
trucks = 5


if cars > people or cars > trucks:
    print "We should take the cars."
elif cars < people and cars == trucks:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars or trucks > people:
    print "That's too many trucks."
elif trucks < cars and trucks == people:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks and people == cars:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

Output ->
We should take the cars.
That's too many trucks.
Fine, let's stay home then.
'''

#4. Above each line write an English description of what the line does.
'''
#Initialization of various values
people = 30
cars = 40
trucks = 15

#If cars are greater than people, the below print statement is printed
if cars > people:
    print "We should take the cars."
#If cars are less than people, the below print statement is printed
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

#If trucks are greater than cars, the below print statement is printed
if trucks > cars:
    print "That's too many trucks."
#If the trucks are less than cars, the below print statement is printed
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

#If the people are greater than trucks, the below print statement is printed
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
'''
