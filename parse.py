import os.path
import urllib.request
from html.parser import HTMLParser
from pokemon import *

def GetAndParse(number, force = False):
	path = 'cache/%03i.shtml' % number
	if force == True or os.path.isfile(path) == False:
		url = 'http://www.serebii.net/pokedex-xy/%03i.shtml' % number
		print('Fetching \'%s\' to \'%s\'' % (url, path))
		data = urllib.request.urlopen(url)
		out = open(path, 'wb')
		out.write(data.read().decode('ISO-8859-1').replace('&eacute;', '\u00E9').encode('utf-8'))
		print('Using newly-fetched file \'%s\'' % path)
	else:
		print('Using already-fetched file \'%s\'' % path)
	
	source = open(path, 'r')
	parser = PokemonParser()
	parser.feed(source.read())
	source.close()
	
	print('Done parsing \'%s\'' % path)
	
	return parser.pokemon

class PokemonParser(HTMLParser):
	def __init__(self):
		super().__init__(strict=False, convert_charrefs=True)
		
		self.pokemon = Pokemon()
		
		self.cur_fooinfo = 0
		self.td_cur_level = 0
		self.fooinfo_enter_level = -1
		self.fooinfo_cur_td = 0
		self.cen_enter_level = -1
		self.cen_cur_td = 0
		self.is_bold = False
		self.fooinfo_temp = 0
	
	def handle_starttag(self, tag, attrs):
		if tag == 'td':
			if self.fooinfo_enter_level == -1 and ('class', 'fooinfo') in attrs:
				self.fooinfo_enter_level = self.td_cur_level
			if self.cen_enter_level == -1 and ('class', 'cen') in attrs:
				self.cen_enter_level = self.td_cur_level
			self.td_cur_level += 1
		# Parse types out of links
		if tag == 'a':
			if self.cen_enter_level != -1:
				if self.cur_fooinfo == 5:
					ptype = PkType[attrs[0][1][12:-6]]
					if self.pokemon.types[0] == 0:
						self.pokemon.types = (ptype, 0)
					else:
						self.pokemon.types = (self.pokemon.types[0], ptype)
		self.is_bold = tag == 'b'
	
	def handle_endtag(self, tag):
		if tag == 'td':
			self.td_cur_level -= 1
			if self.fooinfo_enter_level != -1:
				self.fooinfo_cur_td += 1
			if self.fooinfo_enter_level == self.td_cur_level:
				self.cur_fooinfo += 1
				self.fooinfo_enter_level = -1
				self.fooinfo_cur_td = 0
				self.fooinfo_temp = 0
			if self.cen_enter_level != -1:
				self.cen_cur_td += 1
			if self.cen_enter_level == self.td_cur_level:
				self.cen_enter_level = -1
				self.cen_cur_td = 0
	
	def handle_data(self, data):
		if self.fooinfo_enter_level != -1:
			# 'Name'
			if self.cur_fooinfo == 1:
				self.pokemon.name = data
			# 'No.'
			elif self.cur_fooinfo == 3:
				if self.fooinfo_cur_td == 1:
					self.pokemon.national_dex_number = int(data[1:])
			# 'Gender Ratio'
			elif self.cur_fooinfo == 4:
				if 'is Genderless' in data:
					self.pokemon.gender_ratio = PkGender['0:0']
				if self.fooinfo_cur_td == 1:
					if data == '0%':
						self.pokemon.gender_threshold = PkGender['0:1']
					elif data == '12.5%':
						self.pokemon.gender_threshold = PkGender['1:7']
					elif data == '25%':
						self.pokemon.gender_threshold = PkGender['1:3']
					elif data == '50%':
						self.pokemon.gender_threshold = PkGender['1:1']
					elif data == '75%':
						self.pokemon.gender_threshold = PkGender['3:1']
					elif data == '87.5%':
						self.pokemon.gender_threshold = PkGender['7:1']
					elif data == '100%':
						self.pokemon.gender_threshold = PkGender['1:0']
					else:
						print('Failed to parse gender ratio \'%s\'' % data)
			# 'Classification'
			elif self.cur_fooinfo == 5:
				self.pokemon.species = data[:-8]
			# 'Height'
			elif self.cur_fooinfo == 6:
				if 'm' in data:
					self.pokemon.height = float(data.strip()[:-1])
			# 'Weight'
			elif self.cur_fooinfo == 7:
				if 'kg' in data:
					self.pokemon.weight = float(data.strip()[:-2])
			# 'Capture Rate'
			elif self.cur_fooinfo == 8:
				self.pokemon.catch_rate = int(data)
			# 'Base Egg Steps'
			elif self.cur_fooinfo == 9:
				if data != '\xa0':
					self.pokemon.hatch_counter = int(data.replace(',', '')) // 255
			# 'Abilities'
			elif self.cur_fooinfo == 10:
				if self.is_bold:
					if self.fooinfo_temp % 2 == 0:
						if data == 'Hidden Ability':
							self.fooinfo_temp = 4
						else:
							if self.fooinfo_temp == 0:
								self.pokemon.abilities = (data, None, None)
							elif self.fooinfo_temp == 2:
								self.pokemon.abilities = (self.pokemon.abilities[0], data, None)
							elif self.fooinfo_temp == 6:
								self.pokemon.abilities = (self.pokemon.abilities[0], self.pokemon.abilities[1], data)
					self.fooinfo_temp += 1
			# 'Experience Growth'
			elif self.cur_fooinfo == 11:
				if not 'Points' in data:
					if data == 'Slow':
						self.pokemon.exp_group = PkExpGroup['slow']
					elif data == 'Medium Slow':
						self.pokemon.exp_group = PkExpGroup['mediumslow']
					elif data == 'Medium Fast':
						self.pokemon.exp_group = PkExpGroup['mediumfast']
					elif data == 'Fast':
						self.pokemon.exp_group = PkExpGroup['fast']
					elif data == 'Erratic':
						self.pokemon.exp_group = PkExpGroup['erratic']
					elif data == 'Fluctuating':
						self.pokemon.exp_group = PkExpGroup['fluctuating']
					else:
						print('Failed to parse experience group \'%s\'' % data)
			# 'Base Happiness'
			elif self.cur_fooinfo == 12:
				self.pokemon.base_friendship = int(data)
			# 'Effort Values Earned'
			elif self.cur_fooinfo == 13:
				n = int(data[:1])
				y = self.pokemon.ev_yield
				if 'HP' in data:
					self.pokemon.ev_yield = (n, y[1], y[2], y[3], y[4], y[5])
				elif 'Sp. Attack' in data:
					self.pokemon.ev_yield = (y[0], y[1], y[2], n, y[4], y[5])
				elif 'Sp. Defense' in data:
					self.pokemon.ev_yield = (y[0], y[1], y[2], y[3], n, y[5])
				elif 'Attack' in data:
					self.pokemon.ev_yield = (y[0], n, y[2], y[3], y[4], y[5])
				elif 'Defense' in data:
					self.pokemon.ev_yield = (y[0], y[1], n, y[3], y[4], y[5])
				elif 'Speed' in data:
					self.pokemon.ev_yield = (y[0], y[1], y[2], y[3], y[4], n)
				else:
					print('Failed to parse EV yield \'%s\'' % data)

