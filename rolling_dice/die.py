from random import randint

# A class representing a simple die.
class Die():
	# Assume a six-sided die.
	def __init__(self, num_sides=6):
		self.num_sides = num_sides
	# Return a random value between 1 and number of sides.
	def roll(self):
		return randint(1, self.num_sides)