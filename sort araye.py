araye=(input()).split()
bool=True

for i in range(len(araye)):
        for j in range(i+1,len(araye)):
            if araye[i]>araye[j]:
                bool=False
                break
if bool==True:
    print('yes=araye is sort')   
else:
    print('No=araye not sort')             


