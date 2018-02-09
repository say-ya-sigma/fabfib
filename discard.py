import numpy as np
from abc import ABCMeta, abstractmethod

class DiscardStrategy(object):
	__metaclass__ = ABCMeta

	def __init__(self,Hand):
		self.Hand = Hand
		self.Discard = np.array([],int)

	@abstractmethod
	def discard_check(self):
		raise NotImplementedError()


class BasicLogic(DiscardStrategy):
	def __init__(self,Hand):
		super().__init__(Hand)
		self.Max = np.max(Hand)
		self.Min = np.min(Hand)

	def discard_check(self):
		self.less_then(6)
		if((self.Max - self.Min) < 4):
			self.less_then(9)
		return self.Discard

	def less_then(self,Number):
		self.Discard = np.append(self.Discard,self.Hand[self.Hand < Number])
		self.Hand = self.Hand[self.Hand >= Number]

class OtherNine(DiscardStrategy):
	def __init__(self,Hand):
		super().__init__(Hand)

	def discard_check(self):
		self.Discard = np.append(self.Discard,self.Hand[self.Hand != 9])
		return self.Discard

class NoChange(DiscardStrategy):
	def __init__(self,Hand):
		super().__init__(Hand)

	def discard_check(self):
		return self.Discard
