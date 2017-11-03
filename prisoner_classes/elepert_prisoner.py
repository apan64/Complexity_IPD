from base_class import Prisoner


class ElepertPrisoner(Prisoner):
	def __init__(self):
		Prisoner.__init__(self)
		self.history = []
		# TODO: Give your class a name for me to refer to it by
		self.name = 'EmilyLPrisoner'

	def getHistory(self):
		return self.history

	def addToHistory(self, decision):
		self.history.append(decision)
		return

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