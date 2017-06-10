import numpy as np
import discard as dc
import call as cl

class Game(object):
	def __init__(self):## constructor
		self.Cards = np.empty((0,3),int)
		for i in range(10):
			self.Cards = np.append(self.Cards, np.array([[5,0,0]]),axis=0)## Deck Hand Trash
		self.CurrentNumber = 0
		self.Turn = 1
		self.draw(3)
		print("First Hands")
		print(self.evaluate_hand())

	def get_cards(self):
		return self.Cards

	def show_cards(self):
		print(self.Cards)

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
		if (Call > self.CurrentNumber and Call <=1000 and int(str(Call)[0]) >= int(str(Call)[1]) >= int(str(Call)[2])):
			self.CurrentNumber = Call
		else:
			print('invaild call')

		self.Turn += 1

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
## todo, The logic of discard based on personality. For now I set the standerd logic as placeholder.
		self.Hand = np.array(self.PartGame.get_hand())
		self.DiscardCount = 0
		self.discard(dc.BasicLogic(self.Hand).discard_check())
		print(self.DiscardCount)
		self.PartGame.draw(self.DiscardCount)
		self.Hand = np.array(self.PartGame.get_hand())
		self.PartGame.call(cl.BasicLogic(self.PartGame.CurrentNumber,self.DiscardCount,self.Hand).call_check())

