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
	'''
	Players on BasicLogic strategy discard ...

	less then 6, because a high possibility to draw any of 5-9.
	If the difference of Max and Min is less then 4, other then nine.
	To raise the posibility of 9.
	'''
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
	'''
	Players on this strategy discard other nine of hand.
	I can evaluate this strategy as aggressive.
	'''
	def __init__(self,Hand):
		super().__init__(Hand)

	def discard_check(self):
		self.Discard = np.append(self.Discard,self.Hand[self.Hand != 9])
		return self.Discard

class NoChange(DiscardStrategy):
	'''
	This strategy discard nothing.
	I can evaluate this strategy as Tricky.
	'''
	def __init__(self,Hand):
		super().__init__(Hand)

	def discard_check(self):
		return self.Discard
