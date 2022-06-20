###Animal is-a object 

from msilib.schema import Class


class Animal(object):
    pass

##Dog is-a animal
class Dog(Animal):

    def __init__(self,name):
        #dog has-a name
        self.name = name

#Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        #cat has a name
        self.name = name


#Person is-a object
class Person(object):

    def __init__(self,name):
        #This person has-a name
        self.name = name
        
        ##person has-a pet of some kind
        self.pet = None
        

#Employee is-a person
class Employee(Person):
    ##The employee has-a name and a salary
    def __init__(self, name, salary):
        ##The employee is-a person who has-a name.
        super(Employee, self).__init__(name)
        ## The employee has a salary
        self.salary = salary

##Fish is-a object
class Fish(object):
    pass

##Salmon is a Fish
class Salmon(Fish):
    pass

##Halibut is a Fish
class Halibut(Fish):
    pass

##rover is a dog
rover = Dog("Rover")

#Satan is a cat
satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
