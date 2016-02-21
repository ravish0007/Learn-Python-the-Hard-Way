from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"
    print "Enter a number between 0 and 50:"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print "1. take honey"
    print "2. taunt the bear"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "2" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means. please type 1 or 2"


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Game Over!"
    print "Do you want to play again -> Y or N ?"
    play = raw_input("> ")
    if play == "Y" or play == "y":
	start()
    else: 
	exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    print "1. L or l or left"
    print "2. R or r or right"

    choice = raw_input("> ")

    if choice == "left" or choice == "l" or choice == "L":
        bear_room()
    elif choice == "right" or choice == "r" or choice == "R":
        cthulhu_room()
    elif choice == "":
	print "Taking you to bear room"
	bear_room() 
    else:
        dead("You stumble around the room until you starve.")

start()

"""
Study Drills
1. Draw a map of the game and how you flow through it.
2. Fix all of your mistakes, including spelling mistakes.
3. Write comments for the functions you do not understand.
4. Add more to the game. What can you do to both simplify and expand it?
5. The gold_room has a weird way of getting you to type a number. What are all the bugs in this way of doing it? Can you make it better than what I've written? Look at how int() works for clues.
"""

"""
Why did you write while True?
That makes an infinite loop.

What does exit(0) do?
On many operating systems a program can abort with exit(0), and the number passed in will indicate an error or not. If you do exit(1) then it will be an error, but exit(0) will be a good exit. The reason it's backward from normal boolean logic (with 0==False is that you can use different numbers to indicate different error results. You can do exit(100) for a different error result than exit(2) or exit(1).

Why is raw_input() sometimes written as raw_input('> ')?
The parameter to raw_input is a string that it should print as a prompt before getting the user's input.
"""

"""
Map ->
-----------------------------------------------------------------
|                                      |                        |
|                                      |                        |
|           GOLD ROOM                  |                        |
|                                      |                        |
|                                      |                        |
|                                      |                        |
|-------------______-------------------|                        |
|                                      |                        |
|                                      |      Cthulhu ROOM      |
|                   BEAR ROOM          |                        |
|                                      |                        |
|                                      |                        |
|                   Left Door >        |       < Right Door     |
--------------------------------______---______------------------
|                                                               |
|                                                               |
-----------------------------------------------------------------
                                   Dark Room
"""
