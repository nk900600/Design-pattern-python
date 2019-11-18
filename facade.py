"""


Facade - a pattern that structures objects.


Provides a unified interface instead of a set of interfaces of a subsystem.


The facade defines a higher-level interface that simplifies the use of the subsystem.


"""


class Paper:
    """ Paper """

    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print(text)


class Printer:
    """ Printer """

    def error(self, msg):
        print(' Error: % s ' % msg)

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error(' Paper is out ')


class Facade:

    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print_(self._paper, text)


f = Facade()
f.write(' Hello world! ')  # Hello world!
f.write(' Hello world! ')  # Error: Paper has run out
