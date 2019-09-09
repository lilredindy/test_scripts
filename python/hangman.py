#!/usr/bin/python2.7


class Hangman:
	def __init__(self):
		self.answer = None
		self.correct = []
		self.incorrect = []

	def answer_key(self):
		for s in self.answer:
			if s in self.correct:
				print s,
			else:
				print "_",
		print 
		print 

	def tree_print(self, level=None):
		if not level:
			level = len(self.incorrect)
		
		#print "level is: %d" % level

		if (level == 0):
			print "    ____"
			print "   |    |"
			print "        |"
			print "        |"
			print "        |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 1):
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "        |"
			print "        |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 2):
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "   |    |"
			print "        |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 3):
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "  /|    |"
			print "        |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 4):
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "  /|\\   |"
			print "        |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 5):
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "  /|\\   |"
			print "  /     |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print ""	
			self.answer_key()
			print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		elif (level == 6):
			print "Sorry, you lose!"  
			print 
			print 
			print "    ____"
			print "   |    |"
			print "   o    |"
			print "  /|\\   |"
			print "  / \\   |"
			print "        |"
			print "        |"
			print "  ----------"
			print ""
			print "The correct word is: " + self.answer	
			#self.answer_key()
			#print 'Incorrect: [%s]' % ', '.join(map(str, self.incorrect))
			#print 'Correct: [%s]' % ', '.join(map(str, self.correct))
			print 

		else:
			print "No level is given"



	def generate_word(self):
			
		word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

		response = requests.get(word_site)
		WORDS = response.content.splitlines()

		#print (response,WORDS)

		while (True):
			r = randint(0, len(WORDS)-1)
			self.answer = WORDS[r].lower()
			if self.answer.isalpha() and len(self.answer) > 2:
				return self.answer

		return self.answer #does this need to be here?


	def update_board(self, guess):
		#print "answer right now is:" + self.answer

		result = True
		if guess in self.answer:
			if guess not in self.correct:
				#print "That's correct" 
				self.correct.append(guess)
				self.tree_print()
			else:
				print "That is already been guessed...try again"

		elif guess in self.incorrect:
			print "That is already been guessed...try again"
		else:
			#print "\nSorry that's incorrect" 
			self.incorrect.append(guess)
			if len(self.incorrect) == 6:
				print "Game over, you lose"	
				result = False
			self.tree_print()
		return result

	def rules(self):
		print "------------------RULES---------------------"	
		print "For each move enter a letter or guess the" 
		print "full word."
		print "Six incorrect letter guesses and the game is over."
		print "Guess the word incorrectly and also you lose."
		print "---------------------------------------------"	


if __name__ == "__main__" :

	import requests
	from random import *



	hang = Hangman()
	hang.rules()

	answer = hang.generate_word() #can't the hangman init do this?

	while (True):
		#print answer
		print "\n___________________________________________"
		print "\nEnter a letter or guess the answer:", 
		guess = raw_input()

		if (guess == answer):
			print "Yay! you guessed the correct word: " + guess
			break

		if (guess.isalpha()):
			if len(guess) == 1:
				if not hang.update_board(guess):
					break
			else:
				hang.tree_print(6)
				break
		else:
			print "That's an invalid entry...try again.."

