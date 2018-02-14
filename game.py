import random
import time
from player import Player
from deck import Card, Deck

class Game:

	def __init__(self, deck, players):
		self.deck = deck
		self.players = players

	def shuffleDeck(self, deck):
		print("Shuffling deck...")
		time.sleep(1)
		print("...")
		time.sleep(1)
		random.shuffle(deck.wholeDeck)
		# for card in deck.wholeDeck:
		# 	print (str(card.value) + "of" + card.suit)

	def newDeck(self):
		self.deck = Deck()

	def intro(self):
		print("W E L C O M E    T O     B L A C K J A C K")
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


	def initialDeal(self):
		print("Initial hands dealt!")
		time.sleep(1)
		for player in self.players:
			firstCard = self.deck.wholeDeck.pop(0)
			secondCard = self.deck.wholeDeck.pop(0)
			player.cards.append(firstCard)
			player.cards.append(secondCard)

	def playerHit(self, player):
		nextCard = self.deck.wholeDeck.pop(0)
		player.cards.append(nextCard)
		print(player.name + " drew a " + str(nextCard.value) + " of " + nextCard.suit)

	def checkForBust(self, player):
		handTotal = 0
		for card in player.cards:
				# casts card value to list to allow access of index 0
				# the list will only have one entry
				cardVal = list(card.value.values())
				handTotal += int(cardVal[0])
		print("Hand value: " + str(handTotal))
		if handTotal > 21:
			return True
		return False

	def currentTurn(self, currentPlayer):
		thisPlayer = self.players[currentPlayer]
		print("<>------------- " + thisPlayer.name + "'s turn! --------------<>")
		print("Your hand is: ")
		for card in thisPlayer.cards:
			cardName = list(card.value.keys())
			print(str(cardName[0]) + " of " + card.suit)
		bust = self.checkForBust(thisPlayer)
		if bust == True:
			print("You've gone bust! You're out!")
			self.players.pop(currentPlayer)
		else:
			self.turnOptions(currentPlayer)


	def turnOptions(self, currentPlayer):
		thisPlayer = self.players[currentPlayer]
		print("Press 1 to Stand")
		print("Press 2 to Hit")
		try:
			choice = int(input())
			if choice == 1:
				print(thisPlayer.name + " will stand!")
			elif choice == 2:
				print(thisPlayer.name + " takes another card!")
				self.playerHit(thisPlayer)
				self.currentTurn(currentPlayer)
				self.turnOptions(currentPlayer)
			else:
				print("That's not an option!")
				self.turnOptions(currentPlayer)
		except ValueError:
			print("That's not an option!")
			self.turnOptions(currentPlayer)


	


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