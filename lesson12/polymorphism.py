class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Must be imlement by a sub class')

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof!')

animals = [Cat('Marmon'), Dog('Schwarz'), Cat('Harry')]
for animal in animals:
    animal.talk()
