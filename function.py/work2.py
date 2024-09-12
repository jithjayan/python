
emp=[]
def login():
    usern=input("Enter user name:")
    passw=input("Enter password:")
    f=0
    if usern == 'admin' and passw =='admin':
        f=1
    return f
def add_emp():
    id=int(input("Enter the id"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            add_emp()
    if f1==0:
        name=input("Enter the name:")
        age=int(input("Enter the age:"))
        sal=int(input("Enter the salary:"))
        dob=input("Enter dob")
        pos=str(input("enter the position"))
        emp.append({'id':id,'name':name,'age':age,'sal':sal,'dob':dob,'pos':pos})

while True:
    print('''
          1.login
          2.exit''')
    ch = int(input('Enter the choice:'))
    if ch==1:
       f=login()
       if f==1:
           while True:
               print('''
                     1.Add emp
                     2.view
                     3.upate
                     4.delete
                     5.logout''')
               sub_ch=int(input("Enter the choice:"))
               if sub_ch==1:
                   add_emp()
       else:
           print('invalid user name or password')