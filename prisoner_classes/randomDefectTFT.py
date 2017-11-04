from base_class import Prisoner
import random

# Make sure to use Python 3 syntax since I built the tournament system in 3
class RandomDefectTFT(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.history = []
        self.name = 'RandomDefectTFT'

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games

        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if len(history) == 0:
            return 'C'
        if random.random() < 0.01:
            return 'D'
        return history[-1]
