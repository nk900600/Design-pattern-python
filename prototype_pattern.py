

class House:
    def __repr__(self):
        return str(self.__dict__)


class Duplex(House):
    def __init__(self,floor,doors):
        self.floor=floor
        self.doors=doors


class Prototype:
    def __init__(self):
        self.prototype= {}

    def register(self,object,objectname):
        self.prototype[object]=objectname

    def delete(self,object):
        del self.prototype[object]



h=House()
print(h)

d= Duplex("2",20)
print(d)