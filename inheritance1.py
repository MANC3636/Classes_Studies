

class Mammal:
    def __init__(self):
        self.size=100

    def move(self):
        print("moving")




class Squirrel(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        self.energy=7
        self.hunger=5

    def move(self):
        print("I'm  a big squirrel and I can move myself")

    def sleep(self):
        print("I like to sleep, perchance to dream")

small_squirrel=Squirrel()
small_squirrel.move()