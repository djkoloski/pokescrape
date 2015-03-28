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
		super().__init__()
		
		self.pokemon = Pokemon()
		
		self.cur_fooinfo = 0
		self.td_cur_level = 0
		self.fooinfo_enter_level = -1
		self.fooinfo_cur_td = 0
		self.cen_enter_level = -1
		self.cen_cur_td = 0
	
	def handle_starttag(self, tag, attrs):
		if tag == 'td':
			if self.fooinfo_enter_level == -1 and ('class', 'fooinfo') in attrs:
				self.fooinfo_enter_level = self.td_cur_level
			if self.cen_enter_level == -1 and ('class', 'cen') in attrs:
				self.cen_enter_level = self.td_cur_level
			self.td_cur_level += 1
		if tag == 'a':
			if self.cen_enter_level != -1:
				if self.cur_fooinfo == 5:
					ptype = PkType[attrs[0][1][12:-6]]
					if self.pokemon.types[0] == 0:
						self.pokemon.types = (ptype, 0)
					else:
						self.pokemon.types = (self.pokemon.types[0], ptype)
	
	def handle_endtag(self, tag):
		if tag == 'td':
			self.td_cur_level -= 1
			if self.fooinfo_enter_level != -1:
				self.fooinfo_cur_td += 1
			if self.fooinfo_enter_level == self.td_cur_level:
				self.cur_fooinfo += 1
				self.fooinfo_enter_level = -1
				self.fooinfo_cur_td = 0
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
			#elif self.
		if self.cen_enter_level != -1:
			pass

