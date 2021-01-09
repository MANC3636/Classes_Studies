

class Parent:
    def delegate(self):
        self.other="other"
        self.delegated_action()
    def delegated_action(self):
        self.lost="lost"
        assert False, "delegated action not yet defined "

class Slaved_Class(Parent):
    def delegated_action(self):
        self.name="cat"

        print("Parent delegated my "
              "responsibilities to Slaveed_Class")

lazy_parent=Slaved_Class()
lazy_parent.delegate()

print(lazy_parent.__dict__)
