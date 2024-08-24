l=[1,10,12,'abc',8.5]
sum=0
for i in (l):
    if type(i)==int or type(i)==float:
        sum=sum+i
print(sum)
