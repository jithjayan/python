num={0:'zero',1:'one',2:'two',3:'Three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter a number"))
while a<10:
    b=a%10
    a=a//10
    print(a)
