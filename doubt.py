import numpy as np
from abc import ABCMeta, abstractmethod


class DoubtStrategy(object):
	__metaclass__ = ABCMeta

	def __init__(self,Number,Call,DiscardCount):
		self.Hand = Hand
		self.Number = Number
		self.Call = Call
		self.DiscardCount = DiscardCount

	@abstructmethod
	def doubt_check(self):
		raise NotImplementedError()

class BasicLogic(DoubtStrategy):
	def __init__(self,Number,Call,DiscardCount):
		super().__init__(self,Number,Call,DiscardCount)

