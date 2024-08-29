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
        f=0
        for i in emp:
            if id in i:
                while True:
                    print('''        1.salary
        2.position
        3.experiance
        4.exit''')
                    
                    op=int(input("Enter the input: "))
                    if op==1:
                        slry=int(input("enter salary"))
                        i[4]=slry
                        f=1
                    elif op==2:
                        pos=str(input("Enter the position"))
                        i[5]=pos
                        f=1
                    elif op==3:
                        exp=int(input("Enter the experiance"))
                        i[6]=exp
                        f==1
                    elif op==4:
                        break
                    else:
                        print("invalid input")   
        if f==0:
            print("id not found")
    elif op==4:
        id=int(input("Enter the id"))
        f=0
        for i in emp:
            if id in i:
                emp.remove(i)
                f=1
        if f==0:
                print("id not found")
    elif op==5:
        id=int(input("enter the id"))
        f=0
        import datetime
        for i in emp:
            if id in i:
                task=str(input("enter the task"))
                date=datetime.datetime.now().strftime('%x')
                i.append([task,date])
                f=1
        if f==0:
                print("id not found")
    elif op==6:
        id=int(input("enter the id"))
        f=0
        for i in emp:
            if id in i:
                print(i)
                f=1
        if f==0:
                print("id not found")
    elif op==7:
        break
    else:
        print("invalid input")


            

                 