import random

array=[]
n=int(input('enter size='))
for i in range(n):
    s=random.randint(0,100)
    if s not in array:
        array.append(s)
print(array)        

