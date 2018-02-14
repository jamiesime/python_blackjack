import random
from player import Player
from deck import Card, Deck

class Game:

	def __init__(self):
		self.deck = []
		self.players = []

	def intro():
		print("Welcome to blackjack. Please enter your name.")
		playerName = input()
		player1 = Player(playerName, [])
		print(player1.getName())


	def startNewGame(self):
		self.deck = Deck()

	def shuffleDeck(deck):
		random.shuffle(deck)




Game.intro()