# class syn:
#     def python():
#         print("Python")
#     def java():
#         print("Java")
#     def php():
#         print("PHP")
# manu=syn
# manu.python()
# akhil=syn
# akhil.java()



class bank:
    def __init__(s):
        s.name=input('name')
        s.age=int(input('age'))
        s.bal=0

    def deposite(self,amt):
        self.bal+=amt
        print('deposite done')
    def withdraw(self,amt):
        self.bal-=amt
        print('withdraw')
    def balance(self):
        print('balance',self.bal)
obj=bank()
obj.deposite(5000)
obj.balance()
obj.withdraw(2000)
obj.balance()
print(obj.bal)

obj1=bank()
obj1.deposite(100)
obj1.balance()

