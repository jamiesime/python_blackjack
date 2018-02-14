import random
import time
from player import Player
from deck import Card, Deck

class Game:

	def __init__(self, deck, players):
		self.deck = deck
		self.players = players

	# initial display and takes number of players to play game
	def intro(self):
		print("")
		print("S I M P L E   B L A C K J A C K")
		print("")	
		print("How many players? (1-6)")
		try:
			numOfPlayers = int(input())
			if(numOfPlayers in (1, 2, 3, 4, 5, 6)):
				for i in range(1, (int(numOfPlayers) + 1)):
					print("Player " + str(i) + ", please enter your name.")
					playerName = input()
					self.players.append(Player(playerName, []))

			else:
				print("Out of range!")
				self.intro()
		except ValueError:
			print("Not a number!")
			self.intro()

	def newDeck(self):
		self.deck = Deck()

	# randomises deck, with short wait implemented for comprehensibility
	def shuffleDeck(self, deck):
		print("Shuffling deck...")
		time.sleep(1)
		print("...")
		time.sleep(1)
		random.shuffle(deck.wholeDeck)
		# for card in deck.wholeDeck:
		# 	print (str(card.value) + "of" + card.suit)

	# loops through players list and pops off first two cards in randomised deck, adding to each player's card list
	def initialDeal(self):
		print("Initial hands dealt!")
		time.sleep(1)
		for player in self.players:
			firstCard = self.deck.wholeDeck.pop(0)
			secondCard = self.deck.wholeDeck.pop(0)
			player.cards.append(firstCard)
			player.cards.append(secondCard)

	# displays current hand information, determines if player is bust, and if not, continues on to turnOptions
	def currentTurn(self, currentPlayer):
		thisPlayer = self.players[currentPlayer]
		print("<>------------- " + thisPlayer.name + "'s turn! --------------<>")
		self.displayHand(thisPlayer)
		bust = self.checkForBust(thisPlayer)
		if bust == True:
			time.sleep(1)
			print(thisPlayer.name + " has gone bust! Out of the round!")
			# self.players.pop(currentPlayer)
			time.sleep(1)
		else:
			self.turnOptions(currentPlayer)

	def displayHand(self, thisPlayer):
		print("Your hand is: ")
		for card in thisPlayer.cards:
			# casts card keys dict to list to allow access of index 0
			# this allows access to the name of the card, rather than an int value
			cardName = list(card.value.keys())
			print(str(cardName[0]) + " of " + card.suit)


	def turnOptions(self, currentPlayer):
		thisPlayer = self.players[currentPlayer]
		print("Press 1 to Stand")
		print("Press 2 to Hit")
		try:
			choice = int(input())
			if choice == 1:
				print(thisPlayer.name + " will stand!")
				return
			elif choice == 2:
				print(thisPlayer.name + " takes another card!")
				self.playerHit(thisPlayer)
				self.currentTurn(currentPlayer)
			else:
				print("That's not an option!")
				self.turnOptions(currentPlayer)
		except ValueError:
			print("That's not an option!")
			self.turnOptions(currentPlayer)

	# adds a card to given players card list
	def playerHit(self, player):
		nextCard = self.deck.wholeDeck.pop(0)
		player.cards.append(nextCard)
		cardValue = list(nextCard.value.values())
		print(player.name + " drew a " + str(cardValue[0]) + " of " + nextCard.suit)
		time.sleep(1)

	# determines total value of given players card list and returns true or false depending on if over 21 
	def checkForBust(self, player):
		handTotal = 0
		for card in player.cards:
				# casts card values dict to list to allow access of index 0
				# the list/values will only ever have one entry
				cardVal = list(card.value.values())
				handTotal += int(cardVal[0])
		print("Hand value: " + str(handTotal))
		if handTotal > 21:
			return True
		return False

	


# START OF GAME
gameOver = False
thisGame = Game([], [])
thisGame.intro()
thisGame.newDeck()
thisGame.shuffleDeck(thisGame.deck)
thisGame.initialDeal()
currentPlayer = 0

# GAME LOOPS UNTIL END STATE
while (gameOver == False):
	thisGame.currentTurn(currentPlayer)
	if(currentPlayer < len(thisGame.players) - 1):
		currentPlayer += 1
	else:
		gameOver = True;

# RESTART OPTION