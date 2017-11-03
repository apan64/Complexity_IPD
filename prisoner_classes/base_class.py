# Create a class that extends this one
# Make sure to use Python 3 syntax since I built the tournament system in 3
class Prisoner:
    def __init__(self):
        self.history = []
        # TODO: Give your class a name for me to refer to it by
        self.name = 'Default'

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
        # TODO: Overwrite this function yourself!
        return 'D'

    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision

class Goldfish(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Goldfish'

    def decideOnPrev(self, myarr, t):
        defect = 0
        for i in myarr:
            if i == 'D':
                defect += 1
                if (defect > t):
                    return 'D'
                else:
                    return 'C'

    def makeDecision(self, history):
        if (len(history) > 10):
            last10 = history[-9:]
            return self.decideOnPrev(last10, 3)

        elif (len(history) == 0):
            return 'C'

        else:
            return self.decideOnPrev(history, len(history)//2)
