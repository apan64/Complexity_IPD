from base_class import Prisoner

class PavlovianTFT(Prisoner):
    """Acheive critical mass of TFT to become dominant"""
    def __init__(self):
        self.history = []
        self.name = 'PavlovianTFT'
        self.d_count = 0

    def makeDecision(self, history):
        if (len(history) == 0):
            return 'C'
        if history[-1] == 'D':
            self.d_count += 1
        if self.d_count > 20:
            return 'D'
        return history[-1])
