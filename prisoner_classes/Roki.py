from base_class import Prisoner
from random import random

class Roki(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Roki'
        
    def makeDecision(self, history):
        if (len(history) < 6):
            return 'C'
        isDefactor = history.count('D') >= 2 * history.count('C')
        if isDefactor:
        	return 'D'
        cooperation = 0.6
        if random() < cooperation:
        	return 'C'
        return 'D'
