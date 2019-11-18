class Dog(object):
    def __init__(self, name):
        self._name = name

    def bark(self):
        return ' % s : woof-woof! ' % self._name


class Cat(object):
    def __init__(self, name):
        self._name = name

    def meow(self):
        return ' % s : meow meow! ' % self._name


class CatAdapter(Dog):
    # thanks to the adapter we can use
    # interface of the `Dog` class, and the implementation of the` Cat` class.

    def __init__(self, name):
        super().__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        # request `bark` is converted to request` meow`
        return self._cat.meow()


dog = Dog(' Tuzik ')
print(dog.bark())  # Ace: woof-woof!

dog = CatAdapter(' Tuzik ')
print(dog.bark())  # Tuzik: meow-meow!
