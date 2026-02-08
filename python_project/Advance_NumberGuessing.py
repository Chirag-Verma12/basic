import random
from colorama import Fore, init, Style
from sympy import Le
init(autoreset=True)
print(Fore.GREEN + "*************************************")
print("-------------------------------------")
print(Fore.BLUE + "   Welcome To Number Guessing Game")
print("-------------------------------------")
print(Fore.GREEN + "*************************************")

#defining variables 
easy_Lives = 7
medium_Lives = 5
hard_Lives = 4
score = 0
attempt = 0
again = " "  
guess = 2
win = 0
Level = 0
random_number = int(random.randint(1, 100)) #generating the number

#Main Logic
while True:
    #choosing the Diffculty level
    print("Input The Diffculty You Want..\n1. Easy\n2. Medium\n3. Hard\n4. Exit\n")
    while True:
        try:
            Level = int(input("Enter The Number Of Diffculty ->"))
            if(Level >= 5):
                print(Fore.RED + "\nInvalid Input!!!")
            else:
                break
        except ValueError:
            print(Fore.RED + "\nInvalid input, please keep a number")

    if(Level == 4):
        print("thank you for playing")
        break

    while(Level == 1):
        # print(random_number) Answer revealing
        #Tells invalid input by the user, valid input must be > 1
        print(Fore.RED + f"\nLives: {easy_Lives}" + Fore.RESET)
        while True:
            try:
                guess = int(input(Fore.YELLOW + "\nGuess:" + Fore.RESET))
                if(guess > 1):
                    break
                else:
                    print(Fore.RED + "\nInvalid Input")
            except ValueError:
                print(Fore.RED + "Invalid input, please keep a number")
        if(guess == random_number):
            print(Fore.CYAN + "\nYOU WON")
            win +=1 #counts the win 
            score +=15
            print(Fore.GREEN + f"🎉 YOU WON in {easy_Lives} Remaining,")
            print(f"SCORE: {score}")
            print(f"Attempts you have taken {attempt}\n")
            if(win > 1): #win more than one, it count it as a streak and print the streak
                score +=9
                print(f"\nYour Streak is going crazy!!! {win}, Keep Going Champ\n")
            break

        elif(guess > random_number):
            attempt +=1
            easy_Lives -=1
            if(random_number < 30 and guess >50): #make all this in a single row like random number or and this and that
                print("Huge Difference")
                score +=4 #record the scores
            else:
                print(Fore.MAGENTA + "HIGHER Than the Actual Number")
                score +=6 #if, user is closer... it will add +6

        elif(guess < random_number):
            easy_Lives -=1
            attempt +=1
            if(random_number > 20 and guess > 60):
                print("Huge diiiiiiffff")
                score +=4
            else:
                print(Fore.BLUE + "LOWER Than The Actual Number")
                score +=6

        if(easy_Lives == 0):
            print("\nYou LOSS >_<")
            print(f"The Actual Number Was {random_number}")
            print(f"Your score {score}")
            if(win > 1):
                print(f"Your wining streak {win}, DO IT AGAIN...")
        

    #Medium Level
    random_number = int(random.randint(1, 100)) 
    while(Level == 2):
        continue


    #Hard Level
    random_number = int(random.randint(1, 110)) 
    while Level == 3:
        print(Fore.RED + f"\nLIVES: {hard_Lives}")
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
            score +=20
            win +=1 #counts the win 
            print(Fore.GREEN + f"🎉 YOU WON in {hard_Lives} Remaining,")
            print(f"Attempts you have taken {attempt}")
            print(f"Score: {score}")
            if(win > 1): #win more than one, it count it as a streak and print the streak
                print(f"\nYour Streak is going crazy!!! {win}, Keep Going Champ\n")
                score += 15

        elif(random_number >= 1 and random_number <= 30):
            hard_Lives -=1
            attempt +=1
            score +=7
            print("THE number lies btw 1 to 30")
        elif(random_number > 30 and random_number <= 80):
            hard_Lives -=1
            attempt +=1
            score +=7
            print("IT lies btw 40 to 80")
        elif(random_number > 80 and random_number <= 110):
            hard_Lives -=1
            attempt +=1
            score +=7
            print("Lies btw 80 to 110")
        
        if(hard_Lives == 1):
            hint = input("\nDo you want a hint?? (y/ n)").lower()
            if(hint == "y" or hint == "yes"):
                score -=5 #Hint make the Hard Level a sort of easy, so we minus 5 point from the score
                if(random_number % 2 == 0):
                    print("The Number is PRIME")
                else:
                    print("The Number is NOT PRIME")
        
        if(hard_Lives == 0):
            print("\nYou LOSS > _ <")
            print(f"Score : {score}")
            print(f"Actual Number was {random_number}")
            if(win > 1):
                print(f"Your wining streak is {win}, DO IT AGAIN...")
