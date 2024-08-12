nu=int(input("Enter the number of units :"))

if nu <=100:
    print("The number of unit is less than 100")
elif nu>100 and nu <=200:
    unit=nu-100
    np=unit*5
    print("Charge is",np)
else:
     
     bunit=nu-200
     cunit=bunit*10
     lp=cunit+500
     print("Charge is",lp) 
