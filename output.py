class Output(object):
    def __init__(self, Game):
        self.Game = Game

    def every_turn(self):
        print("Hand")
        print(self.Game.evaluate_hand())
        print("Call")
        print(self.Game.get_current_number())

    def gpprint(String):
        print(String)
