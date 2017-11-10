from base_class import Prisoner
import numpy as np

class MostBestUnderling(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'MostBestUnderling'
        self.bossHandshake = ['C', 'D', 'C', 'C']
        self.underlingHandshake = ['C', 'C', 'C', 'D', 'C', 'C']
        self.strategy = "test_boss"
        self.p = 0.05

    def makeDecision(self, opponent_history):
        # If opponent is not boss, probe for tft
        if len(opponent_history) == 2:
            if opponent_history != ['C', 'D']:
                self.strategy = "probe_tft"
                return 'D'

        if (len(opponent_history) == 3 and self.strategy == "probe_tft"):
            return 'C'

        # Test if tft has responded
        if (len(opponent_history) == 4 and self.strategy == "probe_tft"):
            if opponent_history[-1] == 'D':
                self.strategy = "tft"
                return 'C'
            else:
                self.strategy = "average"

        # Test for the boss
        if opponent_history == self.bossHandshake:
            self.strategy = "boss"

        # Do the secret handshake if testing for boss
        if (len(opponent_history) < len(self.underlingHandshake) and self.strategy == "test_boss"):
            return self.underlingHandshake[len(opponent_history)]


        # If the strategy is set, do it
        if self.strategy == "boss":
            return 'C'

        if self.strategy == "tft":
            if np.random.uniform(0,1) < self.p:
                return 'C'
            return opponent_history[-1]

        if self.strategy == "average":
            if ((len(opponent_history) - 1) % 4 < 2):
                return 'C'
            return 'D'

        # If all else fails, cooperate
        return 'C'
