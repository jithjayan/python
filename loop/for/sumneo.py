a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
sum=0
even=0
odd=0
for i in range(a,b+1):
    sum=sum+i
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(sum)
print(even)
print(odd)        
        