import random
print("*************************************")
print("-------------------------------------")
print("   Welcome To Number Guessing Game")
print("-------------------------------------")
print("*************************************")

#generating the number
lives = 7
attempt = 0
again = " "  
random_number = int(random.randint(1, 100))
print(f"\nYour TOTAL LIFE: {lives}")

#Main Logic
while True:
    #Tells invalid input by the user, valid input must be > 1
    while True or again == "yes":
        try:
            guess = int(input("Guess:"))
            if(guess > 1):
                break
            else:
                print("Invalid Input")

        except ValueError:
            print("Invalid input, please keep a number")

    if(guess == random_number):
        print("\nYOU WON")
        attempt +=1
        print(f"🎉 YOU WON in {lives} Remaining")
        print(f"Attempts you have taken {attempt}")


    elif(guess > random_number):
        lives -=1
        attempt +=1
        print("HIGHER Than the Actual Number")
        print(f"\nLIFE LEFT: {lives}")

    elif(guess < random_number):
        lives -=1
        attempt +=1
        print("LOWER Than The Actual Number")
        print(f"\nLIFE LEFT: {lives}")
    
    if(lives == 0):
            print("\nYou LOSS >_<")
            print(f"The Actual Number Was {random_number}")
    
    #Restart, and reset Lives, attempts and generate a new number
    while lives < 1 or guess == random_number:
        random_number = int(random.randint(1, 100))
        lives = 7
        attempt = 0
        again = input("\nDo You wanna play again?? (y/ n):")

    #Quiting function
    if(again == "N" or again == "n" or again == "no" or again == "NO"):
        print("<><><><><><><><><><><><><><><><><><>")
        print("\n        Thank for playing\n")
        print("<><><><><><><><><><><><><><><><><><>")
        break
        
    

        
    