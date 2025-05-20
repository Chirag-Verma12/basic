import random
players = []
players.append(input("Enter Player Name ->\t"))
players.append(input("Enter Player Name ->\t"))
while len(players) < 5:
    add_more = input("Do you want to add more player's (yes/no)??\t")
    if(add_more == "yes"):
        players.append(input("Enter player's name ->\t"))

    else:
        print("\nHere's the game begin")
        break

truth = ["tell your name", "tell your mobile number"]
dare = ["do a dance", "give other player a coffee"]

while True:
    random_player = random.choice(players)
    print(f"\n{random_player}'s turn")
   
    ask_player = input("Do you want Truth/ Dare ->\t").lower()
    if (ask_player == "truth"):
        print(random.choice(truth))
    
    elif (ask_player == "dare"):
        print(random.choice(dare))

    else:
        print("\nPlease choose between Truth/ Dare....")
        

    cont = input("\nType 'yes' to continue or Type 'no' to stop:\t").lower()
    if(cont != "yes"):
        print("Game over!!")
        break



