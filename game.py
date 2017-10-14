import time
import fabfib as ff
import output as op
import sys

GAMES = int(sys.argv[1])

if __name__ == '__main__':
	CurrentTime = time.time()

	for games in range(GAMES):
		print("Game")
		print(games)
		Game = ff.Game()
		Player1 = ff.Player(Game,[])
		Player2 = ff.Player(Game,[])
		PlayerList = [Player1,Player2]
		Output = op.Output(Game)
		print("First Hand")
		print(Game.evaluate_hand())

		while Game.get_current_number() != 999:
			for Player in PlayerList:
				Player.turn()
				Output.every_turn()
				if Game.get_current_number() >=  999:
					break

		print(Game.HistoryOfNumber)
		print(Game.TurnsOfDoubt)
		SumTurns += Game.get_turn()

	print('time: ' + str(time.time() - CurrentTime))
