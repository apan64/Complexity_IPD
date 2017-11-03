# Create a class that extends this one
import random
# Make sure to use Python 3 syntax since I built the tournament system in 3
class Prisoner:
    def __init__(self):
        self.history = []
        self.name = 'RandomDefectTFT'

    def getHistory(self):
        return self.history

    def addToHistory(self, decision):
        self.history.append(decision)
        return

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games

        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if random.radnom() < 0.01:
            return 'D'
        return history[-1]

    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision
