from base_class import Prisoner
import numpy as np

class SandwichPrisoner(Prisoner):
    def __init___(self):
        Prisoner.__init__(self)
        self.name = 'Idiot Sandwich Prisoner'
    def makeDecision(self, history, p=0.05):
        if len(history) == 0 or np.random.uniform(0,1) < p:
            return 'C'
        return history[-1]
