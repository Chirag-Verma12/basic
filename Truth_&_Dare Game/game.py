import random
players = []
players.append(input("Enter Player Number 1 Name ->"))
players.append(input("Enter Player Number 2 Name ->"))

add_more = input("Do you wanna add third player (yes/no)").lower()
if (add_more == "yes"):
    players.append(input("Enter Player Number 3 Name ->"))
else:
    print()
#we can add number of dares and truth we want to add but right now i only want this code to get truth or dare

while True:
    player = random.choice(players) 
    task_type = random.choice(["Truth", "Dare"]) #now this should work as per mine knowledge...

    print(f"{player}'s turn!!")
    print("you got!! ->", task_type)

    if (task_type == "Truth"):
        print("Give your opponent a question??")
    else:
        print("Give your opponent a dare to do!!")
    
    cont = input("\nType 'yes' to continue or Type 'no' to stop:").lower()
    if(cont != "yes"):
        print("Game over")
        break




