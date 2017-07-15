import fabfib as ff
import output as op


GAMES = 10

if __name__ == '__main__':

	SumTurns = 0
	for games in range(GAMES):
		print("Game")
		print(games)
		Game = ff.Game()
		Player1 = ff.Player(Game,[])
		Player2 = ff.Player(Game,[])
		PlayerList = [Player1,Player2]
		Output = op.Output(Game)

		while Game.CurrentNumber != 999:
			for Player in PlayerList:
				Player.turn()
				Output.every_turn()
				if Game.CurrentNumber >=  999:
					break

		SumTurns += Game.get_turn()

	print(SumTurns/GAMES)
