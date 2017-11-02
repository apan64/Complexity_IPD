# Create a class that extends this one
# Make sure to use Python 3 syntax since I built the tournament system in 3
class Prisoner:
    def __init__(self):
        self.history = []
        # TODO: Give your class a name for me to refer to it by
        self.name = 'Kaitlyn'
        
    def getHistory(self):
        return self.history
    
    def addToHistory(self, decision):
        self.history.append(decision)
        return
    
    def makeDecision(self, history):
        '''
        Kaitlyn tries to cooperate unless it seems likely that the onther one is going to defect (pattern,
        more defects than not, chain of defects).
        
        Input: List containing the history of the opposing agent's decisions throughout previous games
        
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if history[-3:] == ['C', 'D', 'C'] or history[-3:] == ['D', 'D', 'D']:
        	return 'D'
        elif history[-3:] == ['D', 'C', 'D'] or history[-3:] ==  ['C', 'C', 'C']:
        	return 'C'
        elif history.count('D') > history.count('C'):
        	return 'D'
        elif history.count('D') < history.count('C'):
        	return 'C'
        else:
        	return 'C'
    
    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision