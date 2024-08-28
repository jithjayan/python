emp=[['aa',11,23,'zzz',1000,'bbbbb',10],['bb',12,24,'zyy',2000,'wwwww',9]]
while True:
    print('''    1.Register
    2.View
    3.Update
    4.Delete
    5.Add work
    6.Search
    7.Exit''' )
    op=int(input("Enter the input: "))
    if op==1:
        name=input("Enter the name")
        id=int(input("Enter the id"))
        age=int(input("Enter the age"))
        plc=str(input("Enter the place"))
        slry=int(input("Enter the salary"))
        pos=str(input("Enter the position"))
        exp=int(input("Enter the experiance"))
        emp.append([name,id,age,plc,slry,pos,exp])
    elif op==2:
        for i in emp:
            print(i)
    elif op==3:
        id=int(input("Enter the id"))
        if id in i:
            while True:
                print('''    1.salry
                  2.position
                  3.exp''')
                upd=int(input("enter the value"))
                if upd==1:
                    f=0
                    for i in emp:
