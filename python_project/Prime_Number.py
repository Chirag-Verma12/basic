import math
from colorama import Fore, init

init(autoreset=True)
# intro
print("Welcome\n")
is_prime = True
again = ' '
generate_prime = True
go = input(Fore.BLUE + "Ready!!!\n(Type 'go' to start) ->\t").lower()

# Repeat whole logic again
while again == "y" or go == "go":
    choose = input(Fore.WHITE + "\nWant do you wanna do generate or check?? (g/ c) ->\t").lower()

    # Takes user input and check if number is valid or not. Specifically check for number > 1 to continue
    while choose == "c" or choose == "C" or choose == "Check" or choose == "check" or choose == "CHECK":
        while True:
            try:
                number = int(input("Enter Number:\t"))
                if(number > 1):
                    break
                else:
                    print(Fore.YELLOW + "Not Prime")
            except ValueError:
                print(Fore.RED + "Invalid Input!!!\n")


        # Main logic to check if number is prime or not
        if(choose == "c" or choose == "C" or again == "y" or again == "Y"):
            is_prime = True
            for i in range(2, int(math.sqrt(number)) +1):
                if(number % i == 0):
                    is_prime = False

        # Print result
        if(is_prime == True):
            print(Fore.GREEN + "Prime")
            break
        else:
            print(Fore.YELLOW + "Not prime")
            break
    
    # Loop to generate prime numbers till N
    while choose in ("g", "generate"):
        while True:
            try:
                number = int(input("Enter Number:"))
                if(number > 1):
                    break
                else:
                    print(Fore.YELLOW + "Not Prime")
            except ValueError:
                print(Fore.RED + "\nInvalid Input!!!\n")
        
        if choose == "g" or choose == "G" or again == "y" or again == "Y":
            # Generates number from 2 to number
            for i in range(2, number):
            # print("Checking primeness for", i)
                generate_prime = True
                # Check if number i is prime or not by checking divisibility by every number from 1 till sqrt(i)
                d = 2
                while d <= math.sqrt(i):
                    if i % d == 0:
                        generate_prime = False
                        break
                    d += 1
                # Print the number if prime
                if generate_prime:
                    print(i)
        break
    again = input(Fore.WHITE + "\nDo you want to play again (y/ n) ->\t").lower()
    if(again == 'n' or again == 'no'):
        print(Fore.CYAN + "\nThanks for playing\n")
        break
