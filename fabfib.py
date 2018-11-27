import numpy as np
import discard as dc
import call as cl
import output as op
import doubt as db

import random


class Game(object):
    def __init__(self):
        '''
        Cards contain state of game.
        Because Cards express where all card is.
        In fabfib, the number of cards is 50(10 x5).
        The number of each number is 5.
        The number of numbers is 10(0-9).
        '''
        self.Cards = np.empty((0, 3), int)
        for i in range(10):
            self.Cards = np.append(self.Cards, np.array(
                [[5, 0, 0]]), axis=0)  # Deck Hand Trash

        '''
        Mostly, not to think about damage at Discard or Call.
        It is only calculated at the time of Doubt.
        '''
        self.Damages = []
        for i in range(10):
            DamageArray = random.sample([1, 1, 1, 2, 3], 5)
            self.Damages.append(DamageArray)

        '''
        CurrentDamage is list of tuple.
        [(Number, Damage), ... ]
        '''
        self.CurrentDamage = []

        '''
        When calling, a Player needs history of number.
        History of number is History of calls.
        Players can access to these infomation.
        '''
        self.HistoryOfNumber = []
        self.Turn = 0

        '''
        Turns of doubt for analytics.
        '''
        self.TurnsOfDoubt = []

        '''
        Discard Count and History
        '''
        self.HistoryOfDiscardCount = []
        self.DiscardCount = 0

        '''
        Draw 3 cards
        '''
        self.draw(3)

    def get_cards(self):
        """get_all cards state
        >>> Game = Game()
        >>> AllCards = Game.get_cards()
        >>> print(len(AllCards))
        10
        >>> print([len(NumState) for NumState in AllCards])
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        >>> print(sum([len(NumState) for NumState in AllCards]))
        30
        """
        return self.Cards

    def show_cards(self):
        op.Output.gpprint(self.Cards)

    def get_turn(self):
        """get current turn start with 0.
        >>> Game = Game()
        >>> Game.get_turn()
        0
        """
        return self.Turn

    def draw(self, Cards):
        """Max is 3.
        >>> Game = Game()
        >>> Game.draw(1)
        can't draw
        """
        for i in range(Cards):
            if(self.Cards.sum(axis=0)[1] < 3):
                Weight = np.array([])  # dtype's default is float64
                DeckTotal = self.Cards.sum(axis=0)[0]
                for i in range(10):
                    Weight = np.append(Weight, self.Cards[i][0]/DeckTotal)
                # (a,size,weight)
                Drawn = int(np.random.choice(10, 1, p=Weight))

                Damage = self.Damages[Drawn].pop()

                self.Cards[Drawn, 0] -= 1
                self.Cards[Drawn, 1] += 1
                self.CurrentDamage.append((Drawn, Damage))
            else:
                print('can\'t draw')

    def evaluate_hand(self):
        """evaluate hand from Cards
        >>> Game = Game()
        >>> Value = Game.evaluate_hand()
        >>> type(Value)
        <class 'int'>
        >>> print(0 <= Value <=999)
        True
        """
        Hand = self.Cards[0:10, 1]
        Number = ""
        for i in range(9, -1, -1):
            for j in range(Hand[i]):
                Number += str(i)
        return int(Number)

    def get_hand(self):
        """get hand as numpy.array
        >>> Game = Game()
        >>> Hand = Game.get_hand()
        >>> type(Hand)
        <class 'numpy.ndarray'>
        >>> len(Hand)
        3
        """
        Hand = self.Cards[0:10, 1]
        Number = np.array([], int)
        for i in range(9, -1, -1):
            for j in range(Hand[i]):
                Number = np.append(Number, np.array(i))
        return Number

    def discard(self, Discard):
        if(self.Cards[Discard, 1] > 0):
            self.Cards[Discard, 1] -= 1
            self.Cards[Discard, 2] += 1
            self.DiscardCount += 1
        else:
            print('can\'t discard')

    def call(self, Call):
        CallIsHigher = Call > self.get_current_number()
        DigitList = list(map(int, str(Call)))
        CallIsDesc = DigitList[0] >= DigitList[1] >= DigitList[2]
        if (CallIsHigher and Call <= 1000 and CallIsDesc):
            self.HistoryOfNumber.append(Call)
        else:
            print('invaild call')

        self.HistoryOfDiscardCount.append(self.DiscardCount)
        self.DiscardCount = 0
        self.Turn += 1

    def get_history_of_number(self, GoBack):
        Temp = self.HistoryOfNumber.copy()
        HistoryGoingBack = []
        for i in range(0, GoBack):
            HistoryGoingBack.append(Temp.pop())
        return HistoryGoingBack

    def get_current_number(self):
        if len(self.HistoryOfNumber) >= 1:
            Temp = self.HistoryOfNumber.copy()
            return Temp.pop()
        else:
            return 0

    def get_history_of_discard_count(self, GoBack):
        Temp = self.HistoryOfDiscardCount.copy()
        HistoryGoingBack = []
        for i in range(0, GoBack):
            HistoryGoingBack.append(Temp.pop())
        return HistoryGoingBack

    def get_last_discard_count(self):
        if len(self.HistoryOfDiscardCount) > 1:
            Temp = self.HistoryOfDiscardCount.copy()
            return Temp.pop()
        else:
            return 0


class Player(object):
    def __init__(self, Game, Personality):
        self.PartGame = Game
        self.Behavior = np.array(Personality)
        self.Hand = np.array([], int)
        self.RaiseDoubt = False

    def discard(self, Discard):
        for i in Discard:
            self.PartGame.discard(i)
        self.Hand = np.array(self.PartGame.get_hand())

    def turn(self):
        '''
        TODO
        The logic of discard based on personality.
        For now I set the standerd logic as placeholder.
        '''
        # init.
        self.Hand = np.array(self.PartGame.get_hand())
        self.RaiseDoubt = False

        if self.PartGame.Turn != 0:

            # doubt check
            if db.BasicLogic(self.PartGame.get_current_number(),
                             self.PartGame.get_last_discard_count()) \
                    .doubt_check():
                self.RaiseDoubt = True
                return self.RaiseDoubt

            # Discard
            self.discard(dc.BasicLogic(self.Hand).discard_check())

        op.Output.gpprint(self.PartGame.DiscardCount)

        # Draw
        self.PartGame.draw(self.PartGame.DiscardCount)

        # Call
        self.Hand = np.array(self.PartGame.get_hand())
        self.PartGame.call(cl.BasicLogic(self.PartGame.get_current_number(
        ), self.PartGame.DiscardCount, self.Hand).call_check())

        # Doubt?
        if self.PartGame.get_current_number() != self.PartGame.evaluate_hand():
            self.PartGame.TurnsOfDoubt.append(self.PartGame.get_turn())
        return self.RaiseDoubt


if __name__ == '__main__':
    import doctest
    doctest.testmod()
