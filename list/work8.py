std=[]
while True:
    print(''' 
1.add std
2.view std
3.update std
4.delete std
5.exit''')
    num=int(input("Enter your input"))
    if num==1:
        name=str(input("Enter name"))
        age=int(input("Enter age"))
        mark=int(input("Enter mark"))
        std.append([name,age,mark])
    elif num==2:
        for i in std:
            print(i)
    elif num==3:
        name=str(input("Enter name"))
        f=0
        for i in std:
            if name in i:
                mark=int(input("enter mark"))
                i[2]=mark
                f=1
        if f==0:
            print("no student found")
    
    elif num==4:
        name=str(input("Enter name"))
        f=0
        for i in std:
            if name in i:
                std.remove(i)
                f=1
        if f==0:
            print("no student found")
    elif num==5:
        break
    else:
        print("invalid input")  

        

        


       
