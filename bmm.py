while True:
 a=int(input('adad1='))
 b=int(input('adad2='))
 if a<1 or b<1:
   break
 if a<b:
     temp=a
     a=b
     b=temp

 while b!=0:
        r=a%b
        a=b
        b=r
 print(a)        
 break


     