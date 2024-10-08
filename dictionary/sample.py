# d={'name':'anu','age':20,'place':'ekm'}
# print(d)
# print(d['name'])
# print(d['age'])
# print(d['place'])
# for i in d:
#     print(i)  
#     print(d[i])
# d['age']=25
# d['mark']=45
# print(d)

# if d['age']==20:
#     print('available')
# else:
#     print('not available')

# print(d.get('name'))
# print(d.items())
# print(d.values())
# print(d.keys())
# a=d.copy()
# d['mark']=22
# print(a)
# print(d)  
# d.pop('place')
# d.popitem()
# d.setdefault('mark')
# print(d)
# l=[11,12,13]
# print(d.fromkeys(l))
# a=input('key')
# b=input('value')
# d[a]=b
# print(d)


# dt=[{'name':'a','age':20},{'name':'b','age':50},{'name':'c','age':34},{'name':'d','age':45},{'name':'e','age':22},{'name':'f','age':37}]
# for i in dt:
#     print(i['age'])

# print('{:<10}{:<10}'.format("name","age"))
# print('_'*20)
# for i in dt:
#     if i['age']<30:
#         print('{:<10}{:<10}'.format(i['name'],i['age']))
    
# print('{:<10}{:<10}'.format("name","age"))
# print('_'*20)
# for i in dt:
#     if i['age']>30:
#         print('{:<10}{:<10}'.format(i['name'],i['age']))    
        
# a=[]
# b=[]
# for i in dt:
#     if i['age']<30:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)

# a=[i for i in dt if i['age']<30]
# b=[i for i in dt if i['age']>30]
# print(a)
# print(b)