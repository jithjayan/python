from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def py(self):
        print("Py")

class std(syn):
    def reg(self):
        name=input("name")
    def notes(self):
        print("notes")
class staff(syn):
    def reg(self):
        print("staff")

amal=std()
amal.reg()
staff1=staff()
staff1.reg()