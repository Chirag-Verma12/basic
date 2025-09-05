#change the answer idx to the letter idx
from curses.ascii import isalpha
import random

from sympy import true
while true:
    Name = str(input("Enter Your Name ->\t"))
    if Name.isalpha():
        print("\n************* The Game Begin *************")
        print(f"\nWelcome!, {Name} In The Game Of Hangman")
        break
    else:
        print("\nPlease enter a geniun name")

words = ["hello", "ghosting", "number", "her", "nothing"]
answer = random.choice(words)
lives = 6
loss = 0
guessed_words = []
wrong_guess = []
display_word = [answer[0]] + ["_"] * (len(answer) -1)
guessed_words.append(answer[0])

print("\nThe First Word is:\t", answer[0])
print("Length Of The Word is:\t", len(answer))
print("\nLives:\t", lives)

Word_letter = int(input("\nWeather You want to guess a Letter or a Word (1/ 2)?? ->\t"))

#Script of Letter 1:
if Word_letter == 1:
    while lives > 0:
        print("\nCurrent Word:\t", " ".join(display_word))
        while true:
            letter = input("\nGuess a letter:\t").strip().lower()
            if letter.isalpha() and len(letter) == 1:
                print("Thanks...")
                if letter in guessed_words or letter in wrong_guess:
                    print("Guess one at a time")
            else:
                print("\nPlease guess 1 letter at a time...") 
        
            if letter in answer and len(letter) == 1:
                print("\nYou Got It!!!")
                guessed_words.append(letter)

                for idx in range(len(answer)):
                    if answer[idx] == letter:
                        print("\n",display_word)
                        display_word[idx] = letter 
                        print("\n",display_word)
            else:
                print("\nYou guessed it Wrong....")
                lives -= 1
                print(f"Lives Left:\t {lives}" )
                wrong_guess.append(letter)
            