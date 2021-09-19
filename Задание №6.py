class Animal:
    def voice(self):
        pass

class Behemoth(Animal):
    def voice(self):
        print("I'm a behemoth")

class Dog(Animal):
    def voice(self):
        print("I'm a dog")

class Cat(Animal):
    def voice(self):
        print("I'm a cat")

behemoth = Behemoth()
behemoth.voice()

dog = Dog()
dog.voice()

cat = Cat()
cat.voice()