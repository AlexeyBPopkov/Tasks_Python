class Animal:
    def voice(self):
        pass

class Behemoth(Animal):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("I'm a behemoth with name " + self.name)

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("I'm a dog with name " + self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("I'm a cat with name " + self.name)

behemoth = Behemoth('Big')
behemoth.voice()

dog = Dog('Snuppy')
dog.voice()

cat = Cat('Kitty')
cat.voice()