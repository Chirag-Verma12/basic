from colorama import Fore, init
from numpy import equal

#password strength checker
init(autoreset=True)
password = " "
password_good = False

#scoring the password
score = 0

#main logic
while password_good == False:

    #defined requirements of a good password, and when the loops starts again all the things reset
    requirements= {
        "Special_Character" : "@",
        "CountS_C" : 0,
        "uppercase" : 0,
        "spaces" : 0,
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
            score += 2
        
    if requirements["CountS_C"] < 1:
        print(Fore.RED + "At least one specail character must be in password")

    #check's for spaces in password
    for s in range(len(password)):
        if password[s].isspace():
            requirements["spaces"] +=1
    if requirements["spaces"] >= 1:
        print(Fore.RED + "No spaces in the PASSWORD")

    #checks for uppercase in password
    for u in range(len(password)):
        if password[u].isupper():
            requirements["uppercase"] +=1
    if requirements["uppercase"] < 1:
        print("There must be a uppercase in password")

    #checks for number or int value in password
    count_digit = 0
    for n in range(len(password)):
        if password[n].isdigit():
            # print("Digit Found: ", password[n])
            count_digit +=1
            score += 2
        # print("Number Count = ", count_digit)
    
    if (requirements["CountS_C"] and requirements["uppercase"]) >=1 and count_digit >=1:
        print("\nNow the password is ready for use\n")
        password_good = True

#score the password 
print(f"Password = {password}")
print(f"Score = {score}")
