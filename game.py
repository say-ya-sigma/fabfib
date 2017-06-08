import fabfib as ff

GAMES = 10

if __name__ == '__main__':

	SumTurns = 0
	for games in range(GAMES):
		print("Game")
		print(games)
		Game = ff.Game()
		Player = ff.Player(Game,[])

		while Game.evaluate_hand() !=  999:
			Player.turn()
			print(Game.evaluate_hand())

		SumTurns += Game.get_turn()

	print(SumTurns/GAMES)
