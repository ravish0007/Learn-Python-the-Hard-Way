class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

"""
Why do I need self when I make __init__ or other functions for classes?
If you don't have self, then code like cheese = 'Frank' is ambiguous. That code isn't clear about whether you mean the instance's cheese attribute, or a local variable named cheese. With self.cheese = 'Frank' it's very clear you mean the instance attribute self.cheese.
"""

"""
Study Drills
2. Put the lyrics in a separate variable, then pass that variable to the class to use instead.
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

lyrics1 = ["Happy birthday to you",
           "I don't want to get sued",
           "So I'll stop right there"]

lyrics2 = ["They rally around tha family",
           "With pockets full of shells"]

happy_bday = Song(lyrics1)

bulls_on_parade = Song(lyrics2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
"""
