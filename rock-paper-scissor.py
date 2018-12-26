print("Rock Paper and Scissors")

p1_name = input("Enter player 1 name: ")
p2_name = input("Enter player 2 name: ")
p1_play = ""
p2_play = "" 
play_message = " enter your play. rock, paper, scissors(r/p/s): " 
play_again = ""
plays =  {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}
weakness_rules =  {
    "rock": ("paper"),
    "paper": ("scissors"),
    "scissors": ("rock")
}

# game loop
while True:
    while not p1_play in plays:
        p1_play = input(p1_name + play_message)

    while not p2_play in plays:
        p2_play = input(p2_name + play_message)
    
    
    if p1_play == p2_play:
        print("its a tie")
    else:
        if plays[p1_play] in weakness_rules[plays[p2_play]]:
            print("winner is: " + p1_name)
        else:
            print("winner is: " + p2_name)
    
    while play_again != "yes" and play_again != "no":
        play_again = input("play again (yes/no): ")
    
    if play_again == "no":
        break
    else: 
        p1_play = p2_play = play_again = ""

print("game over") 
        