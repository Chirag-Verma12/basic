import random
player = input("Enter Name->\t")


choose = ["Rock", "Paper", "Scissor"]

while True:
    your_ans = input("Choose between (Rock, Paper& Scissor)?? ->\t")
    random_choice = random.choice(choose)
    print(f"\n{player}", "Choose", f"{your_ans}")
    
    computer = random.choice(choose)
    print(f"Computer Choose {computer}")
    if(your_ans == computer):
        print("\nIt's a Draw")
    
    elif(your_ans == "Rock" and computer == "Paper") or (your_ans == "Paper" and computer == "Rock") or (your_ans == "Scissor" and computer == "Paper"):
        print(f"\n{player}'s Win!!!")
    
    else:
        print("\nComputer's Win!!!")

    again = input("\nDo you want to play the game again(yes/ no)?? ->\t")
    if(again.lower() != "yes"):
        print("\nGame Over!!")
        break

#In this version the game ask you btw Rock, Paper and Scissor and the computer will randomly choose btw the option and in the end it will show weather the 
#computer win's or the player win btw them and at the end it will ask "Do you wanna play the game again or to quit" and if u type yes the game will begin again 
#and if you type no the game will end and show a message of "Game over!!"