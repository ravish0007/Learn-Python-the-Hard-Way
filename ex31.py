print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"

#Study Drills
#1. Make new parts of the game and change what decisions people can make. Expand the game out as much as you can before it gets ridiculous.
"""
print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear
        print "Do you want to play another game?"

        play = raw_input("> ")

        if play == "yes":
                print "What do you like darkness"
                dark = raw_input("> ")
        elif play == "no":
                print "Why do you hate darkness"
                dark = raw_input("> ")
        else:
                print "May the darkness consume you"

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
"""

#2. Write a completely new game. Maybe you don't like this one, so make your own. This is your computer, do what you want.
"""
print 'Pick one colour'
print'''
\t*Red
\t*Blue
\t*Green
\t*Yellow
'''

colour = raw_input("> ")

if colour == "Red":
        print "Alone. Yes, that's the key word, the most awful word in the English tongue. Murder doesn't hold a candle to it and hell is only a poor synonym."

elif colour == "Blue":
        print "The sky grew darker, painted blue on blue, one stroke at a time, into deeper and deeper shades of night."

elif colour == "Green":
        print "I had a dream about you. I said green was blue and yellow, and you said green was yellow and blue. You were like that with everything I said, taking the exact opposite stance, yet completely agreeing with me. That is how $

elif colour == "Yellow":
        print "I write on big yellow legal pads - ideas in outline form when I'm doing stand-up and stuff. It's vivid that way. I can't type it into an iPad - I think that would put a filter into the process."
else:
        print "All you had to do was choose a colour...."
"""

"""
How do I tell if a number is between a range of numbers?
You have two options: Use 0 < x < 10 or 1 <= x < 10, which is classic notation, or use x in range(1, 10).

Can you replace elif with a sequence of if-else combinations?
You can in some situations, but it depends on how each if/else is written. It also means that Python will check every if-else combination, rather than just the first false ones like it would with if-elif-else. Try to make some of these to figure out the differences.
"""
