class Ability:
	def __init__(self):
		self.name = None
		self.description = None
	
	def __str__(self):
		return ('Name: %s' % self.name +
			'\nDescription: %s' % self.description)

abilities = [Ability()]
abilities_map = {}
