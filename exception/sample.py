# print("anything")
# a='cr'
# b='7'
# try:
#     print(a+b)
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("nothing")


# while True:
#     print('''
#           1.add
#           2.sub
#           3.mul
#           4.div ''')
#     while True:
#         try:
#             num=int(input("enter the number"))
#             break
#         except:
#             pass
#     if num==1:
#         print('add')
#     if num==2:
#         print('sub')


# l=[1,2,3,25,'abc']
# sum=0
# for i in l:
#     try:
#         sum+=i
#     except:
#         pass
# print(sum)  
    

l=['qwerty',1,2,'book',3,'paper','pen']
for i in l:
    try:
        a=i[::-1]
        print(a)
    except:
        pass
    
