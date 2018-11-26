import time
import fabfib as ff
import output as op
import sys

GAMES = int(sys.argv[1])


def PlayingGame(Game, PlayerList, Output):
    while Game.get_current_number() != 999:
        for Player in PlayerList:
            if Player.turn():
                print("Doubt")
                return
            Output.every_turn()
            if Game.get_current_number() >= 999:
                break


if __name__ == '__main__':
    CurrentTime = time.time()

    for games in range(GAMES):
        print("Game")
        print(games)
        Game = ff.Game()
        Player1 = ff.Player(Game, [])
        Player2 = ff.Player(Game, [])
        PlayerList = [Player1, Player2]
        Output = op.Output(Game)
        print("First Hand")
        print(Game.evaluate_hand())

        PlayingGame(Game, PlayerList, Output)

        print(Game.HistoryOfNumber)
        print(Game.TurnsOfDoubt)

    print('time: ' + str(time.time() - CurrentTime))
