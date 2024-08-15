a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
sum=0
even=0
odd=0
while a<=b:
    sum+=a
    if a%2 ==0:
        even=even+a
    else:
        odd=odd+a
    a+=1
print(sum)
print(even)
print(odd)        
        
    
    
    
        