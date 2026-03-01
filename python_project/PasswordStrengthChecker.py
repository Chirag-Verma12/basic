from colorama import Fore, init
import string
from numpy import equal

#password strength checker
init(autoreset=True)
password = " "
password_good = False

#main logic
while password_good == False:

    #defined requirements of a good password, and when the loops starts again all the things reset
    requirements= {
        "incorrect" : 0,
        "Special_Character" : "@",
        "CountS_C" : 0,
        "uppercase" : 0,
        "lowercase" : 0,
        "spaces" : 0,
        "number" : 0
    }

    #user enter's password
    password = input(Fore.BLUE + "\nEnter password -> " + Fore.RESET)

    #check's for spaces and length of password
    if(len(password) < 5):
        print(Fore.RED + "\nPassword must be greater than 5 and no spaces are allowed")

    #checks for special character in password
    for i in range(len(password)):
        if requirements["Special_Character"] in password[i]:
            requirements["CountS_C"] +=1
        
    if requirements["CountS_C"] < 1:
        print(Fore.RED + "At least one specail character must be in password")

    #check's for spaces in password
    for s in range(len(password)):
        if password[s].isspace():
            requirements["spaces"] +=1
        
    if requirements["spaces"] >= 1:
        print(Fore.RED + "No spaces in the PASSWORD")

    #checks for uppercase in password
    if password.isupper():
        requirements["uppercase"] +=1
        print(Fore.YELLOW + "All character cant be upper case\n")

    #checks for lowercase in password
    if password.islower():
        requirements["lowercase"] +=1
        print(Fore.YELLOW + "All character cannot be lowercase\n")

    #checks for number or int value in password
    for n in range(len(password)):
        if password[n].isdigit():
            requirements["number"] +=1
        else:
            print("at least one number must be there")
            break
    
    if requirements["number"] >=1:
        print(f"your password -> {password} Is all set")
        break
            
#should i also make a number dictonay
