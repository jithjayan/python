# f=open('demo.txt','x')
# f.write('welcome \n')
# f.write('123\n')
# f.write('python\n')


# f=open('demo.txt','r')
# a=f.read()
# print(a)

# f.seek(0)
# b=f.read(5)
# print(b)

# a=f.readline()
# print(a)
# b=f.readline()
# print(b)
# c=f.readline()
# print(c)

# a=f.readline(5)
# print(a)
# b=f.readline()
# print(b)

# a=f.readlines()
# print(a)
# print(len(a))
# print(f.tell())

# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     # print(b)
#     print(b[::-1])


# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     c=len(b)
#     print(c)
    
# l=f.readlines()
# letter=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     for i in b:
#         if i !=' ':
#             letter+=1
#     print(letter)


# l=f.readlines()
# letter=0
# s=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     for i in b:
#         if i !=' ':
#             letter+=1
#             if i.islower():
#                 s+=1

# print('small',s)
# print('cap',letter-s)

# l=f.readlines()
# words=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     for i in b:
#         if i==' ':
#             words+=1
# words+=1
# print(words)

        

# l=f.readlines()
# w=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     a=b.split(' ')
#     for j in a:
#         if j!='':
#             w+=1
# print(w)
# f=open('demo.txt','w')
# f.write('hello\n')
# f.write('alliens\n')
# f.write('welcome  '+'here')


# f=open('demoo.txt','w')
# f.write('hello\n')
# f.write('alliens\n')
# f.write('welcome  '+'here')

# f=open('demoo.txt','w')
# num=int(input("enter the number"))
# if num>0:
#     for i in range(1,11):
#         q=(num*i)
#         print(q)
#         f.write(str(q)+'\n')
        

# num=int(input("Enter the number"))
# if num>0:
#         for j in range(1,11):
#             for i in range(1,num+1):
#                 f.write(f'{j}*{i}={i*j}\t')
#             f.write('\n')
                
# f=open('demo.txt','a')
# f.write('java')

# f=open('demo1.txt','x')
# import os 
# os.remove('demo1.txt')

# if os.path.exists('demo1.txt'):
#     os.remove('demo1.txt')
# else:
#     print('not found')


#date and time


# import datetime
# x=datetime.datetime.now().strftime('%a')
# a=datetime.datetime.now().strftime('%A')
# b=datetime.datetime.now().strftime('%d')
# c=datetime.datetime.now().strftime('%b')
# d=datetime.datetime.now().strftime('%B')
# e=datetime.datetime.now().strftime('%y')
# f=datetime.datetime.now().strftime('%Y')
# print(x,a,b,c,d,e,f)

# math


import math

print(math.ceil(11.2))
print(math.floor(11.5))
print(math.factorial(5))
print(math.sqrt(4))

