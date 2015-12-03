
class Card:
	copy = []
	counter = 0
	copyxs2 = []
	replace = []
	d1 = []
	#the d list is similar to cardValue but contains
	#all strings for better matching of some container values
	d = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	cardSuit = ["C","D","H","S","P"]
	cardValue = [2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
	
	def __init__(self,rank,suit,xs1,run):
		self.rank = rank
		self.suit = suit
		self.xs1 = xs1
		self.run = run
	# create optional print output
	def __str__(self):
		return self.rank + self.suit  
	
		
	def point_val(self):
		if self.rank == "T":
			return 10
		if self.rank == "J":
			return 10
		if self.rank == "Q":
			return 10
		if self.rank == "K":
			return 10
		if self.rank == "A":
			return 15
		else:
			return int(self.rank)
	# draw out the first index 
	def extends_run(self):
		
		copy = []
		self.run.append(self.xs1[0])
		a = len(self.run)
		self.xs1.append(self.run[0])

		xs2 = sorted(sel.fxs1)
	# sorting the container
		for i in xs2:
			if i[0] == "T":
				self.replace.append(i)
				xs2.remove(i)
		for i in xs2:
			if i[0] == "J":
				self.replace.append(i)
				xs2.remove(i)
		for i in xs2:
			if i[0] == "Q":
				self.replace.append(i)
				xs2.remove(i)
		for i in xs2:
			if i[0] == "K":
				self.replace.append(i)
				xs2.remove(i)
		for i in xs2:
			if i[0] == "A":
				self.replace.append(i)
				xs2.remove(i)
			
		for i in self.replace:
			xs2.append(i)
		# checks to see if they match
		# careful with self. constructors and
		# non-self var assignments (confusing)
		for i in range(0,len(xs2)):
			self.copyxs2.append(xs2[i][0])
		copyxs3 = set(self.copyxs2)
		copyd = set(self.d)
		diff = copyd - copyxs3
		for i in self.d:
			if i not in  diff:
				self.d1.append(i)
		if copyxs2 == self.d1:
			print("great job")
		else:
			print("no good")

# create the Hand class		
class Hand:
	counter = 0
	tenList = ["T","J","Q","K"]
# create the constructor for hand	
	def __init__(self,playerCards):
		self.playerCards = playerCards
		
# create the point value method
# all face cards except for A is 10
# A is 15
# numbers match up to their real life counterparts		
	def hand_point_value(self):
		for i in self.playerCards:
			if i[0] in self.tenList:
				self.counter += 10
			elif i[0] == "A":
				self.counter += 15
			else:
				self.counter += int(i[0])
		return self.counter
	
	def __str__(self):
		return self.playerCards			
					
# create the Player class		
class Player:
	counter = 0
	sumcheck = 0
	counter = 0
	copyxs2 = []
	replace = []
	d1 = []
	# will need this d list to match for runs
	d = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	
	checkList = []
	# create the constructor
	# this constructor contains the most parameters
	def __init__(self,hand,cScore,name,discard,deck,p1MeldRun):
		self.hand = hand
		self.cScore = cScore
		self.name = name
		self.discard = discard
		self.deck = deck
		self.p1MeldRun = p1MeldRun
	def __str__(self):
		pass
	# take turn is the longest method since it will
	# contain whatever happens when player has to 
	# select hands until he discards and switches players
	def take_turn(self):
		print()
		self.checkList = []
		print("your hand: ",self.hand)
		menuD()
		check_input = True
		while check_input:
			try:
				choiceD = int(input("Please enter menu choice: "))
				check_input = False
			except ValueError as e:
				print(e)
				
	# this is where the D menu occurs		
		if choiceD == 1:
			self.hand.append(self.deck[0])
			self.deck.pop(0)
		elif choiceD == 2:
			self.hand.append(self.discard[0])
			self.discard.pop()

			
		print("player 1 hand is: ", self.hand)
		print("top card of discard pile is: ", self.discard)
		print("playing deck is: ", self.deck)
		
		
	# for listing the player cards for selection for run or
	# meld	
		handprint = sorted(self.hand)
		print("Menu F: Select Cards")
		for k in range(0,len(self.hand)):
			print(str(k)+". "+str(self.hand[k]))
			
		cards = eval(input("Please make cards selection: "))
		for q in cards:
			self.checkList.append(self.hand[q])
		print("Your chosen cards are: " + str(self.checkList))
		check = False
		cool = True
		
		while cool:
			
			print("your card hand is: ", self.hand)
			menuE()
			choiceE = int(input("Please enter your menu choice: "))
			if choiceE == 1:
				# checking for melds
				
				handcopy = self.checkList[0][0]
				print("meld common: ", handcopy)
				for i in range(0,len(self.checkList)):
					if self.checkList[i][0] == handcopy:
						self.counter += 1
				if self.counter > 2 and self.counter == len(handcopy):
					print("GREAT, YOU HAVE MELD!")
					# if Meld checks out append it to list
					for i in self.checkList:
						self.p1MeldRun.append(i)
					self.checkList = []
					self.counter = 0
					print("meld/run list is: ", self.p1MeldRun)
					print("Your current hand is: ", self.hand)
					for z in self.p1MeldRun:
						for i in self.hand:
							if z == i:
								self.hand.remove(i)
					print("new current hand is: ", self.hand)
					
					
					
					
				else:
					print("nope meld yet!")
					
					
				# here is where we check the run, used sort from meld 
				# again
				self.counter = 0
				self.copyxs2 = []
				self.replace = []
				self.d1 = []

				xs2 = sorted(self.checkList)

				for i in xs2:
					if i[0] == "T":
						self.replace.append(i)
						xs2.remove(i)
				for i in xs2:
					if i[0] == "J":
						self.replace.append(i)
						xs2.remove(i)
				for i in xs2:
					if i[0] == "Q":
						self.replace.append(i)
						xs2.remove(i)
				for i in xs2:
					if i[0] == "K":
						self.replace.append(i)
						xs2.remove(i)
				for i in xs2:
					if i[0] == "A":
						self.replace.append(i)
						xs2.remove(i)
			
				for i in self.replace:
					xs2.append(i)


				for i in range(0,len(xs2)):
					
					self.copyxs2.append(xs2[i][0])
				# almost lost track of all the lists I made
				# so confusing at times
				copyxs3 = set(self.copyxs2)


				copyd = set(self.d)
				
				diff = copyd - copyxs3
				print()
				
				for i in self.d:
					if i not in  diff:
						self.d1.append(i)
		
			 	# if they match then add to the meld/run list
				if self.copyxs2 == self.d1:
					
					for i in self.checkList:
						self.p1MeldRun.append(i)
					
					self.counter = 0
					print("meld/run list is: ", self.p1MeldRun)
					print("Your current hand is: ", self.hand)
					for z in self.p1MeldRun:
						for i in self.hand:
							if z == i:
								self.hand.remove(i)
					
							
				else:
					print("no good")
				

			

				# run the list of hands again for selection
				# had to put this here since I didn't know how to 
				# loop back up and have it repeat the menu AND 
				# cards in hand	
				handprint = sorted(self.hand)
				print("Menu F: Select Cards")
				for k in range(0,len(self.hand)):
					print(str(k)+". "+str(self.hand[k]))
			
				cards = eval(input("Please make cards selection: "))
				for q in cards:
					self.checkList.append(self.hand[q])
				print("Your chosen cards are: " + str(self.checkList))
			
					
				
			
			elif choiceE == 2:
				print("discard hand!")
				self.checkList = []
				cool = False
				
	def __str__(self):
		return self.checkList				
			
			
			
				
# creating the score table class				
class ScoreTable:
	f = ""
	counter = 0
	a = []
	b = []
	c = []
	d = []
	e = []
	oldNames = []
	container = []
	newcontainer = []
	# creating the constructor
	def __init__(self,statsList):
		self.statsList = statsList
		
		
	def read_scores(self):
		self.f = open('ScoresTable','rU')
		# iteration excluding the new line character
	
		for i in self.f:
			print(i[:-1])
		self.f.close()

		
	def save_scores(self):
		# saves the scores and closes the file
		self.f = open('ScoresTable','w+')
		for i in self.statsList:
			self.f.write(str(i))
		self.f.close()
		
	def __str__(self):
		return self.statsList
		
		

	

                     
def menu():
	menu = """
	1. View scores
	2. Play 2-player game
	3. Play 3-player game
	4. play 2-player game with stacked deck
	5. Play 3-player game with stacked deck
	6. Quit"""
	print(menu)

def menuB():
	menu = """
	1. new player
	2. returning player"""
	print(menu)
# menu to select which old player to use
# hardest menu to create	
def menuC(oldNames):

	counter = 0
	a = []
	b = []
	c = []
	d = []
	e = []
	oldNames = []
	
	f = open('/Users/Nguyen/Documents/az1/chjo.txt','rU')
	
	container = []
	for i in f:
		container.append(i[:-1])
		f = container

	
	box = []
	for i in f:
		erase = i.replace('\"', "")
		box.append(erase)

	
	
	for i in container:
		print(i[0])

	for z in container:	
		d = z.split(",")
		e.append(d)
	
	

	for i in range(1,len(e)):
		print(e[i][0])
		oldNames.append(e[i][0])
	
	print()
	print(oldNames)
	print()
	print("Menu C: Choose Previous Player: ")
	for j in range(0,len(oldNames)):
		print(str(j) + ". " + str(oldNames[j]))
	return oldNames
	
		
	
# create Menu D
def menuD():
	menu = """
	Menu D: Which Card to Draw
	1. Draw from stock pile
	2. Draw from discard pile"""
	print(menu)
# create Menu E 	
def menuE():
	menu = """
	Menu E: Next Action
	1. Play down cards
	2. Discard"""
	print(menu)
	

		

	
def fullDeck():
	
	cardList = []
	s = "2C 3C 4C 5C 6C 7C 8C 9C TC JC QC KC AC 2D 3D 4D 5D 6D \
	7D 8D 9D TD JD QD KD AD 2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH AH \
	2S 3S 4S 5S 6S 7S 8S 9S TS JS QS KS AS 2P 3P 4P 5P 6P 7P 8P 9P \
	TP JP QP KP AP"
	codes = s.split()
	for code in codes:
		cardList.append(code)
	
	return cardList
	
# clear screen function	
def clear_screen():
	import os
	if os.name == "posix":
		clear_cmd = "clear"
	elif os.name == "nt":
		clear_cmd = "cls"
	else:
		raise Exception ("\n\n\n*** Unsupported System \
		***\nApplication Terminating !!!\n\n\n")
	os.system(clear_cmd)

# the main calling function
# create some lists and set a score to zero
# might not use all of them just to have
# for possible use
def main():
	# import random module for shuffling decks 
	import random
	
	playerList = []	
	cScore = 0
	player1 = []
	player2 = []
	player3 = []
	playerOne = []
	playerTwo = []
	playerThree = []
	p1MeldRun = []
	p2MeldRun = []
	p3MeldRun = []
	discard = []
	round = 0
	game = 0
	
	
	# set boolean sentinel to loop through main menu
	need_input = True
	while need_input:
		menu()
		until = True
		while until:
			try:
				choice = int(input("PLEASE ENTER YOUR CHOICE: "))
				until = False
			except ValueError as e:
				print(e)
		
		
		
		# mostly used choice 2 as the test for my 
		# entire project
		if choice == 2:
			# since it's two players have it cycle through 
			# this
			for i in range(1,3):
				menuB()
				
				
				until1 = True
				while until1:
					try:
						playerType = int(input("Choose the player type: "))
						until1 = False
					except Exception as e:
						print(e)
				
				
				
				
				if playerType == 1:
					pName = input("Please enter your name: ")
					playerList.append(pName)
				if playerType == 2:
					oldNames = []
					old = menuC(oldNames)
					
					oldName = int(input("Please choose a player: "))
					oldPlayer = old[oldName]
					playerList.append(oldPlayer)
					
		### this is where we start the game for players!!!!			
			print("The players are: ", playerList)
			playingDeck = fullDeck()
			
			random.shuffle(playingDeck)
		
			
		# make sure the deck is shuffled
			player1.append(playingDeck[0:10])
			del playingDeck[0:10]
			player2.append(playingDeck[0:10])
			del playingDeck[0:10] 
			discard.append(playingDeck[0])
			del playingDeck[0]
			for i in player1:
				for j in i:
					playerOne.append(j)
			for i in player2:
				for j in i:
					playerTwo.append(j)
				
			print("The discard card is: ", discard[0])

			print()

			good = True
			while good:
				for i in range(0,len(playerList)):
					
					p1 = Player(playerOne,0,"chris",discard,playingDeck,p1MeldRun)
					# if players cards are empty round is over and add one point
					# if three rounds have progressed then game is over
					print(p1.take_turn())
					if p1.hand == []:
						round += 1
						if round == 3:
							game += 1
					good = False
					clear_screen()
					p2 = Player(playerTwo,0,"bill",discard,playingDeck,p1MeldRun)
					print(p2.take_turn())
					if p2.hand == []:
						round += 1
						if round == 3:
							game += 1
					clear_screen()
					good = False
					
					
		
		
		if choice == 3:
			for i in range(1,4):
				menuB()
				
				until2 = True
				while until2:
					try:
						playerType = int(input("Choose the player type: "))
						until2 = False
					except Exception as e:
						print(e)
						
				if playerType == 1:
					pName = input("Please enter your name: ")
					playerList.append(pName)
				if playerType == 2:
					oldNames = []
					old = menuC(oldNames)
					
					oldName = int(input("Please choose a player: "))
					oldPlayer = old[oldName]
					playerList.append(oldPlayer)
					
		### this is where we start the game for 1ST PLAYER!!!!			
			
			

			playingDeck = fullDeck()
		
	
	
			player1.append(playingDeck[0:10])
			del playingDeck[0:10]
			player2.append(playingDeck[0:10])
			del playingDeck[0:10] 
			discard.append(playingDeck[0])
			del playingDeck[0]
			for i in player1:
				for j in i:
					playerOne.append(j)
			for i in player2:
				for j in i:
					playerTwo.append(j)
				
			print("The discard card is: ", discard[0])
			
			print()
			print(playingDeck)
			good = True
			while good:
				p1 = Player(playerOne,0,"chris",discard,playingDeck,p1MeldRun)
				# if players cards are empty round is over and add one point
				# if three rounds have progressed then game is over
				print(p1.take_turn())
				if p1.hand == []:
					round += 1
					if round == 3:
						game += 1
				good = False
				clear_screen()
				p2 = Player(playerTwo,0,"bill",discard,playingDeck,p1MeldRun)
				print(p2.take_turn())
				if p2.hand == []:
					round += 1
					if round == 3:
						game += 1
				clear_screen()
				good = False
		if choice == 4:
			# almost the exact same code as before
			for i in range(1,3):
				menuB()
				until3 = True
				while until3:
					try:
						playerType = int(input("Choose the player type: "))
						until3 = False
					except Exception as e:
						print(e)
				
				
				if playerType == 1:
					pName = input("Please enter your name: ")
					playerList.append(pName)
				if playerType == 2:
					oldNames = []
					old = menuC(oldNames)
					
					oldName = int(input("Please choose a player: "))
					oldPlayer = old[oldName]
					playerList.append(oldPlayer)
					
		### this is where we start the game for 1ST PLAYER!!!!	
		    # this time using stack deck		
			f = open("the.deck","rU")
			s = f.read()
			cardDeck= s.split()
			playingDeck = cardDeck[:]
	
	
	
			# same 10 card distribution to each player
			player1.append(playingDeck[0:10])
			del playingDeck[0:10]
			player2.append(playingDeck[0:10])
			del playingDeck[0:10] 
			discard.append(playingDeck[0])
			del playingDeck[0]
			for i in player1:
				for j in i:
					playerOne.append(j)
			for i in player2:
				for j in i:
					playerTwo.append(j)
			# display the discard card	
			print("The discard card is: ", discard[0])
			print(playerOne)
			print(playerTwo)
			print()
			print(playingDeck)
			good = True
			while good:
				p1 = Player(playerOne,0,"chris",discard,playingDeck,p1MeldRun)
				# if players cards are empty round is over and add one point
				# if three rounds have progressed then game is over
				print(p1.take_turn())
				if p1.hand == []:
					round += 1
					if round == 3:
						game += 1
				clear_screen()
				good = False
				p2 = Player(playerTwo,0,"bill",discard,playingDeck,p1MeldRun)
				print(p2.take_turn())
				if p2.hand == []:
					round += 1
					if round == 3:
						game += 1
				good = False
				clear_screen()						
		if choice == 5:
			# almost exactly the same code as before
			for i in range(1,4):
				menuB()
				until4 = True
				while until4:
					try:
						playerType = int(input("Choose the player type: "))
						until4 = False
					except Exception as e:
						print(e)
				if playerType == 1:
					pName = input("Please enter your name: ")
					playerList.append(pName)
				if playerType == 2:
					oldNames = []
					old = menuC(oldNames)
					
					oldName = int(input("Please choose a player: "))
					oldPlayer = old[oldName]
					playerList.append(oldPlayer)
					
		### this is where we start the game for 1ST PLAYER!!!!			
			f = open("the.deck","rU")
			s = f.read()
			cardDeck= s.split()
			playingDeck = cardDeck[:]
	
	
	
			player1.append(playingDeck[0:10])
			del playingDeck[0:10]
			player2.append(playingDeck[0:10])
			del playingDeck[0:10] 
			discard.append(playingDeck[0])
			del playingDeck[0]
			for i in player1:
				for j in i:
					playerOne.append(j)
			for i in player2:
				for j in i:
					playerTwo.append(j)
				
			print("The discard card is: ", discard[0])
			print(playerOne)
			print(playerTwo)
			print()
			print(playingDeck)
			good = True
			while good:
				p1 = Player(playerOne,0,"chris",discard,playingDeck,p1MeldRun)
				# if players cards are empty round is over and add one point
				# if three rounds have progressed then game is over
				print(p1.take_turn())
				if p1.hand == []:
					round += 1
					if round == 3:
						game += 1
				good = False
				clear_screen()
				p2 = Player(playerTwo,0,"bill",discard,playingDeck,p1MeldRun)
				print(p2.take_turn())
				if p2.hand == []:
					round += 1
					if round == 3:
						game += 1
				clear_screen()
				good = False	
		# quit the program	
		if choice == 6:
			print("Thanks for playing!")
			quit()	
			
# run the show					
main()  
