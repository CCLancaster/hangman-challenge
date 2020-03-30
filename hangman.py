# Initialize the game: Initialize all variables to default values.
# Display hangman or number of guesses remaining.
# Randomly select a secret word.
# Display the word as blanks.
# Display the letters guessed so far.
# Ask the user for a letter.
# Determine if letter is correct or incorrect.
# If incorrect, add the letter to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
# If correct, add the letter to the guessed list, redraw the secret word with the new letter(s) showing.
# Loop back up to step 6 and continue until the word is fully revealed or guesses are used up.

import random

# print these lines for each wrong guess
drawings = [
' ____\n|    |\n|    \n|   \n|    \n|-\n',
' ____\n|    |\n|    O\n|   \n|    \n|-\n',
' ____\n|    |\n|    O\n|   |\n|    \n|-\n',
' ____\n|    |\n|    O\n|   -|\n|    \n|-\n',
' ____\n|    |\n|    O\n|   -|-\n|    \n|-\n',
' ____\n|    |\n|    O\n|   -|-\n|    /\n|-\n',
' ____\n|    |\n|    O\n|   -|-\n|    /\\\n|-\n'
]

# word = input()
# word = "secret"
secret_words = [
    "rose",
    "blue",
    "poem",
    "video",
    "game",
    "phone",
    "shiny",
    "firefly"
]

global hang
global word
global guesses
global display
global turns

word= ""
guesses = ""
display = ""
hang = 0

#select word from list 
word = random.choice(secret_words)

#split the word into its individual characters
def split(word):
    return list(word)

#display the word
display = split(word)
print(display)

# for i in range (len(display)):
#     display[i] = "_"
#     print(' '.join(display))

length = len(word)
turns = length

while turns > 0:
    failed = 0
    print("Your word has ", length, "letters")
    
    guess = input("Guess a letter: ")
    guesses += guess
   
    for char in word: 
        if char in guesses:
            place = word.index(char)
            print(display[place])
        else:
            failed += 1
    if failed == 0:
        print("You won")
        break

    print('Your guesses: ', guesses)
    
    if guess not in word:
        turns -= 1
        hang += 1
        print(drawings[hang])
        print("Try again")
        print("You have ", + turns, " guesses left")
        if turns == 0:
            print("Bummer, you lose")
    



    
