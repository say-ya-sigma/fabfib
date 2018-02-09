import numpy as np
import discard as dc
import call as cl
import output as op

class Game(object):
	def __init__(self):## constructor
		'''
		Cards contain state of game.
		Because Cards express where all card is.
		In fabfib, the number of cards is 50(10 x5).
		The number of each number is 5.
		The number of numbers is 10(0-9).
		'''
		self.Cards = np.empty((0,3),int)
		for i in range(10):
			self.Cards = np.append(self.Cards, np.array([[5,0,0]]),axis=0)## Deck Hand Trash

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
		Draw 3 cards and evaluate hand
		'''
		self.draw(3)
		self.first_turn()

	def first_turn(self):
		self.call(self.evaluate_hand())

	def get_cards(self):
		return self.Cards

	def show_cards(self):
		op.Output.gpprint(self.Cards)

	def get_turn(self):
		return self.Turn

	def draw(self,Cards):
		for i in range(Cards):
			if(self.Cards.sum(axis=0)[1] < 3):
				Weight = np.array([])#dtype's default is float64
				DeckTotal = self.Cards.sum(axis=0)[0]
				for i in range(10):
					Weight = np.append(Weight, self.Cards[i][0]/DeckTotal)
				Drawn = int(np.random.choice(10,1,p=Weight))## (a,size,weight)
				self.Cards[Drawn,0] -= 1
				self.Cards[Drawn,1] += 1
			else:
				print('can\'t draw')

	def evaluate_hand(self):
		Hand = self.Cards[0:10,1]
		Number = ""
		for i in range(9,-1,-1):
			for j in range(Hand[i]):
				Number += str(i)
		return int(Number)

	def get_hand(self):
		Hand = self.Cards[0:10,1]
		Number = np.array([],int)
		for i in range(9,-1,-1):
			for j in range(Hand[i]):
				Number = np.append(Number, np.array(i))
		return Number

	def discard(self,Discard):
		if(self.Cards[Discard,1]>0):
			self.Cards[Discard,1] -= 1
			self.Cards[Discard,2] += 1
		else:
			print('can\'t discard')

	def call(self,Call):
		if (Call > self.get_current_number() and Call <=1000 and int(str(Call)[0]) >= int(str(Call)[1]) >= int(str(Call)[2])):
			self.HistoryOfNumber.append(Call)
		else:
			print('invaild call')

		self.Turn += 1

	def get_history_of_number(self,GoBack):
		Temp = self.HistoryOfNumber.copy()
		HistoryGoingBack = []
		for i in range(0,GoBack):
			HistoryGoingBack.append(Temp.pop())
		return HistoryGoingBack
			
	def get_current_number(self):
		if len(self.HistoryOfNumber)>=1:
			Temp = self.HistoryOfNumber.copy()
			return Temp.pop()
		else:
			return 0


class Player(object):
	def __init__(self,Game,Personality):
		self.PartGame = Game
		self.Behavior = np.array(Personality)
		self.DiscardCount = int()
		self.Hand = np.array([],int)

	def discard(self,Discard):
		for i in Discard:
			self.PartGame.discard(i)
			self.DiscardCount += 1
		self.Hand = np.array(self.PartGame.get_hand())


	def turn(self):

		'''
		TODO
		The logic of discard based on personality.
		For now I set the standerd logic as placeholder.
		'''
		## init.
		self.Hand = np.array(self.PartGame.get_hand())
		self.DiscardCount = 0

		## Discard
		self.discard(dc.BasicLogic(self.Hand).discard_check())
		op.Output.gpprint(self.DiscardCount)

		## Draw
		self.PartGame.draw(self.DiscardCount)

		## Call
		self.Hand = np.array(self.PartGame.get_hand())
		self.PartGame.call(cl.BasicLogic(self.PartGame.get_current_number(),self.DiscardCount,self.Hand).call_check())

		## Doubt?
		if self.PartGame.get_current_number() != self.PartGame.evaluate_hand():
			self.PartGame.TurnsOfDoubt.append(self.PartGame.get_turn())
