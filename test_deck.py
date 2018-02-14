import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

	def setUp(self):
		self.deck = Deck()

	def testGetFourSuits(self):
		self.assertTrue(len(self.deck.getSuits()) == 4)

	def testDeckLength(self):
		self.assertTrue(self.deck.getDeckLength() == 52)


def main():
	unittest.main()

if __name__ == '__main__':
	main()