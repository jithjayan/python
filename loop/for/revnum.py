a=int(input("Enter a number"))
rev=0
for i in range(a):
    b=a%10
    rev=rev*10+b
    a//=10
    if a==0:
        break
print(rev)