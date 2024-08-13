a=int(input("Enter the bike price"))
if a>100000:
    b=(15/100)*a
    print("Tax amount is ",b)
elif a>50000 and a<100000:
    c=(10/100)*a
    print("Tax amount is ",c)
elif a<50000:
    d=(5/100)*a
    print("Tax amount is ",d)
else:
    print("Invalid input")