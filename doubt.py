import numpy as np
from abc import ABCMeta, abstractmethod
import numpy as np


class DoubtStrategy(object):
	__metaclass__ = ABCMeta

	def __init__(self,Number,Call,DiscardCount):
		self.Number = Number
		self.Call = Call
		self.DiscardCount = DiscardCount
		self.Doubt = False

	@abstractmethod
	def doubt_check(self):
		raise NotImplementedError()

class BasicLogic(DoubtStrategy):
	def __init__(self,Number,Call,DiscardCount):
		super().__init__(Number,Call,DiscardCount)

	def doubt_check(self):
		DoubtIndex = (np.random.rand() * 0.1 + 0.9) * ((Call - 700 / 300) ** 2)
		if DoubtIndex > 0.8:
			self.Doubt = True

		return self.Doubt

