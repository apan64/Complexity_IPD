from base_class import Prisoner


class Bob(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.history = []
        self.name = 'BOB'

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        isOpponentCooperator = history.count('C') >= history.count('D')
        isSelfCooperator = self.history.count('C') >= self.history.count('D')
        if(isSelfCooperator and isOpponentCooperator):
            return 'C'
        elif(history[-1] == 'C'):
            return 'D'
        elif(history[-1] == 'D'):
            return 'C'
        return 'D'
