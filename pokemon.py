from pk import *
from move import *
from ability import *

class Pokemon:
	def __init__(self):
		self.national_dex_number = 0
		self.name = 'None'
		self.species = 'None'
		self.types = (0, 0)
		self.abilities = (0, 0, 0)
		self.gender_threshold = 0
		self.catch_rate = 0
		self.egg_groups = (0, 0)
		self.hatch_counter = 0
		self.height = 0.0
		self.weight = 0.0
		self.base_exp_yield = 0
		self.base_friendship = 0
		self.exp_group = 0
		self.ev_yield = (0, 0, 0, 0, 0, 0)
		self.body_style = 0
		self.color = 0
		self.base_stats = (0, 0, 0, 0, 0, 0)
		self.pokedex_x = 'None'
		self.pokedex_y = 'None'
		self.pokedex_or = 'None'
		self.pokedex_as = 'None'
		self.learnset_level_xy = []
		self.learnset_level_oras = []
		self.learnset_machine = []
		self.learnset_egg_move = []
		self.learnset_tutor = []
		self.learnset_special = []
		self.learnset_evolve = []
		self.learnset_transfer = []
	
	def __str__(self):
		return ('Dex #: %i' % self.national_dex_number +
			'\nName: %s' % self.name +
			'\nSpecies: %s' % self.species +
			'\nTypes: %i/%i (%s/%s)' % (self.types[0], self.types[1], PkIType[self.types[0]], PkIType[self.types[1]]) +
			'\nAbilities: %i/%i/%i (%s/%s/%s)' % (self.abilities[0], self.abilities[1], self.abilities[2], abilities[self.abilities[0]].name, abilities[self.abilities[1]].name, abilities[self.abilities[2]].name) +
			'\nGender Threshold: %i (%s)' % (self.gender_threshold, PkIGender[self.gender_threshold]) +
			'\nCatch Rate: %i' % self.catch_rate +
			'\nEgg Groups: %i/%i (%s/%s)' % (self.egg_groups[0], self.egg_groups[1], PkIEggGroup[self.egg_groups[0]], PkIEggGroup[self.egg_groups[1]]) +
			'\nHatch Counter: %i' % self.hatch_counter +
			'\nHeight: %f' % self.height +
			'\nWeight: %f' % self.weight +
			'\nBase Exp Yield: %i' % self.base_exp_yield +
			'\nBase Friendship: %i' % self.base_friendship +
			'\nExp Group: %i (%s)' % (self.exp_group, PkIExpGroup[self.exp_group]) +
			'\nEV Yield: %i/%i/%i/%i/%i/%i' % self.ev_yield +
			'\nBody Style: %i' % self.body_style +
			'\nColor: %i (%s)' % (self.color, PkIColor[self.color]) +
			'\nBase Stats: %i/%i/%i/%i/%i/%i' % self.base_stats +
			'\nPokedex Entry (X): %s' % self.pokedex_x +
			'\nPokedex Entry (Y): %s' % self.pokedex_y +
			'\nPokedex Entry (OR): %s' % self.pokedex_or +
			'\nPokedex Entry (AS): %s' % self.pokedex_as +
			'\nLearnset (XY): %s' % str(self.learnset_level_xy) +
			'\nLearnset (ORAS): %s' % str(self.learnset_level_oras) +
			'\nLearnset (TM/HM): %s' % str(self.learnset_machine) +
			'\nLearnset (Egg Move): %s' % str(self.learnset_egg_move) +
			'\nLearnset (Tutor): %s' % str(self.learnset_tutor) +
			'\nLearnset (Special): %s' % str(self.learnset_special) +
			'\nLearnset (Pre-evo): %s' % str(self.learnset_evolve) +
			'\nLearnset (Transfer): %s' % str(self.learnset_transfer))

