# def sample():
#     print("welcome")
#     print("welcome1")
#     print("welcome2")
# a=[1,2,3,4,5]
# print(a)
# sample()
# a=[1,2,3,4,5]
# print(a)
# sample()


# def sample():
#     b=0
#     print("number b=",b)
#     print("nunber a=",a)
# a=1
# sample()
# print("number a=",a) 
# print("number b=",b)  


# def sample():
#     a=0
#     print("nunber a=",a)
# a=1
# sample()
# print("number a=",a) 


# def sample():
#     print("welcome")
#     print("welcome1")
#     print("welcome2")
# a=[1,2,3,4,5]
# print(a)
# sample()
# a=[1,2,3,4,5]
# print(a)
# sample()


# def sample():
#     b=0
#     print("number b=",b)
#     print("nunber a=",a)
# a=1
# sample()
# print("number a=",a) 
# print("number b=",b)  


# def sample():
#     a=0
#     print("nunber a=",a)
# a=1
# sample()
# print("number a=",a) 

# def sample():
#     global a
#     a=10
#     print("number a=",a)
# sample()
# print(a)    


# def sample():
#     a=10
#     b=11
#     return 'hi',a,b
# # print(sample())
# a,b,c=sample()
# print(a)
# print(b)
# print(c)

# def sample(a,b):
#     print(a,b)
# sample(10,20)
# sample('abc',20)
# sample(['abc',20],20)


# def sample(name,age):
#     print("name",name)
#     print("age",age)
# sample(age=20,name='awu')    


# def sample(name='aqw',age=20):
#     print(name,age)
# sample("awi")
# sample("sawq",22)
# sample()


# def sample(*a):
#     print(a)
# sample()
# sample('hello','world')
# sample('hello','world',11.12)


# def sample(**a):
#     print(a)
# sample()
# sample(name='aqw',age=20)
# sample(name='aqw',age=20,ph=111111)



'''map'''

l=[1,2,3,4,5]
# print(list(map(lambda x:x*2,l)))

def num(x):
    return x+2
print(list(map(num,l)))