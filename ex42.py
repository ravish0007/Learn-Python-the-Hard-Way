## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a Object
class Person(object):

    def __init__(self, name):
        ## Parson has-an name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## frank is-a Employee and his salary is 120000
frank = Employee("Frank", 120000)

## frank's pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

'''
What does super(Employee, self).__init__(name) do?
That's how you can run the __init__ method of a parent class reliably. Search for "python super" and read the various advice on it being evil and good for you.

Python always requires (object) when you make a class. Save your brain power for something important.
class Fish(object):
    pass
'''
