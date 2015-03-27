from html.parser import HTMLParser

PK_TYPES = {
	'None': 0,
	'Normal': 1,
	'Fighting': 2,
	'Flying': 3,
	'Poison': 4,
	'Ground': 5,
	'Rock': 6,
	'Bug': 7,
	'Ghost': 8,
	'Steel': 9,
	'Fire': 10,
	'Water': 11,
	'Grass': 12,
	'Electric': 13,
	'Psychic': 14,
	'Ice': 15,
	'Dragon': 16,
	'Dark': 17,
	'Fairy': 18
}

class Parser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.tables = 0
		self.tableDepth = 0
		self.trIndex = 0
		self.tdIndex = 0
		self.intd = False
		self.tdtext = ''
	
	def in_table(self):
		return self.tables >= 1 and self.tables <= 6 and self.tableDepth == 1
	
	def handle_starttag(self, tag, attrs):
		if self.in_table():
			if tag == 'tr':
				self.tdIndex = 0
			elif tag == 'td':
				self.intd = True
		if tag == 'table':
			self.tableDepth += 1
	
	def handle_endtag(self, tag):
		if self.in_table():
			if tag == 'tr':
				self.trIndex += 1
				if self.tdIndex != 0:
					if self.tdIndex != 6:
						self.out.write('\t%s' % str(PK_TYPES['None']))
					self.out.write('\n')
			elif tag == 'td':
				if self.tdIndex == 1:
					self.out.write(self.tdtext[1:].lstrip('0'))
				elif self.tdIndex == 4 or self.tdIndex == 5:
					self.out.write('\t%s' % str(PK_TYPES[self.tdtext]))
				self.tdIndex += 1
				self.intd = False
				self.tdtext = ''
		if tag == 'table':
			self.tableDepth -= 1
			if self.tableDepth == 0:
				self.tables += 1
	
	def handle_data(self, data):
		if self.in_table() and self.intd:
			self.tdtext += data.strip()
