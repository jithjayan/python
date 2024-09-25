# f=open('demo.txt','x')
# f.write('welcome \n')
# f.write('123\n')
# f.write('python\n')


f=open('demo.txt','r')
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


a=f.readlines()
l=len(a)
f.seek(0)
for i in range(l):
    b=f.readline().strip()
    c=len(b)
    print(c)
    