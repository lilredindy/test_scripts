##################
#    c1 c2 c3
#r1   -  -  -
#r2   -  -  -
#r3   -  -  -
##################

import numpy as np
import re

class Computer:
	def __init__(self, difficulty):
		self.difficulty = difficulty

	def move(self, current_board):
		if (self.difficulty == "easy"):
			return self.easy(current_board)
		elif (self.difficulty == "medium"):
			return self.medium(current_board)
		else:
			return self.hard(current_board)


	def easy(self,current_board):
		for i, sublist in enumerate(current_board.data):
			for j,item in enumerate(sublist):
				if (item != 'O' and item != 'X'):
					return ('r'+str(i)+'c'+str(j))
					#self.data[i][j] = 'X'
					#self.stats['r{}'.format(i)][1] +=1
					#self.stats['c{}'.format(j)][1] +=1
					#return

	def medium(self):
		return move


	def hard(self, current_board):
		#defensive 
		#1. check opponent
		for key, value in current_board.stats.items():
			print key,value
			if value[0] == current_board.board_size -1: #value[0] is num of O's 
				if key.startswith('r'): #block opponent's row win
					r = int(key[1])
					for c in range(current_board.board_size): 
						if current_board.data[r][c] != 'O' and current_board.data[r][c] != 'X':
							print "about to mark with X"
							return ('r'+str(r)+'c'+str(c))

							#self.data[r][c] = 'X'
							#self.stats['r{}'.format(r)][1] +=1
							#self.stats['c{}'.format(c)][1] +=1
							#return
				else: #block opponnent's col win
					c = int(key[1])
					for r in range(current_board.board_size): 
						if current_board.data[r][c] != 'O' and current_board.data[r][c] != 'X':
							print "about to mark with X"
							return ('r'+str(r)+'c'+str(c))

							#self.data[r][c] = 'X'
							#self.stats['r{}'.format(r)][1] +=1
							#self.stats['c{}'.format(c)][1] +=1
							#return
				
		#block diaganol 1
		count = 0
		index = None
		for i in range(current_board.board_size):
			if (current_board.data[i][i] == 'O'): 
				count += 1 
			elif (current_board.data[i][i] == 'X'): #already blocked
				break #opponent can't win diagonal 1 
			else: 
				index = i  #99.9% last empty
		
		if current_board.board_size - count == 1: 
			return ('r'+str(index)+'c'+str(index))

			#self.data[index][index] = 'X'
			#self.stats['r{}'.format(index)][1] +=1
			#self.stats['c{}'.format(index)][1] +=1
			#return 

		#block diaganol 2
		count = 0
		index = None
		for i in range(current_board.board_size):
			if (current_board.data[current_board.board_size-1-i][i] == 'O'): 
				count += 1 
			elif (current_board.data[current_board.board_size-1-i][i] == 'X'): #already blocked
				break  #opponent can't win diagonal 2
			else: 
				index = i  #99.9% last empty

		if current_board.board_size - count == 1: 
			return ('r'+str(current_board.board_size-1-index)+'c'+str(index))

			#self.data[self.board_size-1-index][index] = 'X'
			#self.stats['r{}'.format(self.board_size-1-index)][1] +=1
			#self.stats['c{}'.format(index)][1] +=1
			#return 


		return self.easy(current_board) #X marks normally



		



class Board:
	def __init__(self, board_size):
		self.board_size = board_size
		self.data = []
		self.stats = {} #[{r0:[]},{r1:[]}]
		for i in range(self.board_size):
			self.stats["r{}".format(i)]=[0,0]
			self.stats["c{}".format(i)]=[0,0]


	def make(self):
		for row in range(self.board_size):
			self.data.append([])
			for col in range(self.board_size):
				self.data[row].append("-")
				self.data[row][col] = "r{}c{}".format(row,col)

		print (self.data)
		print (self.stats)

	def update(self,move=None, is_computer=False):
		for i, sublist in enumerate(self.data):
			for j,item in enumerate(sublist):
				if (item == move):
					if is_computer:
						self.data[i][j] = 'X'
						self.stats['r{}'.format(i)][1] +=1
						self.stats['c{}'.format(j)][1] +=1 
						return		
					else:
						self.data[i][j] = 'O'
						self.stats['r{}'.format(i)][0] +=1
						self.stats['c{}'.format(j)][0] +=1 
						return


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
	rules()
	print "Enter size of board, e.g., 3 indicates 3x3:" ,
	board_size = raw_input()
	print "Enter the dificulty level [easy, medium, hard]: ",
	dificulty = raw_input()
	#make_board(int(board_size))
	board = Board(int(board_size))
	board.make()
	board.print_me()
	c = Computer(dificulty)

	
	num_moves_left = pow(len(board.data), 2)
	while (True):
		if num_moves_left == 0:
			print "IT'S A DRAW!"
			board.print_me()
			break
		print "Enter your move:", 
		move = raw_input()
		#print move
		x = re.search('r[0-{0}]c[0-{0}]'.format(len(board.data)-1),move)
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

				board.update(c.move(board), True) #either calls board.update or returns move
				num_moves_left -=1
				if board.is_won(True):
					print "\n==========YOU LOST!============"
					board.print_me()
					break
				board.print_me()
			else:
				print "That spot is already taken..try again"
		else:
			print "That's an invalid position...try again"




play_game()
