import unittest
from game import Game


class TestGame(unittest.TestCase):

	def setUp(self):
		self.game = Game([], [])

	def testHasFullDeck(self):
		self.game.newDeck()
		self.assertTrue(len(self.game.deck.wholeDeck) == 52)


def main():
	unittest.main()

if __name__ == "__main__":
	main()