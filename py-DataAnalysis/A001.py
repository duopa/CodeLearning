import time

def swap(a,b):
    b,a=a,b


a,b=3,4
swap(a,b)
print(a,b)

a=0
async def add(a):
    a+=1
    return print(a)


for i in range(10):
    add(a)