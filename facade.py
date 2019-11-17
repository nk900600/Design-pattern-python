class Paper:
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print(text)
        # else:
        #     return "ran out of paper"


class Printer(object):
    """ Printer """

    def error(self, msg):
        print(' Error: % s ' % msg)

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error(' Paper is out ')


class Facade(object):
    def __init__(self,int_):
        self._printer = Printer()
        self._paper = Paper(int_)

    def write(self, text):
        self._printer.print_(self._paper, text)


f = Facade(10)
for i in range(11):

    f.write(' Hello world! ')  # Hello world!
# f.write(' Hello world! ')  # Error: Paper has run out
