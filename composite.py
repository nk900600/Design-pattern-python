

class Clinic:

    def show(self):
        pass

    def add(self,obj):
        pass

    def remove(self,obj):
        pass

    def display(self):
        pass


class Patient(Clinic):

    def show(self):
        print("patient")

class Medicine(Clinic):

    def show(self):
        print("medicine")

class Hospital(Clinic):

    def __init__(self):
        self._Clinic= []

    def add(self,obj):
        if isinstance(obj,Clinic) and obj not in self._Clinic:
            self._Clinic.append(obj)

    def remove(self,obj):
        del self._Clinic[obj]

    def display(self):
        for i in self._Clinic:
            i.show()


c = Hospital()

c.add(Patient())
c.display()

