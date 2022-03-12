class Parent():
    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
