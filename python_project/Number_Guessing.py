import random
print("*************************************")
print("   Welcome To Number Guessing Game")
print("*************************************")

#generating the number
lives = 7
attempt = 0
again = []  
random_number = int(random.randint(1, 100))
print(random_number) #hide after done
print(f"\nYour TOTAL LIFE: {lives}\n")

while True:
    while True:
        try:
            guess = int(input("Guess:\t"))
            if(guess > 1):
                break
            else:
                print("Invalid Input")

        except ValueError:
            print("Invalid input, please keep a number")
    if(lives <= 1):
        print("LOSS")
        print(f"the actual number was {random_number}")
        break

    elif(guess == random_number):
        print("YOU WON")
        attempt +=1
        print(f"YOU WON AT {lives} remaining")
        print(f"Attempts you have taken {attempt}")

    elif(guess > random_number):
        lives -=1
        attempt +=1
        print("HIGHER Than the Actual Number")
        print(f"LIFE LEFT: {lives}")

    elif(guess < random_number):
        lives -=1
        attempt +=1
        print("LOWER Than The Actual Number")
        print(f"LIFE LEFT: {lives}")
    

        
    