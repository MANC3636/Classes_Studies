class Freshman():
    def __init__(self):
        self.catalogue_read=Catalogue()

    def comment1(self):
        print("I've started school")

    def classesTaken(self):
        print("I took Trig")
        print(f"I took {self.catalogue_read.cat1} ")
        self.catalogue_read.cat_wish_list()


class Sophmore(Freshman):
    def currentClasses(self):
        print("I am taking Calc")

    def wish_list(self):
        print(f"I am a soph and would like to take {self.catalogue_read.cat2}")

class Catalogue:
    def __init__(self):
        self.cat1="English"
        self.cat2="History"
        self.cat3="Art"

    def cat_wish_list(self):
        print(f"my bucket list class is {self.cat3}")

    def func2(self):pass




#--------------delegation--------------
fresh=Freshman()
print(fresh.catalogue_read.cat1)
#------delegation can complement inheritance------
soph=Sophmore()
soph.currentClasses()
soph.classesTaken()
soph.wish_list()
soph.catalogue_read.cat_wish_list()
print(soph.catalogue_read.cat2)
print(Catalogue.__dict__)
