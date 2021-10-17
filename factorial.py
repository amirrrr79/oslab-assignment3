number=int(input('Enter please number='))
fact=1

for i in range(1,number+1):
  fact*=i
  if fact==number:
     print('yes')
     break

if fact!=number:
    print('no')      
    


