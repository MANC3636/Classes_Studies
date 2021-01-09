
"""A study in polymorphism"""
class Worker:
    def __init__(self):
        None

    def speak(self, *args, **kwargs):#not using kwargs
        print("I am a {}". format(args[0]))
        print("You want to know what I do? I {}".format(args[1]))


class Worker_Type1(Worker):
    def __init__(self): None



class Worker_Type2(Worker):
    def __init__(self): None

# #instantiate our workers
waiter=Worker_Type1()
concierge=Worker_Type2()
#
# #call the speak method/function
waiter.speak("waiter", "wait tables")
print()
concierge.speak("concierge", "greet guests and ensure their comfort")