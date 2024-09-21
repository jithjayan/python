userl=[{'id': 102, 'name': 'sn', 'email': 'sw','phone': 9112, 'pword': 'dd','book':[]}]
lib=[{'id': 1001, 'name': 'aa', 'price': 20, 'stock': 2}]
def register():
    if len(userl)==0:
        id=101
    else:
        id=userl[-1]['id']+1
    email=str(input("Enter the email"))
    f=0
    for i in userl:
        if i['email']==email:
            f=1
            register()
    if f==0:
        name=str(input("Enter your name"))
        phone=int(input("Enter the ph number"))
        pword=input("enter the password")
        userl.append({'id':id,'name':name,'email':email,'phone':phone,'pword':pword,'book':[]})

def login():
    username=str(input("enter username"))
    pword=input("enter password")
    f=0
    if username=='admin' and pword=='admin':
        f=1
    user=''
    for i in userl:
        if username==i['email'] and pword==i['pword']:
            f=2
            user=i
    return f,user

def add_book():
    if len(lib)==0:
        id=1001
    else:
        id=lib[-1]['id']+1
        
        bname=str(input("Enter the book name"))
        price=int(input("enter the price"))
        stock=int(input("Enter the stock"))
        lib.append({'id':id,'bname':bname,'price':price,'stock':stock})
def view_book():
    print('BOOK DETAILS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','BOOKNAME','PRICE','STOCK'))
    print('_'*30)
    for i in lib:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))
def update_book():
    print()
def delete_book():
    print()
def view_user():
    print()
def view_pro(user):
    print(user)

def lend_book(user):
    id=input("Enter id")
    f=0
    for i in lib:
        if id==i['id']:
            f=1
            i['stock']-=1
            user['book'].append(id)
    if f==0:
        print("book not found")

def update_pro():
    

while True:
    print('''
          1.registration
          2.login
          3.exit''')
    ch=int(input("Enter your choice"))
    if ch==1:
        register()
    elif ch==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                      1.add book
                      2.view book
                      3.update book
                      4.delete book
                      5.view user
                      6.exit''')
                num=int(input("enter your choice"))
                if num==1:
                    add_book()
                elif num==2:
                    view_book()
                elif num ==3:
                    update_book()
                elif num==4:
                    delete_book()
                elif num==5:
                    view_user()
                elif num==6:
                    break
                else:
                    print("invalid choice")

        elif f==2:
            while True:
                print('''
                      1.view profile
                      2.view book
                      3.lend book
                      4.update profile
                      5.exit''')
                num=int(input("enter your choice"))
                if num==1:
                    view_pro(user)
                elif num==2:
                    view_book()
                elif num==3:
                    lend_book(user)
                elif num==4:
                    update_pro()
        else:
            print("invalid username or password")
