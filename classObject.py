class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

class Animal:
    def run(self):
        print('Animal is running...')

    def run_twice(animal):
        animal.run()
        animal.run()

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

# bart = Student('Bart Simpson', 59)
# bart.print_score()

dog = Dog()
dog.run_twice()

print abs(-10)