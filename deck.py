class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def getSuit(self):
		return self.suit

	def getValue(self):
		return self.value


class Deck:


	# on init, add 52 Cards to wholeDeck looping through each suit, and each value
	def createNewDeck(self, suits, values):
		thisDeck = []
		for suit in suits:
			for value in values:
				thisDeck.append(Card(suit, value))
		return thisDeck
					

	def __init__(self):
		self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		self.values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
		self.wholeDeck = self.createNewDeck(self.suits, self.values)


	def getSuits(self):
		return self.suits

	def getDeckLength(self):
		return len(self.wholeDeck)

	def getDeck(self):
		return self.wholeDeck
