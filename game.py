import fabfib as ff

GAMES = 10

if __name__ == '__main__':

	SumTurns = 0
	for games in range(GAMES):
		print("Game")
		print(games)
		Game = ff.Game()
		Player = ff.Player(Game,[])

		while Game.CurrentNumber !=  999:
			Player.turn()
			print("Hand")
			print(Game.evaluate_hand())
			print("Call")
			print(Game.CurrentNumber)

		SumTurns += Game.get_turn()

	print(SumTurns/GAMES)
