#This is a Miguel Ferreira production

import random #this is an important thing, I hope you like him, 'cause he'll be helping the computer to choose a random string so the computer can play

options = ['rock','paper','scissors'] #just a list, where the computer can check its choice


# ==== Game function ==== #

def check_winner(player, computer): #this is a kind thing called "function" and it will recieve 2 values --> the player choice and the computer choice
	#in this line below me (yes, I'm the comment) we set this variable as false, so we can return them anyways
	# 0 = lose, 1 = win, 2 = draw
	win = 0

	if(player == computer):
		win = 2


	#this following lines are just the game logic with some if's in the middle (as you can see, there's no cheating in this game) 
	if player == "rock":
		if computer == "scissors":
			win = 1
	elif player == "paper":
		if computer == "rock":
			win = 1
	else: #this can just be scissors, as we did the validation before
		if computer == "paper":
			win = 1

	#see, we return them here
	return win

def validate_players_choice(player):
	return "y" if player in options else "n"


# ====================== #

# ==== Main program ==== #

print("=== Rock, paper, scissors... ===\n")


while True:
	player = str(input("Rock, paper, scissors...? » ")).lower()
	if(validate_players_choice(player) != "y"):
		continue

	computer = random.choice(options)

	#LOSE CONDITION
	if(check_winner(player, computer) == 0):
		print("\n==== You lost :( try again!! ====\n")
	#WIN CONDITION
	elif(check_winner(player, computer) == 1):
			print("\n==== You won the computer!! ====\n")
	#DRAW CONDITION
	else:
		print("\n=== DRAW ===\n")