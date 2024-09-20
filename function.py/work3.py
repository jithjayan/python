user=[]
lib=[]
def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    email=input("Enter the email")
    f=0
    for i in user:
        if i['email']==email:
            f=1
            register()
    if f==0:
        name=str(input("Enter your name"))
        username=email
        phone=int(input("Enter the ph number"))
        pword=input("enter the password")
        user.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'pword':pword})

def login():
    username=input("enter username")
    pword=(input("enter password"))
    f=0
    if username=='admin' and pword=='admin':
        f=1
    user=''
    for i in user:
        if username==i['email'] and pword==i['pword']:
            f=2
            user=i
    return f,user

def add_book():
    if len(lib)==0:
        id=1001
    else:
        id=lib[-1]['id']+1
    f=0
    for i in lib:
        
        bname=str(input("Enter the book name"))
        price=int(input("enter the price"))
        stock=int(input("Enter the stock"))
        lib.append({'id':id,'bname':bname,'price':price,'stock':stock})

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
        elif f==2:
            print("user login")
        elif f==0:
            print("invalid username or password")
