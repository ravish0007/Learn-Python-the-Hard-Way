tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\n"

# Fun code
'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
'''

#Study Drill
#1. Memorize all the escape sequences by putting them on flash cards.
#http://learnpythonthehardway.org/book/ex10.html

#2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# See Fun code

#3. Combine escape sequences and format strings to create a more complex format.
print "There \n are \t %d types of \"people\"." % 10

print "\n"

#4. Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
print "---%r Usage---"
x = "There 'are' %d 'types' of people." % 10
print "I said: %r." % x

print "\n"

print "---%s Usage---"
x = "There 'are' %d 'types' of people." % 10
print "I said: %s." % x

"""
When I use a %r format none of the escape sequences work.
That's because %r is printing out the raw representation of what you typed, which is going to include the original escape sequences. Use %s instead. Always remember this: %r is for debugging, %s is for displaying.
"""
