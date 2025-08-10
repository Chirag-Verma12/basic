import random
words = ["name", "list", "fist", "pop"]

guess  = random.choice(words)
lives = 6
loss = 0
guessed_letter = []
wrong_guess = []
display_word = [guess[0]] + ["_"] * (len(guess) -1)
guessed_letter.append(guess[0])

print("The first word is:\t", guess[0])
print("The word length is:\t", len(guess))

while lives >0 and "_" in display_word:
    print("\ncurrent word:\t", " ".join(display_word))
    letter = input("Guess a letter:\t").lower()

    if letter in guessed_letter or letter in wrong_guess:
        print("you have already guessed it!!")
        
    if letter in guess:
        print("You got it..") 
        guessed_letter.append(letter)

        for idx in range(len(guess)):
            if guess[idx] == letter:
                display_word[idx] = letter
       
    else:
        print("You have guessed it wrong...")
        lives -=1
        wrong_guess.append(letter)
        print(f"Lives left {lives}")
        

if "_" not in display_word:
    print("You won the game:\t", guess)

else:
    print("\ngame over the word was:\t", guess)