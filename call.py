import numpy as np
from abc import ABCMeta, abstractmethod

class CallStrategy(object):
	__metaclass__ = ABCMeta

	def __init__(self,Number,DiscardCount,Hand):
		self.Hand = Hand
		self.Number = Number
		self.DiscardCount = DiscardCount

	def evaluate_hand(self,Hand):
		Number = ""
		for i in range(3):
			Number += str(Hand[i])
		return int(Number)

	@abstractmethod
	def call_check(self):
		raise NotImplementedError()

class BasicLogic(CallStrategy):
	def __init__(self,Number,DiscardCount,Hand):
		super().__init__(Number,DiscardCount,Hand)

	def call_check(self):
		EvaluatedValue = super().evaluate_hand(self.Hand)

		if self.Number >= EvaluatedValue:
			ToCall = np.array([int(i) for i in list(str(self.Number))])
			ToCall = np.sort(ToCall) #ascending order
			NonNines = 3 - len(np.where(ToCall == 9)[0])
			IncreaseFrom = min(self.DiscardCount,NonNines) -1

			for i in range(0,IncreaseFrom):
				ToCall[i] = np.random.poisson(lam=4)
				if ToCall[i] > 9:
					ToCall[i] = 9
			
			ToCall[IncreaseFrom] += 1
			ToCall[IncreaseFrom] += np.random.poisson(lam=0.2)
			if ToCall[IncreaseFrom] > 9:
				ToCall[IncreaseFrom] = 9
					
			
			return super().evaluate_hand(np.sort(ToCall)[::-1])

		else:
			return EvaluatedValue
		
