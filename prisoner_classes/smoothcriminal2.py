from base_class import Prisoner

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