lb=[]
while True:
    print('''
          1.Add a book
          2.Update
          3.Remaove
          4.view
          5.search
          6.exit''')
    num=int(input("Enter the input"))
    if num==1:
        name=str(input("Enter book name"))
        author=str(input("Enter book author"))
        price=int(input("Enter book price"))
        id=int(input("enter athe id"))
        qnty=int(input("Enter the quantity"))
        lb.append({'bname':name,'bauthor':author,'bprice':price,'pid':id,'quantity':qnty})
    elif num==2:
        a=int(input("Enter the id"))
        for i in lb:
            f=0
            if i['pid']==a:
                while True:
                    print('''
                        1.price
                        2.quantity
                        3.exit''')
                    num=int(input("Enter the input"))
                    if num==1:
                        nprice=int(input("Enter the new price"))
                        i['bprice']=nprice
                        f=1
                    elif num==2:
                        nqnty=int(input("Enter the new quantity"))
                        i['quantity']=nqnty
                        f=1
                    elif num==3:
                        break
                    else:
                        print("Invalid input")
        if f==0:
            print("Invalid id")
    elif num ==3:
        a = int(input("Enter the id"))
        for i in lb:
            f = 0
            if i['pid'] == a:
                lb.remove(i)
                f = 1
        if f==0:
            print("Invalid id")
    elif num==4:
        for i in lb:
            print(i)
    elif num==5:
        a=int(input("Enter the id"))
        f=0
        for i in lb:
            if i['pid']==a:
                print(i)
                f=1
        if f==0:
            print("Invalid id")
    elif num==6:
        break
    else:
        print("Invalid input")
            




