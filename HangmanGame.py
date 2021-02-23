import random
from images import IMAGES
print("hiiii")
name=input("enter a any name----")
print("good luck",name)
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
          'water', 'board', 'geeks','smile']
word=random.choice(words)  
print("guess the word") 
string=""

word1=[i for i in word]
gues=['_' for i in word]
chance=8
countofwronganswer=0
while chance>0:
    for i in gues:
        print(i,end=' ')

    print()
    a=input('your guess\t')
    if a==word:
        print(" countralations you win")
        break
    elif a in word1 and a in gues:
        print('you already guessed')
    elif a in word1:
        string=''
        l=0
        while l<len(word1):

            if word1[l]==a:
                string+=word1[l]
            elif gues[l]!='_':
                string+=gues[l]
            else:
                string+='_'
            l+=1
        gues=[i for i in string]
        if gues==word1:
            print("you win")
            chance=0
            break 
    else:
        print(IMAGES[countofwronganswer])
        chance=chance-1
        countofwronganswer+=1
        print('your guess is wrong')
        print("you have only this much chance",chance)
        
    if chance==0:
        print(' you lose')


        
IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /    |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''
	
''']

    

