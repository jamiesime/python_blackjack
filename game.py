import random
from player import Player
from deck import Card, Deck

class Game:

	def __init__(self, deck, players):
		self.deck = deck
		self.players = players

	def shuffleDeck(self, deck):
		random.shuffle(deck.wholeDeck)
		for card in deck.wholeDeck:
			print (str(card.value) + "of" + card.suit)

	def newDeck(self):
		self.deck = Deck()

	def intro(self):
		print("Welcome to blackjack. How many players? (1-6)")
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
	


thisGame = Game([], [])
thisGame.intro()
thisGame.newDeck()
thisGame.shuffleDeck(thisGame.deck)
