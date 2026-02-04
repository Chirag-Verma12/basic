import random
from colorama import Fore, init
init(autoreset=True)
print(Fore.GREEN + "*************************************")
print("-------------------------------------")
print(Fore.BLUE + "   Welcome To Number Guessing Game")
print("-------------------------------------")
print(Fore.GREEN + "*************************************")

#generating the number
lives = 7
attempt = 0
again = " "  
win = 0
loss = 0
random_number = int(random.randint(1, 100))
print(Fore.RED + f"\nYour TOTAL LIFE: {lives}")

#Main Logic
while True:
    print(random_number)
    #Tells invalid input by the user, valid input must be > 1
    while True or again == "yes":
        try:
            guess = int(input(Fore.YELLOW + "Guess:"))
            if(guess > 1):
                break
            else:
                print("Invalid Input")

        except ValueError:
            print(Fore.RED + "Invalid input, please keep a number")

    if(guess == random_number):
        print(Fore.CYAN + "\nYOU WON")
        attempt +=1
        win +=1
        print(Fore.GREEN + f"🎉 YOU WON in {lives} Remaining,")
        print(f"Attempts you have taken {attempt}")
        if(win > 1): #win more than one, it count it as a streak and print the streak
            print(f"\nYour Streak is going crazy!!! {win}, Keep Going Champ\n")



    elif(guess > random_number):
        lives -=1
        attempt +=1
        print(Fore.MAGENTA + "HIGHER Than the Actual Number")
        print(f"\nLIFE LEFT: {lives}")

    elif(guess < random_number):
        lives -=1
        attempt +=1
        print(Fore.BLUE + "LOWER Than The Actual Number")
        print(f"\nLIFE LEFT: {lives}")
    
    if(lives == 0):
            print("\nYou LOSS >_<")
            print(f"The Actual Number Was {random_number}")
            if(win > 1):
                print(f"Your wining streak {win}, DO IT AGAIN...")
    
    #Restart, and reset Lives, attempts and generate a new number
    while lives < 1 or guess == random_number:
        random_number = int(random.randint(1, 100))
        lives = 7
        attempt = 0
        again = input("\nDo You wanna play again?? (y/ n):")
        print("\n")

    #Quiting function
    if(again == "N" or again == "n" or again == "no" or again == "NO"):
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><>")
        print(Fore.GREEN + "        Thank for playing")
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><>")
        break
        

        
    