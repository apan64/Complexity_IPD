from base_class import Prisoner
import numpy as np


class UnderlingTFT(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Underling'
        self.handshake = ['C', 'C', 'D', 'C']
        self.onlyDefect = ['D', 'D', 'D', 'D', 'D']
        self.p = 0.05

    def makeDecision(self, opponent_history):
        if len(opponent_history) >= 4:
            if opponent_history[:4] == self.handshake
                return 'C'

        if len(opponent_history) == 0 or np.random.uniform(0,1) < self.p:
            return 'C'
        return opponent_history[-1]

class ImprovedUnderlingTFT(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'ImprovedUnderling'
        self.handshake = ['C', 'C', 'D', 'C']
        self.onlyDefect = ['D', 'D', 'D', 'D', 'D']
        self.p = 0.05

    def makeDecision(self, opponent_history):
        if len(opponent_history) == 0:
            return 'C'

        if len(opponent_history) >= 4:
            if opponent_history[:4] == self.handshake
                return 'C'

        if len(opponent_history) <= 5:
            if opponent_history[:5].count('D') == len(opponent_history)
                return 'C'

        if np.random.uniform(0,1) < self.p:
            return 'C'
        return opponent_history[-1]
