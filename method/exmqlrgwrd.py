f=open('demo.txt','r')
l=f.readlines()
f.seek(0)
long=''
for i in range(len(l)):
    b=f.readline().strip()
    c=b.split(' ')
    for j in c:
        if j!='' and len(j)>len(long):
            long=j

print(long)