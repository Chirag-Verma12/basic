import random
player = input("Enter Name->\t")

number_of_rounds = int(input("Number's Of Round You Want To Play (3/ 5/ 7)?? ->\t"))
if(number_of_rounds == 3) or (number_of_rounds == 5) or (number_of_rounds == 7):
    print("\nHere the game begin....")
else:
    print("\nInvalid!!!")
    exit()
choose = ["rock", "paper", "scissor"]
print(choose)

player_win = 0
computer_win = 0
draw  = 0
nums_of_rd = number_of_rounds

while nums_of_rd > 0:
    your_ans = input("\nChoose between (rock, paper& scissor)?? ->\t").lower()
    random_choice = random.choice(choose)
    print(f"{player}", "Choose", f"{your_ans}")
    
    computer = random.choice(choose)
    print(f"Computer Choose {computer}")
    if(your_ans == computer):
        print("\nIt's a Draw")
        draw += 1
    
    elif(your_ans == "paper" and computer == "rock") or (your_ans == "rock" and computer == "scissor") or (your_ans == "scissor" and computer == "paper"):
        print(f"\n{player}'s Win!!!")
        player_win += 1
    
    else:
        print("\nComputer's Win!!!")
        computer_win += 1

    
    nums_of_rd -= 1
print(player_win, computer_win, draw, end=",")
if(player_win < computer_win):
    print(f"\nComputer Win {computer_win} out of {number_of_rounds}")

elif(player_win == computer_win):
    print("\nNO ONE WIN'S SAD..!!!")

else:
    print(f"\nHuman's Win's {player_win} out of {number_of_rounds}")

#this version is even better even pervious one... 