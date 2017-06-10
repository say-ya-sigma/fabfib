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
			CalledHand = np.array([int(i) for i in list(str(self.Number))])
			for i in range(2, 2-self.DiscardCount, -1):
				CalledHand[i] += 1
				CalledHand[i] += np.random.poisson(lam=0.2)
				if CalledHand[i] > 9:
					CalledHand[i] = 9
			return super().evaluate_hand(np.sort(CalledHand)[::-1])

		else:
			return EvaluatedValue
		
