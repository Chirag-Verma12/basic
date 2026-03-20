from colorama import Fore, init
import json
init(autoreset=True)

#Storing Data (OOPS)
class info:
    def __init__(self, name, phone_number, city) -> None:
        self.name = name
        self.phone_number = phone_number
        self.city = city


#Welcome and Menu
print("\n")
print(Fore.BLACK + "=================")
print(Fore.GREEN + "   Contact Book")
print(Fore.BLACK + "=================")
print("\b")

while True:
    #dictionary to store information in list 
    information = {
        "name" : [],
        "phone_number" : [],
        "city" : []
    }

    contact_info_saved = False
    menu_select = 0
    
    print("Menu:")
    print("1. Store\n2. Display\n3. Delete\n4. Search\n5. Exit")

    try:
        menu_select = int(input("Enter Your Choice (1/ 2/ 3/ 4/ 5)? -> "))
        if menu_select <1:
            print("Invalid Option\n")
    except ValueError:
        print("Invalid Input\n")
    
    if menu_select == 1:
        print(Fore.GREEN + "\n   Welcome to Storing Page")
        print("-------------------------------")

        #storing contact information(name, phone number & city)
        while contact_info_saved == False:
            contact_name = input(Fore.YELLOW + "Name -> " + Fore.RESET)
            #phone number invalid
            while True:
                phone_number = input(Fore.YELLOW + "Phone Number -> " + Fore.RESET)
                if len(phone_number) == 10 and phone_number.isdigit():
                    break
                else:
                    print(Fore.RED + "Invalid Input!!")

            city = input(Fore.YELLOW + "City -> " + Fore.RESET)
            
            edit_option = int(input(Fore.RED + "\nDo you want to save or change information? (1/ 2) -> " + Fore.RESET))
            if edit_option == 1:
                information["name"].append(contact_name)
                information["phone_number"].append(phone_number)
                information["city"].append(city)
                contact_info_saved = True
                print(Fore.LIGHTGREEN_EX + "Information Saved!!\n" + Fore.RESET)
                with open("data.json", "w") as file:
                    json.dump(information, file)
                break
            else:
                print(Fore.BLUE + "\nChanging Information:" + Fore.RESET)
        









