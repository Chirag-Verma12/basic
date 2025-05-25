import random
player = input("Enter Name->\t")

number_of_rounds = int(input("Number's Of Round You Want To Play (3/ 5/ 7)?? ->\t"))
if(number_of_rounds == 3) or (number_of_rounds == 5) or (number_of_rounds == 7):
    print("\nHere the game begin....")
else:
    print("\nInvalid!!!")
    exit()
choose = ["Rock", "Paper", "Scissor"]
print(choose)

player_win = 0
computer_win = 0
nums_of_rd = number_of_rounds

while nums_of_rd > 0:
    your_ans = input("\nChoose between (Rock, Paper& Scissor)?? ->\t")
    random_choice = random.choice(choose)
    print(f"{player}", "Choose", f"{your_ans}")
    
    computer = random.choice(choose)
    print(f"Computer Choose {computer}")
    if(your_ans == computer):
        print("\nIt's a Draw")
    
    elif(your_ans == "Rock" and computer == "Paper") or (your_ans == "Paper" and computer == "Rock") or (your_ans == "Scissor" and computer == "Paper"):
        print(f"\n{player}'s Win!!!")
        player_win += 1
    
    else:
        print("\nComputer's Win!!!")
        computer_win += 1

    
    nums_of_rd -= 1
 #print(player_win, computer_win)
if(player_win < computer_win):
    print(f"\nComputer Win human race by {computer_win} out of {number_of_rounds}")

elif(player_win == computer_win):
    print("\nnothing just wasting our time to play this shit game!!!")
    #print(f"\nHuman's Win's {player_win} out of {number_of_rounds}")

else:
    print(f"\nHuman's Win's {player_win} out of {number_of_rounds}")
    #print("\nnothing just wasting our time to play this shit game!!!")



#Each version is different from other and in this version the player can choose between Rock, Paper and scissor and the other computer will randomly 
#choose between it and the round of round's you have selected it will run till that and then it will stop and the final result will declaire on the bases of the total round..
#as whoe's number of wins are greater that player will be the final winner...
