import random
import gc
import inspect
import numpy as np

# Create a class that extends this one
# Make sure to use Python 3 syntax since I built the tournament system in 3
class Prisoner:
    def __init__(self):
        self.personal_history = []
        # TODO: Give your class a name for me to refer to it by
        self.name = 'Default'

    def getHistory(self):
        return self.personal_history

    def addToHistory(self, decision):
        self.personal_history.append(decision)
        return

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games

        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        # TODO: Overwrite this function yourself!
        return 'D'
    
    # Note: YOU CANNOT USE THIS IN A TOURNAMENT BECAUSE THE DECISION OF THE SECOND PRISONER IS BASED ON THE DECISON OF THE FIRST ONE!
    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision

class Defector(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Defector'
    def makeDecision(self, history):
        return 'D'

class Cooperator(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Cooperator'
    def makeDecision(self, history):
        return 'C'


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
        return 'C'

    def makeDecision(self, history):
        if (len(history) > 10):
            last10 = history[-9:]
            return self.decideOnPrev(last10, 3)

        elif (len(history) == 0):
            return 'C'

        else:
            return self.decideOnPrev(history, len(history)//2)

class PavlovianTFT(Prisoner):
    """Acheive critical mass of TFT to become dominant"""
    def __init__(self):
        self.personal_history = []
        self.name = 'PavlovianTFT'
        self.d_count = 0

    def makeDecision(self, history):
        if (len(history) == 0):
            return 'C'
        if history[-1] == 'D':
            self.d_count += 1
        if self.d_count > 20:
            return 'D'
        return history[-1]

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
        if random.random() < cooperation:
            return 'C'
        return 'D'

class Average_Joe(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Average_Joe'
    def makeDecision(self,history):
        c = []
        for i in history:
            if i == 'C':
                c.append(i)
        if len(c) >= len(history)/2:
            return 'C'
        else:
            return 'D'

class Bob(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.personal_history = []
        self.name = 'BOB'

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        isOpponentCooperator = history.count('C') >= history.count('D')
        isSelfCooperator = self.personal_history.count('C') >= self.personal_history.count('D')
        if(isSelfCooperator and isOpponentCooperator):
            return 'C'
        elif(history[-1] == 'C'):
            return 'D'
        elif(history[-1] == 'D'):
            return 'C'
        return 'D'

class ElepertPrisoner(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.personal_history = []
        # TODO: Give your class a name for me to refer to it by
        self.name = 'EmilyLPrisoner'

    def makeDecision(self,history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if history == []:
            return 'D'
        elif history[-1] == 'C':
            return 'C'
        elif history[-1] == 'D':
            return 'D'

    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision

class Kaitlyn(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Kaitlyn'
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

class SandwichPrisoner(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Idiot Sandwich Prisoner'
    def makeDecision(self, history, p=0.05):
        if len(history) == 0 or np.random.uniform(0,1) < p:
            return 'C'
        return history[-1]

class SmoothCriminal2AkaPrettyPrincess(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Smooth Criminal 2 AKA Pretty Princess'

    def makeDecision(self, history):
        c_count = 0;
        d_count = 0;

        for decision in history:
            if decision == "C":
                c_count += 1
            elif decision == "D":
                d_count += 1

        # No matter what, defecting is the only sure way to gain points per round
        # But if both prisoners cooperate, there is a much larger reward
        # So if the other prisoner has a history of cooperating much more than defecting,
        # Pretty Princess will cooperate too
        # Otherwise, Pretty Princess will defect

        if c_count > d_count * 2:
            return "C"
        else:
            return "D"

class Snail(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Snail'

    def makeDecision(self, history):
        lag = 5
        if len(history) > lag:
            return 'C' if history[-lag] == 'C' else 'D'
        return 'D'

class TigerMountainPrisoner(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Wolpertinger'
        
    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if (len(history) == 0):
            return 'C'
        elif history[-1] is 'C':
            return 'C'
        else:
            cs = history.count('C')
            ds = history.count('D')
            if cs > ds*2:
                return 'C'
            return 'D'

class VickyPrisoner(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.personal_history = []
        self.name = 'VickyPrisoner'

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games

        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        # if they defect more than they cooperate then we should defect too
        if 'D' in history:
            if history.count('D') > history.count('C'):
                return 'D'
            # if they have reason to be believe we are a defector then we should defect
            elif self.personal_history.count('D') > self.personal_history.count('C'):
                return 'D'
            # otherwise let us cooperate
            else:
                return 'C'
        # if they have never defected then we will cooperate
        else:
            return 'C'

    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision

class wtw(Prisoner):
    def __init__(self):
        self.personal_history = []
        self.name = 'OppoTaco'
    def makeDecision(self, history):
        if not len(self.personal_history) or self.personal_history.count('C')/len(self.personal_history) < 0.5:
            return 'C'

        if history.count('D')/len(history) > 0.75 or (len(history) > 5 and history[-5:].count('D')/5  > 0.8):
            return 'C'
        elif history.count('C')/len(history) > 0.75 or (len(history) > 5 and history[-5:].count('C')/5  > 0.8):
            return 'D'

        if self.personal_history[-1] == 'C':
            return 'D'
        else:
            return 'C'

class NotAMobster(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.name = 'Tony'
        self.handshake = ['C', 'D', 'C', 'C']
        self.underling_handshake = ['C', 'C', 'C', 'D']
        self.is_underling = True
        self.quotes = [
            "I'm gonna make him an offer he can't refuse.",
            "A friend should always underestimate your virtues and an enemy overestimate your faults.",
            "You talk about vengeance. Is vengeance going to bring your son back to you? Or my boy to me?",
            "Revenge is a dish best served cold."
        ]

    def generousTitForTat(self, history):
        if len(history) == 0 or random.random() < 0.33:
            return 'C'
        else:
            return history[-1]

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games

        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        roundNum = len(history) + 1
        if self.is_underling:
            if len(history) <= len(self.underling_handshake):  # check for deviations from fingerprint
                if history != self.underling_handshake[:len(history)]:
                    self.is_underling = False
                    return self.generousTitForTat(history)

            if roundNum <= len(self.handshake):  # make a name for youself
                return self.handshake[roundNum - 1]

            # gdi evan
            # if random.random() < 0.01:  # make a statement
            #     print(random.choice(self.quotes))

            return 'D'  # deny once it's (presumably) the underling

        else:  # play generous tit for tat
            return self.generousTitForTat(history)

class RandomDefectTFT(Prisoner):
    def __init__(self):
        Prisoner.__init__(self)
        self.personal_history = []
        self.name = 'RandomDefectTFT'

    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        if len(history) == 0:
            return 'C'
        if random.random() < 0.01:
            return 'D'
        return history[-1]

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