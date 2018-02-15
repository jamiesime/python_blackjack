import unittest
from deck import Deck, Card

class TestDeck(unittest.TestCase):

	def setUp(self):
		self.deck = Deck()

	def testGetFourSuits(self):
		self.assertTrue(len(self.deck.getSuits()) == 4)

	def testDeckLength(self):
		self.assertTrue(self.deck.getDeckLength() == 52)

	# def testValueDict(self):
	# 	for card in self.deck.wholeDeck:
	# 		print(card.value.keys())
	# 		print(card.value.values())

	def testCheckForAce(self):
		aceCard = Card("Spades", {"Ace" : 11})
		name = list(aceCard.value.keys())[0]
		self.assertTrue(name == "Ace")

def main():
	unittest.main()

if __name__ == '__main__':
	main()