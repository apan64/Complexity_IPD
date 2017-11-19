import random
from base_class import Prisoner


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

            if random.random() < 0.01:  # make a statement
                print(random.choice(self.quotes))

            return 'D'  # deny once it's (presumably) the underling

        else:  # play generous tit for tat
            return self.generousTitForTat(history)


if __name__ == '__main__':
    tony = NotAMobster()
    for i in range(300):
        print(tony.makeDecision(['C','C','D','C','D']))
