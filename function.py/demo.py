def register():
    print('Registration Page')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'book':[]})

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

def add_bk():
    print('ADD BOOK')
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    lib.append({'id':id,'name':name,'price':price,'stock':stock,})

def view_bk():
    print('BOOK DETAILS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','BOOKNAME','PRICE','STOCK'))
    print('_'*30)
    for i in lib:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def update_bk():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')

def delete_bk():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            lib.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')

def view_usr():
    print('USERS DETAILS')
    print("{:<10}{:<15}{:<15}{:<15}".format('ID','NAME','EMAIL','PHONE'))
    print('_'*55)
    for i in user:
        print("{:<10}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email'],i['phone']))

def view_pro(u):
    print('NAME : ',u['name'])
    print('ID : ',u['id'])
    print('Email : ',u['email'])
    print('Phone : ',u['phone'])
    print('Password : ',u['password'])
    print('Books : ',u['book'])



def update_usr(u):
    phone=int(input('enter your number : '))
    password=input('enter new password')
    u['phone']=phone
    u['password']=password
    print('updated')

def rent(u):
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            f=1
            i['stock']-=1
            u['book'].append(id)
            print('book added')
    if f==0:
        print('invalid ID')

def return_bk(u):
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id and id in u['book']:
            f=1
            i['stock']+=1
            u['book'].remove(id)
            print('book removed')
    if f==0:
        print('invalid ID')

def bkhnd(u):
    print(u['book'])

# Fuctions end

user=[{'id': 1000, 'name': 'sajan', 'email': 's@','phone': 920712, 'password': 'asdf','book':[1,2]}]
lib=[{'id': 1, 'name': 'aa', 'price': 20, 'stock': 2},{'id': 2, 'name': 'ab', 'price': 200, 'stock': 2}]
while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()
        if f==1:
            while True:
                print('''
                1.Add book
                2.View Book
                3.Update Book Details
                4.Delete book
                5.View Users
                6.Logout''')

                c1=int(input('enter your choice : '))
                if c1==1:
                    add_bk()
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_bk()
                elif c1==4:
                    delete_bk()
                elif c1==5:
                    view_usr()
                elif c1==6:
                    break
                else:
                    print('invalid Choice')
        elif f==2:
            while True:
                print('''
                    1.view profile
                    2.view book
                    3.update profile
                    4.Rent a book
                    5.Return a book
                    6.Books in hand
                    7.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_pro(u)
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_usr(u)
                elif c1==4:
                    rent(u)
                elif c1==5:
                    return_bk(u)
                elif c1==6:
                    bkhnd(u)
                elif c1==7:
                    break
                else:
                    print('invalid option')
        else:
            print('invalid username or password')
    elif c==3:
        break
    else:
        print('Invalid Choice')