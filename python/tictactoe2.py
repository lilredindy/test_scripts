#!/usr/bin/python2.7
##################
#    c1 c2 c3
#r1   -  -  -
#r2   -  -  -
#r3   -  -  -
##################

import numpy as np
import re
from random import *



class Board:
	def __init__(self, board_size, difficulty):
		self.board_size = board_size
		self.difficulty = difficulty
		self.data = []
		self.stats = {} #[{r0:[]},{r1:[]}]
		for i in range(self.board_size):
			self.stats["r{}".format(i)]=[0,0]
			self.stats["c{}".format(i)]=[0,0]


	def setup(self):
		for row in range(self.board_size):
			self.data.append([])
			for col in range(self.board_size):
				self.data[row].append("-")
				self.data[row][col] = "r{}c{}".format(row,col)

		#print (self.data)
		#print (self.stats)

	def update(self,move=None):
		if (move): #opponent's move
			r = int(move[1])
			c = int(move[3])
			self.data[r][c] = 'O'
			self.stats['r{}'.format(r)][0] +=1
			self.stats['c{}'.format(c)][0] +=1 
			return

			"""
			for i, sublist in enumerate(self.data):
				for j,item in enumerate(sublist):
					if (item == move):
						self.data[i][j] = 'O'
						self.stats['r{}'.format(i)][0] +=1
						self.stats['c{}'.format(j)][0] +=1 
						return
			"""
		
		else: #computer's turn
			if self.difficulty == "easy":
				self.easy()
			elif self.difficulty == "medium":
				self.medium()
			else:
				self.hard()

	def random_computer_move(self):
		while(True):
			r = randint(0, self.board_size-1)
			c = randint(0, self.board_size-1)
			#print r,c

			if self.data[r][c] != 'O' and self.data[r][c] != 'X':
				self.data[r][c] = 'X'
				self.stats['r{}'.format(r)][1] +=1
				self.stats['c{}'.format(c)][1] +=1
				return


	def default_computer_move(self): #next open slot in sequence
		for i, sublist in enumerate(self.data):
			for j,item in enumerate(sublist):
				if (item != 'O' and item != 'X'):
					self.data[i][j] = 'X'
					self.stats['r{}'.format(i)][1] +=1
					self.stats['c{}'.format(j)][1] +=1
					return

	def easy(self):
		#self.default_computer_move()
		self.random_computer_move()

	def medium(self):
		if self.computer_plays_defensive():
			return
		self.random_computer_move()


	def hard(self):
		if self.computer_plays_offensive():
			return
		if self.computer_plays_defensive():
			return
		self.random_computer_move() #computer defaults to basic move



	def computer_plays_offensive(self,level=0):
		
		#OFFENSIVE IDEAS
		for key, value in self.stats.items():
			#print key,value
			num_of_X = value[1]  #value[1] is num of X's 
			if num_of_X == self.board_size -1: #computer almost can win. now find where...
				if key.startswith('r'): 
					r = int(key[1])
					for c in range(self.board_size): 
						if self.data[r][c] != 'O' and self.data[r][c] != 'X':
							self.data[r][c] = 'X'
							self.stats['r{}'.format(r)][1] +=1
							self.stats['c{}'.format(c)][1] +=1
							return True
				else: 
					c = int(key[1])
					for r in range(self.board_size): 
						if self.data[r][c] != 'O' and self.data[r][c] != 'X':
							self.data[r][c] = 'X'
							self.stats['r{}'.format(r)][1] +=1
							self.stats['c{}'.format(c)][1] +=1
							return True

		#seperate code for diagonal
		#check for diaganol 1 win
		count = 0
		index = None
		for i in range(self.board_size):
			if (self.data[i][i] == 'X'): 
				count += 1 
			elif (self.data[i][i] == 'O'): #opponent already blocked 
				break  
			else: 
				index = i  #the open slot
		
		if (self.board_size - count == 1) and index:  #edge-case diag filled so check index
			self.data[index][index] = 'X'
			self.stats['r{}'.format(index)][1] +=1
			self.stats['c{}'.format(index)][1] +=1
			return True

		#check for diaganol 2 win
		count = 0
		index = None
		for i in range(self.board_size):
			if (self.data[self.board_size-1-i][i] == 'X'): 
				count += 1 
			elif (self.data[self.board_size-1-i][i] == 'O'): #opponent already blocked 
				break  
			else: 
				index = i  #the open slot

		if (self.board_size - count == 1) and index:  #edge-case diag filled so check index
			self.data[self.board_size-1-index][index] = 'X'
			self.stats['r{}'.format(self.board_size-1-index)][1] +=1
			self.stats['c{}'.format(index)][1] +=1
			return True


		return False


	def computer_plays_defensive(self,level=0):
		#DEFENSIVE IDEAS 
		for key, value in self.stats.items():
			#print key,value
			num_of_O = value[0]
			if num_of_O == self.board_size -1: #value[0] is num of O's 
				if key.startswith('r'): #block opponent's row win
					r = int(key[1])
					for c in range(self.board_size): 
						if self.data[r][c] != 'O' and self.data[r][c] != 'X':
							self.data[r][c] = 'X'
							self.stats['r{}'.format(r)][1] +=1
							self.stats['c{}'.format(c)][1] +=1
							return True
				else: #block opponnent's col win
					c = int(key[1])
					for r in range(self.board_size): 
						if self.data[r][c] != 'O' and self.data[r][c] != 'X':
							self.data[r][c] = 'X'
							self.stats['r{}'.format(r)][1] +=1
							self.stats['c{}'.format(c)][1] +=1
							return True
				
		#block diaganol 1
		count = 0
		index = None
		for i in range(self.board_size):
			if (self.data[i][i] == 'O'): 
				count += 1 
			elif (self.data[i][i] == 'X'): #already blocked
				break 
			else: 
				index = i #the open slot 
		
		if (self.board_size - count == 1) and index:  #edge-case diag filled so check index
			self.data[index][index] = 'X'
			self.stats['r{}'.format(index)][1] +=1
			self.stats['c{}'.format(index)][1] +=1
			return True

		#block diaganol 2
		count = 0
		index = None
		for i in range(self.board_size):
			if (self.data[self.board_size-1-i][i] == 'O'): 
				count += 1 
			elif (self.data[self.board_size-1-i][i] == 'X'): #already blocked
				break  
			else: 
				index = i  #the open slot

		if (self.board_size - count == 1) and index: #edge-case diag filled so check index
			self.data[self.board_size-1-index][index] = 'X'
			self.stats['r{}'.format(self.board_size-1-index)][1] +=1
			self.stats['c{}'.format(index)][1] +=1
			return True


		return False



	def print_me(self):
		print 
		print ("    "),
		for i in range(self.board_size):
			print "c%i "%i,
		print 
		print "   +" + ("----"*self.board_size)+ "+"
		for i, sublist in enumerate(self.data): 
			print "r%i |"%i,
			for item in sublist:
				if item == "O":
					print " O " ,
				elif item == "X":
					print " X ",
				else:
					print " - " , 
			print "|"
		print "   +" + ("----"*self.board_size)+ "+"
		print 


	def is_spot_available(self,move):
		for sublist in self.data:
			for item in sublist:
				if (item == move):
					return  True
		return False


	def is_won(self,is_computer):
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
		for i, sublist in enumerate(self.data):
			colWin = all(sublist[i] == player for sublist in self.data) 
			if (colWin):
				return True
			rowWin = all(item == player for item in sublist) #rows match
			if rowWin:
				return True
			if sublist[i] != player:
				diag1Win = False
			if sublist[self.board_size-1-i] != player:
				diag2Win = False

		if (diag1Win or diag2Win):
			return True

		return False #not a winner




def rules():
	print "------------------RULES---------------------"	
	print "For each move enter a position, e.g. r0c1:"
	print 
	print "     c0  c1  c2"
	print "   +-----------+ "
	print "r0 | -   -   - |"
	print "r1 | -   -   - |"
	print "r2 | -   -   - |"
	print "   +-----------+ "	
	print 
	print "---------------------------------------------"	





def play_game():

	print "Enter size of board, e.g., 3 indicates 3x3:" ,
	board_size = raw_input()
	print "Enter the dificulty level [easy, medium, hard]: ",
	difficulty = raw_input()
	#make_board(int(board_size))
	if difficulty not in ["easy", "medium", "hard"]:
		print "Invalid input...goodbye"
		return
	board = Board(int(board_size),difficulty)
	board.setup()
	board.print_me()

	num_moves_left = pow(len(board.data), 2)
	while (True):
		if num_moves_left == 0:
			print "\n========IT'S A DRAW!==========="
			board.print_me()
			break
		print "Enter your move:", 
		move = raw_input()
		#print move
		x = re.search('^r[0-{0}]c[0-{0}]$'.format(len(board.data)-1),move) #^ begins, $ ends
		if (x):
			if board.is_spot_available(move):
				board.update(move) #player's move
				num_moves_left -=1
				
				if (board.is_won(False)):
					print "\n=========YOU WIN!==========="
					board.print_me()
					break

				if num_moves_left == 0:
					print "\n========IT'S A DRAW!==========="
					board.print_me()
					break

				board.update() #computer's move
				num_moves_left -=1
				if board.is_won(True):
					print "\n==========YOU LOST!============"
					board.print_me()
					break

				board.print_me() # both opponent and computer's moves are printed
			else:
				print "That spot is already taken..try again"
		else:
			print "That's an invalid position...try again"



if __name__ == "__main__" :
	rules()
	play_game()




"""
def make_board(board_size):
	global board
	#Board = []
	for row in range(board_size):
		board.append([])
		for col in range(board_size):
			board[row].append("-")
			board[row][col] = "r{}c{}".format(row,col)
	print board
	return board
	#L = []
	#for i in range(board_size*board_size):
	#	L.append(i)

	#Board = np.array_split(list(Board), board_size)
	#for x in range(0, len(L), board_size):
	#	print x

	#Board =  [L[x:x+board_size] for x in range(0, len(L), board_size)]
	#print Board
"""

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



