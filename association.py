dict1={}

dict1["boy"]="jeremiah"
dict1["boy1"]="claude"
dict1["boy2"]="joshua"
dict1["boy3"]="semaj"
dict1["boy1"]="tony"

del dict1["boy1"]




# def add(x, y, func, a):
#     print(func(x, y)+a)



def decorator(func):
    def inner(x, y):
        print("this is it")
        mult1=func(x,y)
        print(mult1*100)
    return inner
@decorator
def mult(x, y):
    return x*y

mult(4,5)

#-----------association-------------
class Manager():
    def __init__(self, class_obj):

        self.swipe=class_obj()




class Swipe_Card():
    def __init__(self):
        pass

    def swipe(self, word):
        print(f"I swipped for a  {word}")

    def card_name(self, name):
        print(name)



income =[34, 56, 7]

man1=Manager( Swipe_Card)
man1.swipe.swipe("word")
swipped=Swipe_Card()
swipped.card_name("placate")
print(dict1)
print(dict1["boy3"])