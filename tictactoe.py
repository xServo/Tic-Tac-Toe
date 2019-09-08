#Tic-Tac-Toe
import os

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
turns = 1

def board():
	os.system("clear")
	print("   |   |   ")
	print(" " + row1[0] + " | " + row1[1] + " | " + row1[2] + " ")
	print("___|___|___")
	print("   |   |   ")
	print(" " + row2[0] + " | " + row2[1] + " | " + row2[2] + " ")
	print("___|___|___")
	print("   |   |   ")
	print(" " + row3[0] + " | " + row3[1] + " | " + row3[2] + " ")
	print("   |   |   ")

	

print("Welcome to Tic-Tac-Toe.\nWhen the game is finished type \"done\"")

#board
while True:

	#player 1
	board()
	row = input("\nPlayer 2:\nPick your row. ")
	if row == "done":
		row1 = [" ", " ", " "]
		row2 = [" ", " ", " "]
		row3 = [" ", " ", " "]
		input("Game over.\nPress enter to play again.")
	column = input("Pick your column. ")

	if row == "1":
		row1[int(column) - 1] = "x"
	elif row == "2":
		row2[int(column) - 1] = "x"
	elif row == "3":
		row3[int(column) - 1] = "x"
	
	#player 2	
	board()
	row = input("\nPlayer 2:\nPick your row. ")
	if row == "done":
		row1 = [" ", " ", " "]
		row2 = [" ", " ", " "]
		row3 = [" ", " ", " "]
		input("Game over.\nPress enter to play again.")
		os.system("clear")
	column = input("Pick your column. ")

	if row == "1":
		row1[int(column) - 1] = "o"
	elif row == "2":
		row2[int(column) - 1] = "o"
	elif row == "3":
		row3[int(column) - 1] = "o"
		input("Game over.\nPress enter to play again.")

	