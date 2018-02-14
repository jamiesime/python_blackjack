import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

	def setUp(self):
		self.deck = Deck()

	def testGetSuits(self):
		self.assertTrue(len(self.deck.getSuits()) == 4)


def main():
	unittest.main()

if __name__ == '__main__':
	main()