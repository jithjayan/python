shop=[]
user=[]
def reg():
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input("enter email"))
    f=0
    for i in user:
        if ['email']==email:
            f=1
            print("email already exist")
    if f==0:
        name=str(input("Enter name"))
        ph=int(input("Enter ph"))
        password=input("enter password")
        user.append({'id':id,'name':name,'ph':ph,'email':email,'password':password})
    print("registered")

def login():
    usern=str(input('Enter Username : '))
    passw=input('Enter password : ')
    f=0
    u=''
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add_prdt():
    print('ADD PRODUCTS')
    if len(shop)==0:
        id=1
    else:
        id=shop[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    shop.append({'id':id,'name':name,'price':price,'stock':stock})

def update_prdt():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')


def delete_prdt():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            shop.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')

def view_prdt():
    print('BOOK DETAILS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','PRODUCT','PRICE','STOCK'))
    print('_'*30)
    for i in shop:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def search():
    qa=int(input("enter the id"))
    for i in shop:
        if i['id']==qa:
            print(i)
        

while True:
    print('''
1.Register
2.Login
3.Exit''')
    ch=int(input("Enter the choice"))
    if ch==1:
        reg()
    elif ch==2:
       f,u=login()
       if f==1:
            while True:
                print('''
                1.Add products
                2.Update product
                3.Delete product
                4.Logout''')

                ab=int(input('enter your choice : '))
                if ab==1:
                    add_prdt()
                elif ab==2:
                    update_prdt()
                elif ab==3:
                    delete_prdt()
                elif ab==4:
                    break
                else:
                    print('invalid Choice')
       elif f==2:
            while True:
                print('''
                      1.search
                    2.view products
                    3.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    search()
                elif c1==2:
                    view_prdt()
                elif c1==3:
                    break
                else:
                    print('invalid option')
       else:
            print('invalid username or password.') 