x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#Study Drills
#1. Go through this program and write a comment above each line explaining it.

#2. Find all the places where a string is put inside a string. There are four places.
#Line 4, 9, 10, 13

#3. Are you sure there are only four places? How do you know? Maybe I like lying.

#4. Explain why adding the two strings w and e with + makes a longer string.

"""
What is the difference between %r and %s?
Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
"""
