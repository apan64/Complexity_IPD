from base_class import Prisoner


class VickyPrisoner(Prisoner):
    def __init__(self):
        self.history = []
        self.name = 'VickyPrisoner'

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
        # if they have ever defected then we will defect too
        if 'D' in history:
            return 'D'
        # if they have never defected then we will cooperate
        else:
            return 'C'

    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision
