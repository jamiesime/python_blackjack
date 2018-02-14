import unittest
from player import Player

class PlayerTests(unittest.TestCase):

	def setUp(self):
		self.player = Player("Bramble", [])

	def testName(self):
		self.assertTrue(self.player.getName() == "Bramble")

	def testCards(self):
		self.assertTrue(len(self.player.getCards()) == 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()