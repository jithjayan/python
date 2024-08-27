while True:
    print('''
1.add
2.sub
3.mul
4.div''')
    num=int(input("Enter your input"))
    if num==1:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a+b
        print(c)
    elif num==2:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a-b
        print(c)
    elif num==3:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a*b
        print(c)
    elif num ==4:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a/b
        print(c)
    elif num==5:
        break
    else:
        print("Invalid input")
    