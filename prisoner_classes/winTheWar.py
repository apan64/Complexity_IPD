from base_class import Prisoner

class wtw(Prisoner):
    def __init__(self):
        self.history = []
        self.name = 'OppoTaco'
    def makeDecision(self, history):
        if self.history.count('C')/len(self.history) < 0.5:
            return 'C'

        if history.count('D')/len(history) > 0.75 or (len(history) > 5 and history[-5:].count('D')/5  > 0.8):
            return 'C'
        elif history.count('C')/len(history) > 0.75 or (len(history) > 5 and history[-5:].count('C')/5  > 0.8):
            return 'D'

        if self.history[-1] = 'C':
            return 'D'
        else:
            return 'C'
