a=input('Enter jomle=')
count=0
space=0
f=0
for char in a:
    if space==False:
        count+=1
        space=True
        f=True
    else:
        space=False
if f==True:
    print(count)
        




    

