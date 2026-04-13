from colorama import Fore, init
init(autoreset=True)
import json
import os

#import file name as FILE
FILE = "data.json"

#loading file
def loading_file():
    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        return[]
    with open(FILE, "r") as file:
        return json.load(file)
    
#saving contact
def save_contact(contacts):
    with open(FILE, "w") as file:
        json.dump(contacts, file, indent=4)

#adding contact 
def add_contact():
    correct_contact_number = False
    name = input("Enter name -> ")
    while correct_contact_number == False:
        phone_number = input("Phone number -> ")
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Incorrect Contact Number\n")
        else:
            correct_contact_number = True
            break
        
    city = input("Enter city -> ")

    contact = {
        "name" : name,
        "phone_number" : phone_number,
        "city" : city
    }

    contacts = loading_file()
    contacts.append(contact)
    save_contact(contacts)
    print(f"{name} saved sucessfully!!\n")

#display contacts
def display_contact():
    contacts = loading_file()
    if not contacts:
        print("Nothing has been saved yet!\n")
        return
    for i, c in enumerate(contacts, 1):
        print(f"\n{i}. {c['name']} | {c['phone_number']} | {c['city']}\n")

#searching
def search_contact():
    search = input("Enter name to search -> ")
    contacts = loading_file()

    if not contacts:
        print("Nothing has been saved yet!!\n")
        return
    
    result = [c for c in contacts if search in c["name"].lower()]
    if result:
        for c in result:
            print(f"\nName: {c['name']}")
            print(f"\nPhone number: {c['phone_number']}")
            print(f"\nCity: {c['city']}")
    else:
        print("Contact not found!\n")

#delete contact
def delete_contact():
    name = input("Enter name to delete contact -> ")
    contacts = loading_file()
    new_contact = [c for c in contacts if c["name"].lower() != name]

    if len(new_contact) == len(contacts):
        print("contact not found!\n")
    else:
        save_contact(new_contact)
        print(f"Contact deleted\n")


while True:
    print("Menu:")
    print("1. Store\n2. Display\n3. Delete\n4. Search\n5. Exit")
    choose = int(input("Choose -> "))
    if choose == 1:
        add_contact()
    elif choose == 2:
        display_contact()
    elif choose == 3:
        delete_contact()
    elif choose == 4:
        search_contact()
    elif choose == 5:
        print("Thank you")
        break
    else:
        print("invalid input")
        
