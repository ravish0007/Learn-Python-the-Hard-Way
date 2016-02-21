my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

#Study Drills
#1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.

#2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
my_height = 74 # inches
my_weight = 180 # lbs

my_height_cms = 74 * 2.54 # centimeters
my_weight_kgs = 180 * 0.453592 # kilograms

#3. Search online for all of the Python format characters.
"""
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E
"""

#4. Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
# %r -> String (converts any python object using repr()).

print "\n"

#5. How can I round a floating point number?
Rounded_Var = round(1.7333);
print "Rounded_Var", Rounded_Var
