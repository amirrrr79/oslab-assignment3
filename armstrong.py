import math
num=int(input('Enter number='))
if num<1:
    print('eror')
    num=int(input('Enter number='))
    
sum=0
count=0
x=[]

while num:
 p=int(num%10)
 x.append(p)
 num//=10
 count+=1
 
for i in range(len(x)):
 s=int(math.pow(x[i],count))
 sum+=s
print(sum)
if num==sum:
  print('Yes')
else:    
  print('No')    
    
 
