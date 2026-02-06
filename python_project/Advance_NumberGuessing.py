import random
from colorama import Fore, init, Style
init(autoreset=True)
print(Fore.GREEN + "*************************************")
print("-------------------------------------")
print(Fore.BLUE + "   Welcome To Number Guessing Game")
print("-------------------------------------")
print(Fore.GREEN + "*************************************")

#generating the number
easy_Lives = 7
medium_Lives = 5
hard_Lives = 4
score = 0 
attempt = 0
again = " "  
win = 0
Level = 0
random_number = int(random.randint(1, 100))
print(Fore.RED + f"\nYour TOTAL LIFE: {easy_Lives}")

#Main Logic
while True:
    #choosing the Diffculty level
    print("Input The Diffculty You Want..\n1. Easy\n2. Medium\n3. Hard\n")
    while True:
        try:
            Level = int(input("Enter The Number Of Diffculty ->"))
            if(Level >= 4):
                print(Fore.RED + "\nInvalid Input!!!")
            else:
                break
        except ValueError:
            print(Fore.RED + "\nInvalid input, please keep a number")

    while(Level == 1):
        print(random_number)
        #Tells invalid input by the user, valid input must be > 1
        while True:
            try:
                guess = int(input(Fore.YELLOW + "Guess:" + Fore.RESET))
                if(guess > 1):
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print(Fore.RED + "Invalid input, please keep a number")
        if(guess == random_number):
            print(Fore.CYAN + "\nYOU WON")
            attempt +=1
            win +=1 #counts the win 
            print(Fore.GREEN + f"🎉 YOU WON in {easy_Lives} Remaining,")
            print(f"Attempts you have taken {attempt}")
            if(win > 1): #win more than one, it count it as a streak and print the streak
                print(f"\nYour Streak is going crazy!!! {win}, Keep Going Champ\n")

        elif(guess > random_number):
            attempt +=1
            easy_Lives -=1
            if(random_number < 30 and guess >50): #make all this in a single row like random number or and this and that
                print("Huge Difference")
                score +=4
            else:
                print(Fore.MAGENTA + "HIGHER Than the Actual Number")
                score +=6
            print(f"\nLIFE LEFT: {easy_Lives}")

        elif(guess < random_number):
            easy_Lives -=1
            attempt +=1
            if(random_number > 50 and guess < 30):
                print("Huge diiiiiiffff")
            else:
                print(Fore.BLUE + "LOWER Than The Actual Number")
            print(f"\nLIFE LEFT: {easy_Lives}")

        if(easy_Lives == 0):
            print("\nYou LOSS >_<")
            print(f"The Actual Number Was {random_number}")
            if(win > 1):
                print(f"Your wining streak {win}, DO IT AGAIN...")
            break

    while Level == 3:
        print(random_number)
        while True:
            try:
                guess = int(input(Fore.YELLOW + "Guess:" + Fore.RESET))
                if(guess > 1):
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print(Fore.RED + "Invalid input, please keep a number")

        if(guess == random_number):
            print(Fore.CYAN + "\nYOU WON")
            attempt +=1
            win +=1 #counts the win 
            print(Fore.GREEN + f"🎉 YOU WON in {hard_Lives} Remaining,")
            print(f"Attempts you have taken {attempt}")
            if(win > 1): #win more than one, it count it as a streak and print the streak
                print(f"\nYour Streak is going crazy!!! {win}, Keep Going Champ\n")