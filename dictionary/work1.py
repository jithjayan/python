p=[]
while True:
    print('''          1.add product
          2.view product
          3.update product
          4.delete product
          5.exit''')
    num=int(input("enter the input"))
    if num==1:
        name=str(input("enter product name"))
        id=input("enter product id")
        price=int(input("enter product price"))
        p.append({'pname':name,'pid':id,'pprice':price})
    elif num==2:
            for i in p:
                print(i['pname'],i['pid'],i['pprice'])
    elif num==3:
         a=input('enter product id')
         for i in p:
              f=0
              if i['pid']==a:
                   nprice=input("enter new price")
                   i['pprice']=nprice
                   f=1               
         if f==0:
              print("product not found")
    elif num==4:
         a=input('enter product id')
         for i in p:
              f=0
              if i['pid']==a:
                   p.remove(i)
                   f=1
         if f==0:
              print("product not found")
    elif num==5:
         break
    else:
         print("invalid input")

     