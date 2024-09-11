def num():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    return a,b
def add():
    a,b=num()
    print(a+b)
def sub():
    a,b=num()
    print(a-b)
while True:
    print('''
1.Addition
2.Subtract
3.Multiply
4.Divide
5.Exit''')
    ch=int(input("enter your choice"))
    if ch==1:
        add()
    elif ch==2:
      sub()
    elif ch==3:
        a,b=num()
        print(a*b)
    elif ch==4:
        a,b=num()
        print(a/b)
    elif ch==5:
        break
    else:
        print("invalid choice")
