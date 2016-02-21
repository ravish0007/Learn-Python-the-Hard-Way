ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!

#Study Drills
#1. Take each function that is called, and go through the steps for function calls to translate them to what Python does. For example, more_stuff.pop() is pop(more_stuff).
"""
ten_things.split(' ') -> split(ten_things, ' ')
more_stuff.pop() -> pop(more_stuff)
stuff.append(next_one) -> append(stuff, next_one)
stuff.pop() -> pop(stuff)
"""

#2. Translate these two ways to view the function calls in English. For example, more_stuff.pop() reads as, "Call pop on more_stuff." Meanwhile, pop(more_stuff) means, "Call pop with argument more_stuff." Understand how they are really the same thing.

#3. Go read about "object-oriented programming" online. Confused? I was too. Do not worry. You will learn enough to be dangerous, and you can slowly learn more later.

#4. Read up on what a "class" is in Python. Do not read about how other languages use the word "class." That will only mess you up.
"""
Class
A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
"""

#5. Do not worry If you do not have any idea what I'm talking about. Programmers like to feel smart so they invented object-oriented programming, named it OOP, and then used it way too much. If you think that's hard, you should try to use "functional programming."

#6. Find 10 examples of things in the real world that would fit in a list. Try writing some scripts to work with them.
"""

list1 = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"

days = list1.split(' ')

print "Days of a Week : ", days

list2 = "Red Blue Green Yellow"

colors = list2.split(' ')

print "Colors : ", colors

print "days[0]: ", days[0]
print "colors[1:2]: ", colors[1:2]

colors.append("Violet")

print "Colors after appending : ", colors

del colors[3]

print "Colors after deleting : ", colors

days.reverse()

print "Days after reversing : ", days
"""

"""
Why does join(' ', stuff) not work?
The way the documentation for join is written doesn't make sense. It does not work like that and is instead a method you call on the inserted string to put between the list to be joined. Rewrite it like ' '.join(stuff).

What does stuff[3:5] do?
That extracts a "slice" from the stuff list that is from element 3 to element 4, meaning it does not include element 5. It's similar to how range(3,5) would work.
"""
