##################
#    c1 c2 c3
#r1   -  -  -
#r2   -  -  -
#r3   -  -  -
##################

import numpy as np
import re

def rules():
	print "For each move enter a position, e.g. r0-c1:"
	print 
	print "     c0  c1  c2"
	print "   +-----------+ "
	print "r0 | -   -   - |"
	print "r1 | -   -   - |"
	print "r2 | -   -   - |"
	print "   +-----------+ "	
	print 
	print "---------------------------------------------"	

def setup_game():
	rules()
	print "Enter size of board: " ,
	board_size = raw_input()
	print "Enter the dificulty level (super-easy or hard): ",
	dificulty = raw_input()
	Board = make_board(int(board_size))
	print_board(Board)
	return (Board,dificulty)
	#play_game(Board,dificulty)	
	

def print_board(board):
	print 
	print ("    "),
	for i in range(len(board)):
		print "c%i "%i,
	print 
	print "   +" + ("----"*len(board))+ "+"

	for i, sublist in enumerate(board): 
		print "r%i |"%i,
		for item in sublist:
			if item == "O":
				print " O " ,
			elif item == "X":
				print " X ",
			else:
				print " - " , 
		print "|"
	print "   +" + ("----"*len(board))+ "+"
	print


def is_spot_available(board, move):
	for sublist in board:
		for item in sublist:
			if (item == move):
				return  True
	return False


def super_easy(board):
	for i, sublist in enumerate(board):
		for j,item in enumerate(sublist):
			if (item != 'O' and item != 'X'):
				board[i][j] = 'X'
				return board
	return board


def hard(board):
	#defensive 
	#check opponent for 2 in row, col, diagonal
	for i, sublist in enumerate(board):
		print sublist
		if sublist.count('O') == len(board) - 1:
			for j,item in enumerate(sublist):
				if item != 'O' and item != 'X':
					board[i][j] = 'X'
					return board
		
	return super_easy(board)



def update_board(board,difficulty,move=None):
	if (move):
		for i, sublist in enumerate(board):
			for j,item in enumerate(sublist):
				if (item == move):
					board[i][j] = 'O'
		return board
	else: #computer's turn
		if difficulty == "super-easy":
			return super_easy(board)
		else:
			return hard(board)





def is_won(board, is_computer):

	if is_computer:
		player = 'X'
	else:
		player = 'O'

	"""
	#rows match
	for sublist in board:  
		win = all(item == player for item in sublist)
		if (win):
			return True
	"""

	"""
	#cols match 
	for i in range(len(board)): 
		colWin = all(sublist[i] == player for sublist in board) 
		if (colWin):
			return True
	"""
	
	"""
	#diagnol uppperLeft-bottonRight
	win = True
	for i, sublist in enumerate(board):
		if sublist[i] != player:
			win = False
	if (win):
		return True


	#diagnol uppperRight-bottonLeft
	win = True
	for i, sublist in enumerate(board):
		if sublist[len(board)-1-i] != player:
			win = False
	if (win):
		return True
	"""

	diag1Win = True
	diag2Win = True
	for i, sublist in enumerate(board):
		colWin = all(sublist[i] == player for sublist in board) 
		if (colWin):
			return True
		rowWin = all(item == player for item in sublist) #rows match
		if rowWin:
			return True
		if sublist[i] != player:
			diag1Win = False
		if sublist[len(board)-1-i] != player:
			diag2Win = False

	if (diag1Win or diag2Win):
		return True

	return False #not a winner


def play_game(board, difficulty):
	num_moves_left = pow(len(board), 2)
	while (True):
		if num_moves_left == 0:
			print "IT'S A DRAW!"
			print_board(board)
			break
		print "Enter your move:", 
		move = raw_input()
		#print move
		x = re.search('r[0-{0}]c[0-{0}]'.format(len(board)-1),move)
		if (x):
			if is_spot_available(board,move):
				board = update_board(board,difficulty, move) #player's move
				num_moves_left -=1
				if (is_won(board, False)):
					print "\n=========YOU WIN!==========="
					print_board(board)
					break

				if num_moves_left == 0:
					print "\n========IT'S A DRAW!==========="
					print_board(board)
					break

				board = update_board(board,difficulty) #computer's move
				num_moves_left -=1
				if is_won(board, True):
					print "\n==========YOU LOST!============"
					print_board(board)
					break
				print_board(board)
			else:
				print "That spot is already taken..try again"
		else:
			print "That's an invalid position...try again"


def make_board(board_size):
	Board = []
	for row in range(board_size):
		Board.append([])
		for col in range(board_size):
			Board[row].append("-")
			Board[row][col] = "r{}c{}".format(row,col)
	print Board
	return Board
	#L = []
	#for i in range(board_size*board_size):
	#	L.append(i)

	#Board = np.array_split(list(Board), board_size)
	#for x in range(0, len(L), board_size):
	#	print x

	#Board =  [L[x:x+board_size] for x in range(0, len(L), board_size)]
	#print Board



T = setup_game()
play_game(T[0], T[1])

"""
def winning_move(player, row_index, col_index):
	
	winner = False
	for item in Board[row_index]: #check for row win
		if item is player:
			winner =  True
		else:

	#for L in Board: #check for column win
	#	if L[col_index] not player:
			notAWinner =  True
	if (Board[0][0] != player and Board[1][1] != player and Board[2][2] != player ):
		notAWinner =  True
	if (Board[2][0] != player and Board[1][1] != player and Board[0][2] != player ):
		notAWinner =  True

"""



