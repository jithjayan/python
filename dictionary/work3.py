num={0:'zero',1:'one',2:'two',3:'Three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter a number"))
s=''
while a>0:
    b=a%10
    s=num[b]+' '+s
    a=a//10
print(s)
