import numpy as np
from abc import ABCMeta, abstractmethod


class DoubtStrategy(object):
	__metaclass__ = ABCMeta

	def __init__(self,Number,Call,DiscardCount):
		self.Number = Number
		self.Call = Call
		self.DiscardCount = DiscardCount

	@abstractmethod
	def doubt_check(self):
		raise NotImplementedError()

class BasicLogic(DoubtStrategy):
	def __init__(self,Number,Call,DiscardCount):
		super().__init__(Number,Call,DiscardCount)

	def doubt_check(self):
		pass ## todo, doubt_check design is not defined
		

