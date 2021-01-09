
import pygame
class Gaming_Template:
    def __init__(self):
        self.attribute1=None
        self.mapping_attribute=Map()#1

    def do_something(self):
        print("I'm doing something")

    def mapping(self):
        self.mapping_attribute.display()#2

#using map to show "has a" relationship
class Map:
    def __init__(self):
        self.Chicago=None

    def display(self):
        print("I am a map of Chicago being displayed")

#using Game_Sound to show "is a" relationship
class Game_Sound(Gaming_Template):#1
    def __init__(self):#3
        Gaming_Template.__init__(self)#2
        self.attribute=None

    def sound(self):
        print("I am a game with sound")



plane1=Gaming_Template()
#plane1.do_something()

game_with_sound=Game_Sound()
game_with_sound.do_something()



