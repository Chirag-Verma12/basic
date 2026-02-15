from colorama import Fore, init
import string
init(autoreset=True)
#password strength checker

#User Enter Password
while True:
    password = input("Enter Password -> ")
    if(len(password) < 5):
        print("Password must be greater than 5")
    
    if(password.isupper()):
        print("Full name cant be Upper case")
    
    if(password.islower()):
        print("Full name cant be Lower case")
    else:
        break

print(password) 
            

'''

Objective: 
1. Limit the length of Password 
2. There must be an Uppercase, Special Character and An Int present in the password
3. There must be a Score checker in the last, to check where it is strong or weak

'''