from player import Player

class Game:

	def intro():
		print("Welcome to blackjack. Please enter your name.")
		playerName = input()
		player1 = Player(playerName, "none")
		print(player1.getName())
		print("Your deck is currently: " + player1.getCards())




Game.intro()