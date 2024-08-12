slry=int(input("Enter the salary :"))
serv=int(input("Enter year of service :")) 
print("salary without bonus",slry)
if serv > 5 :
    a=(5/100)*slry
    nslry=a+slry
    print("New salary :",nslry)
else:
    print("No bonus") 