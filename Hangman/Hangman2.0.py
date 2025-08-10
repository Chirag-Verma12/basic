import random
words = ["hello", "hi", "bye"]

guess = random.choice(words)
lives = 6
loss = 0
display_words = [guess[0]] + ["_"] * (len(guess) -1)
guessed_letter = []
wrong_guess = []

print("The first words is ->\t", guess[0])
print("The Length Of the Word is ->\t", len(guess))

while lives >= 0 and "_" in display_words:
    print("\nCurrent word:\t", " ".join(display_words))

