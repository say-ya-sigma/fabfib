import numpy as np
from abc import ABCMeta, abstractmethod
import numpy as np


class DoubtStrategy(object):
    __metaclass__ = ABCMeta

    def __init__(self,Call,DiscardCount):
        self.Call = Call
        self.DiscardCount = DiscardCount
        self.Doubt = False

    @abstractmethod
    def doubt_check(self):
        raise NotImplementedError()

class BasicLogic(DoubtStrategy):
    def __init__(self,Call,DiscardCount):
        super().__init__(Call,DiscardCount)

    def doubt_check(self):
        DoubtIndex = 0.0
        DoubtIndex += (np.random.rand() * 0.2 + 0.8) * (((self.Call - 700) / 300) ** 3)

        if self.DiscardCount == 2:
            DoubtIndex += 0.1
            if self.Call >=990:
                DoubtIndex += 0.6

        if self.DiscardCount == 3:
            DoubtIndex += 0.3
            if self.Call >=900:
                DoubtIndex += 0.3

        print("DoubtIndex=")
        print(DoubtIndex)
        if DoubtIndex > 0.85:
            self.Doubt = True

        return self.Doubt

