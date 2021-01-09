import turtle as t
t1=t.Pen()

def letter_a():
    t1.circle(50)
    t1.up()
    t1.left(65)
    t1.fd(90)
    t1.right(125)
    t1.down()
    t1.fd(90)


def space(angle=55, distance=50):
    t1.lt(angle)
    t1.up()
    t1.fd(distance)
    t1.rt(-94)
    t1.down()

def letter_i():
    t1.left(90)#turn 90 degrees
    t1.fd(50)
    #let's make the dot
    t1.up()
    t1.fd(10)
    t1.color("red")
    t1.down()
    t1.circle(5)

def letter_t():
    t1.pensize(10)
    t1.left(90)#turn 90 degrees
    t1.fd(90)
    #let's cross the t
    t1.up()
    t1.lt(90)
    t1.back(-90)
    t1.color("blue")
    t1.rt(180)
    t1.down()
    t1.fd(180)


def letter_c():
    t1.fd(80)
    t1.up(), t1.left(90),
    t1.fd(100)
    t1.down(), t1.left(90)
    t1.fd(80)
    t1.left(90)
    t1.fd(100)





#print("what follows is the Amy object")
class Mostly_Vowels:
    def __init__(self,letter1, letter2):
        self.vowel1=letter1
        self.vowel2=letter2
        self._c=Soft_Consonants(letter_c)#instantiate in the init function

    def show_letter_a(self):
        self.vowel1()

    def show_letter_i(self):
        self.vowel2()

    def show_letter_c(self):
        self._c.show_letter_c1()

    def space(self,  distance=0, angle2=0, angle=0):
        t1.up()
        t1.left(angle)
        t1.fd(distance)
        t1.left(angle2)
        t1.down()

class Hard_Consonants(Mostly_Vowels):#notice use of parameter
    def __init__(self, letter3):
        Mostly_Vowels.__init__(self, letter_a, letter_i)#notice we call the vowel class init function
        self.t=letter3

    def show_letter_t(self):
        self.t()

class Soft_Consonants:#notice use of parameter
    def __init__(self, letter4):
        self.c=letter4

    def show_letter_c1(self):
        self.c()





vowel=Mostly_Vowels(letter_a, letter_i)
vowel.show_letter_c()
cs=Soft_Consonants(letter_c)
cs.show_letter_c1()
# word1=Hard_Consonants(letter_t)
# word1.show_letter_t()
# word1.space(12, 45, 100)#does Hard Consonant have a space function
# word1.show_letter_a()#does Hard Consonant have a show_letter function

print(dir(t))

t.mainloop()
