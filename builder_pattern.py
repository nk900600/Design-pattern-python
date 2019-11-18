class Builder:
    def getdrinks(self): pass

    def getsandwich(self): pass

    def getfries(self): pass


class Drinks:
    drink =None


class Sandwich:
    sandwich = "foot long"


class Fries:
    fries = "french fries"


class Coke(Builder):

    def getdrinks(self):
        drink = Drinks()
        drink.drink ="rfrf"
        return drink

    def getsandwich(self):
        sandwich = Sandwich()
        z = sandwich.sandwich
        return z

    def getfries(self):
        fries = Fries()
        # z = fries.fries
        return fries


class Franchise:

    def __init__(self):
        self._drinks = None
        self._sandwich = None
        self._fries = None

    def setdrinks(self, drink):
        self._drinks = drink

    def setsandwich(self, sandwich):
        self._sandwich = sandwich

    def setfries(self, fries):
        self._fries = fries

    def __str__(self):
        # print(dir(self._fries))
        print("body: %s" % self._fries.fries)


class Director:

    _builder= None

    def setBuilder(self,builder):
        self._builder=builder

    def setFranchise(self):

        # for drinks
        franchise= Franchise()
        drink= self._builder.getdrinks()
        franchise.setdrinks(drink)

        # for sandwich

        sandwich= self._builder.getsandwich()
        franchise.setsandwich(sandwich)

        # for fries
        fries= self._builder.getfries()
        franchise.setfries(fries)

        return franchise


dir_= Director()
fran= Coke()

dir_.setBuilder(fran)
fr =dir_.setFranchise()
fr.__str__()




