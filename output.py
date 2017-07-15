import numpy as np
# from fabfib import Game

class Output(object):
    def __init__(self,Game):
        self.Game = Game

    def every_turn(self):
        print("Hand")
        print(self.Game.evaluate_hand())
        print("Call")
        print(self.Game.CurrentNumber)
