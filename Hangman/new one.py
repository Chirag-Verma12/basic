import random
Name = str(input("Enter Your Name ->\t"))

print("\n************* The Game Begin *************")
print(f"\nWelcome!, {Name} In The Game Of Hangman")

words = ["hello", "ghosting", "number", "her", "nothing"]
guess = random.choice(words)
lives = 6
loss = 0
guessed_words = []
wrong_guess = []
display_word = [guess[0]] + ["_"] * (len(guess) -1)
guessed_words.append(guess[0])

print("\nThe First Word is:\t", guess[0])
print("Length Of The Word is:\t", len(guess))
print("\nLives:\t", lives)

Word_letter = int(input("\nWeather You want to guess a Letter or a Word (1/ 2)?? ->\t"))

#Script of Letter 1:
if Word_letter == 1:
    while lives > 0:
        print("\nCurrent Word:\t", " ".join(display_word))
        letter = input("Guess a letter:\t").lower()

        if letter in guessed_words or letter in wrong_guess:
            print("You got it!!!") 

        
        if letter in guess:
            print("You Got It!!!")
            guessed_words.append(letter)

            for idx in range(len(guess)):
                if guess[idx] == letter:
                    display_word[idx] = letter 
        else:
            print("\nYou guessed it Wrong....")
            lives -= 1
            print(f"Lives Left:\t {lives}" )
            wrong_guess.append(letter)