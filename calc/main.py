from numin import *
from add import *
from sub import *
from mul import *
from div import *
from mod import *
while True:
    print('''
          1.add
          2.sub
          3.mult
          4.div
          5.mod
          6.exit''')
    ch=int(input("Enter the choice"))
    if ch==1:
        a,b=num()
        add(a,b)
    elif ch==2:
        a,b=num()
        sub(a,b)
    elif ch==3:
        a,b=num()
        mul(a,b)
    elif ch==4:
        a,b=num()
        div(a,b)
    elif ch==5:
        a,b=num()
        mod(a,b)
    elif ch==6:
        break
    else:
        print("Invalid choice")
    




