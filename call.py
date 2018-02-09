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

		## if real hand's value is weak, Calling fake number based on Game's State
		if self.Number >= EvaluatedValue:

			## Leaves to change is based on NonNines Count of Game's Number or DiscardCount.
			ToCall = np.array([int(i) for i in str(self.Number)])
			ToCall = np.sort(ToCall) #ascending order
			NonNines = len(np.where(ToCall != 9)[0])
			LeavesToChange = min(self.DiscardCount,NonNines)

			for i in range(0,LeavesToChange -1):
				ToCall[i] = np.random.poisson(lam=4)
				if ToCall[i] > 9:
					ToCall[i] = 9
			
			ToCall[LeavesToChange -1] += 1
			ToCall[LeavesToChange -1] += np.random.poisson(lam=0.2)
			if ToCall[LeavesToChange -1] > 9:
				ToCall[LeavesToChange -1] = 9
					
			
			return super().evaluate_hand(np.sort(ToCall)[::-1])

		else:
			return EvaluatedValue
		
