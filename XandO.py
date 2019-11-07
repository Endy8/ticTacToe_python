 #Python x and 0

import random

board = [[" ", " ", " "], 
    	 [" ", " ", " "],
    	 [" ", " ", " "]]



def printBoard():
	print("\n")
	for i in range(0,3):
		for j in range(0,3):
			if j==2:
				print(" "+str(board[i][j]),end="")
			else:
				print(" "+str(board[i][j])+" |",end="")
		if i!=2:
			print("\n---+---+---")
	print("\n")

def playerMove():

	playerRowPosition = int(input("Row position: "))
	playerColumnPosition = int(input("Column position: "))

	while playerRowPosition-1 < 0 or playerRowPosition-1 > 2 or playerColumnPosition-1 < 0 or playerColumnPosition-1 > 2 or board[playerRowPosition-1][playerColumnPosition-1] != " ":
		print("Invald positions! Try again!")
		playerRowPosition = int(input("Row position: "))
		playerColumnPosition = int(input("Column position: "))

	board[playerRowPosition-1][playerColumnPosition-1] = "X"

def aiMove():
	aiRowMove = random.randint(0,2)
	aiColumnMove = random.randint(0,2)
	while aiRowMove < 0 or aiRowMove > 2 or aiColumnMove < 0 or aiColumnMove > 2 or board[aiRowMove][aiColumnMove] != " ":
		aiRowMove = random.randint(0,2)
		aiColumnMove = random.randint(0,2)
	board[aiRowMove][aiColumnMove] = "O"



def checkWin():
	horizontal = ""
	vertical = ""
	diagonal1 = ""
	diagonal2 = ""

	for i in range(0,3):
		for j in range(0,3):
			horizontal += str(board[i][j])
			if str(horizontal) == "XXX":
				return "X WINS!"
			elif str(horizontal) == "OOO":
				return "O WINS!"
		horizontal = ""

	for j in range(0,3):
		for i in range(0,3):
			vertical += str(board[i][j])
			if str(vertical) == "XXX":
				return "X WINS!"
			elif str(vertical) == "OOO":
				return "O WINS!"
		vertical = ""

	for i in range(0,3):
		for j in range(0,3):
			if i==j:
				diagonal1+=str(board[i][j]);
			if i+j==2:
				diagonal2+=str(board[i][j]);

	if str(diagonal1) == "XXX" or str(diagonal2) == "XXX":
		return "X WINS!"
	elif str(diagonal1) == "OOO" or str(diagonal2) == "OOO":
		return "O WINS!"

	return 0



for i in range(0,5):
	printBoard()
	playerMove()
	if i!=4:
		aiMove()
	else:
		if(checkWin()==0):
			print("DRAW!")
			break
	if checkWin() != 0:
		print("\n"+checkWin())
		break

printBoard()


