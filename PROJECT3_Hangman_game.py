#HANGMAN GAME

import random
import PROJECT3_HStages
import PROJECT3_WordFile

word_list=['apple','bird','yellow','beautiful','flowers']
lives=6
choosen_word=random.choice(PROJECT3_WordFile.words)
#print(choosen_word)

display=[]
for letter in range(len(choosen_word)):        #print dashes equal to the letters present in the chosen word
    display+='_'
print(display)

game_over=False

while not game_over:
    guessed_letter=input('Guess a letter : ').lower()
    for pos in range(len(choosen_word)):
        letter=choosen_word[pos]
        if letter==guessed_letter:
            display[pos]=guessed_letter
    print(display)

    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print('YOU LOSE!!')

    if '_' not in display:
        game_over=True 
        print('YOU WIN!!')

    print(PROJECT3_HStages.STAGES[lives])

