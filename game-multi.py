import fabfib as ff
import output as op
import multiprocessing as multi
import time
import sys


def playing(self):

    print("Game start")
    Game = ff.Game()
    Player1 = ff.Player(Game, [])
    Player2 = ff.Player(Game, [])
    PlayerList = [Player1, Player2]
    Output = op.Output(Game)
    print("First Hand")
    print(Game.evaluate_hand())

    while Game.get_current_number() != 999:
        for Player in PlayerList:
            Player.turn()
            Output.every_turn()
            if Game.get_current_number() >= 999:
                break

    print(Game.HistoryOfNumber)
    print(Game.TurnsOfDoubt)


if __name__ == '__main__':
    CurrentTime = time.time()

    ProcPool = multi.Pool(multi.cpu_count())
    ProcPool.map(playing, list(range(int(sys.argv[1]))))
    ProcPool.close()

    print('time: ' + str(time.time() - CurrentTime))
