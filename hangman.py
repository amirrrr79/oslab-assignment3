import random
word_bank=['tree','ball','python','up','java', 'sos']
word=random.choice(word_bank)
joon=7
user_chare_true=[]

 
while True:
    win=True
    for char in word:
        if char in user_chare_true:
            print(char,end='')

        else:
           print('-', end='')
           win=False
    if win:
        print('\nExcellent you win')      
        break
    user_char=input('Enter character=')    
    if user_char in word:
     user_chare_true.append(user_char)
     print('true')
    else:
     joon-=1
     print('false')
     
    if joon==0:
     print('game over')
     break

