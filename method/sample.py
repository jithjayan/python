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

f=open('demoo.txt','w')
num=int(input("enter the number"))
if num>0:
    for i in range(1,11):
        q=(num*i)
        print(q)
        f.write(str(q)+'\n')
        