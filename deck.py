class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def getSuit(self):
		return self.suit

	def getValue(self):
		return self.value


class Deck:

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

	def getDeck(self):
		for card in self.wholeDeck:
			print (str(card.value) + " of " + card.suit)
		print(str(len(self.wholeDeck)))
		return self.wholeDeck


newDeck = Deck()
newDeck.getDeck()