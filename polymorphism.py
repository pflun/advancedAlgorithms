class Animal(object):
    def run(self):
        print 'Animal is running...'

# inheritance
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

# polymorphism
def polyrun(animal):
    animal.run()

test = Dog()
print test.run()
print isinstance(test, Animal)
print polyrun(Animal())