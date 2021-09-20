class Animal:
    counter = 0
    def voice(self):
        pass
    def count():
        print('Current population of animals: %s animals' % Animal.counter)

class Behemoth(Animal):
    def __init__(self, name):
        self.name = name
        Animal.counter += 1
    def voice(self):
        print("I'm a behemoth with name %s" % self.name)

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        Animal.counter += 1
    def voice(self):
        print("I'm a dog with name " + self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        Animal.counter += 1
    def voice(self):
        print("I'm a cat with name " + self.name)

Big = Behemoth('Big')
Big.voice()

Snuppy = Dog('Snuppy')
Snuppy.voice()

Kitty = Cat('Kitty')
Kitty.voice()

Animal.count()