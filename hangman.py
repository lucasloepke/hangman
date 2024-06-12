import sys
import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

def loseg():
    print("Unfortunately, you have lost... The word was "+word)
    #sys.exit()

def wing():
    print("\nYou have won, congratulations!")
    #sys.exit()

def getchar():
    global attempt 
    attempt = input("Guess a character: ")
    if len(attempt) != 1:
        getchar()

# game logic
def game():
    print("Welcome to Hangman. Please start guessing")

    length = len(word)
    win = False
    strikes = 0
    guessed_letters = set()

    while win != True:
        remaining_letters = 0
        for i in range(length):
            if word[i] in guessed_letters:
                print(word[i]+" ", end="")
            else:
                print("_ ", end="")
                remaining_letters += 1

        if remaining_letters == 0:
            win = True
            wing()
            break
        print("")
        getchar()

        if attempt in word or attempt.upper() in word:
            print("")
        elif attempt in guessed_letters:
            print("")
        else:
            strikes += 1
            print("You have guessed incorrectly "+str(strikes)+" out of 8 times\n")
        
        guessed_letters.add(attempt)
        guessed_letters.add(attempt.upper())

        if strikes > 7:
            loseg()
            break
#---------------------------------------------------------------------------
# Pandas
df = pd.read_csv(r'hmwords.csv')
random_row = df.sample()
word = random_row.iloc[0,0]
#---------------------------------------------------------------------------

# game looper
play = True
while play is True:
    game()
    cont = input("Continue playing? [y/n] ").strip().lower()
    if cont.startswith('y'):
        play = True
        random_row = df.sample()
        word = random_row.iloc[0,0]
    else:
        play = False
        print("Goodbye!")
        sys.exit(0)