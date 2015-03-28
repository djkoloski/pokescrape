PkType = {
	'none': 0,
	'normal': 1,
	'fighting': 2,
	'flying': 3,
	'poison': 4,
	'ground': 5,
	'rock': 6,
	'bug': 7,
	'ghost': 8,
	'steel': 9,
	'fire': 10,
	'water': 11,
	'grass': 12,
	'electric': 13,
	'psychic': 14,
	'ice': 15,
	'dragon': 16,
	'dark': 17,
	'fairy': 18
}
PkIType = {
	0: 'none',
	1: 'normal',
	2: 'fighting',
	3: 'flying',
	4: 'poison',
	5: 'ground',
	6: 'rock',
	7: 'bug',
	8: 'ghost',
	9: 'steel',
	10: 'fire',
	11: 'water',
	12: 'grass',
	13: 'electric',
	14: 'psychic',
	15: 'ice',
	16: 'dragon',
	17: 'dark',
	18: 'fairy'
}

PkGender = {
	'0:0': 255,
	'0:1': 254,
	'1:7': 223,
	'1:3': 191,
	'1:1': 127,
	'3:1': 63,
	'7:1': 31,
	'1:0': 0
}
PkIGender = {
	255: '0:0',
	254: '0:1',
	223: '1:7',
	191: '1:3',
	127: '1:1',
	63: '3:1',
	31: '7:1',
	0: '1:0'
}

PkEggGroup = {
	'none': 0,
	'monster': 1,
	'water1': 2,
	'bug': 3,
	'flying': 4,
	'field': 5,
	'fairy': 6,
	'grass': 7,
	'humanlike': 8,
	'water3': 9,
	'mineral': 10,
	'amorphous': 11,
	'water2': 12,
	'ditto': 13,
	'dragon': 14,
	'undiscovered': 15
}
PkIEggGroup = {
	0: 'none',
	1: 'monster',
	2: 'water1',
	3: 'bug',
	4: 'flying',
	5: 'field',
	6: 'fairy',
	7: 'grass',
	8: 'humanlike',
	9: 'water3',
	10: 'mineral',
	11: 'amorphous',
	12: 'water2',
	13: 'ditto',
	14: 'dragon',
	15: 'undiscovered'
}

PkExpGroup = {
	'none': 0,
	'slow': 1,
	'mediumfast': 2,
	'fast': 3,
	'mediumslow': 4,
	'erratic': 5,
	'fluctuating': 6
}
PkIExpGroup = {
	0: 'none',
	1: 'slow',
	2: 'mediumfast',
	3: 'fast',
	4: 'mediumslow',
	5: 'erratic',
	6: 'fluctuating'
}

PkColor = {
	'none': 0,
	'black': 1,
	'blue': 2,
	'brown': 3,
	'gray': 4,
	'green': 5,
	'pink': 6,
	'purple': 7,
	'red': 8,
	'white': 9,
	'yellow': 10
}
PkIColor = {
	0: 'none',
	1: 'black',
	2: 'blue',
	3: 'brown',
	4: 'gray',
	5: 'green',
	6: 'pink',
	7: 'purple',
	8: 'red',
	9: 'white',
	10: 'yellow'
}

class Pokemon:
	def __init__(self):
		self.national_dex_number = 0
		self.name = None
		self.species = None
		self.types = (0, 0)
		self.abilities = (None, None, None)
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
		self.pokedex_x = None
		self.pokedex_y = None
		self.pokedex_or = None
		self.pokedex_as = None
		self.learnset_level_xy = []
		self.learnset_level_oras = []
		self.learnset_machine = []
		self.learnset_egg_move = []
		self.learnset_tutor = []
		self.learnset_special = []
		self.learnset_evolve = []
		self.learnset_transfer = []
		self.evolve_from = []
		self.evolve_into = []
	
	def __str__(self):
		return ('Dex #: %i' % self.national_dex_number +
			'\nName: %s' % self.name +
			'\nSpecies: %s' % self.species +
			'\nTypes: %i/%i (%s/%s)' % (self.types[0], self.types[1], PkIType[self.types[0]], PkIType[self.types[1]]) +
			'\nAbilities: %s/%s/%s' % self.abilities +
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

