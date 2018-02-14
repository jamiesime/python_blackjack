class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def getSuit(self):
		return self.suit

	def getValue(self):
		return self.value


class Deck:

	# cardvalues = {"Ace" : 11, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "King" : 10, "Queen" : 10, "Jack" : 10}

	# on init, add 52 Cards to wholeDeck looping through each suit, and each value
	def createNewDeck(self, suits, values):
		thisDeck = []
		for suit in suits:
			for valStr, valInt in values.items():
				thisDeck.append(Card(suit, {valStr : valInt}))
		return thisDeck
					

	def __init__(self):
		self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		self.values = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "King" : 10, "Queen" : 10, "Jack" : 10}
		self.wholeDeck = self.createNewDeck(self.suits, self.values)


	def getSuits(self):
		return self.suits

	def getDeckLength(self):
		return len(self.wholeDeck)

	def getDeck(self):
		return self.wholeDeck
