import random
players = []
players.append(input("Enter's player name ->      \t"))
players.append(input("Enter's 2nd player name ->  \t"))

print("Here's the game begin...\n")

choose = ["Rock", "Paper", "Scissor"]

while True:
    player1, player2 = random.sample(players, 2)
    choice1 = random.choice(choose)
    choice2 = random.choice(choose)
    print(f"{player1}'s Got -> \t {choice1}")
    print(f"{player2}'s Got -> \t {choice2}")

    if(choice1 == choice2):
        print("It's a tie\n")
    elif(choice1 == "Rock" and choice2 == "Scissor") or (choice1 == "Scissor" and choice2 == "Paper") or (choice1 == "Paper" and choice2 == "Rock"):
        print(f"{player1} Win's")
    else:
        print(f"{player2} Win's")
    
    again = input("\nDo you want to play the game again? (yes/no) ->\t")
    if (again.lower() != "yes"):
        print("Thanks for playing")
        break


#In this the user can put 2 player's in it and then the game will automatically choose btw Rock, Paper and Scissor then who's so ever win or it's a draw will show in the next line..
#at the end it will ask you "Do you wanna play the game again or quit", if the player choose yes the game will begin again and if it choose's no the game will stop there and it i'll show "Thanks for playing"
