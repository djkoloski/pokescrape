from html.parser import HTMLParser

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
		return self.tables == 1 and self.tableDepth == 2
	
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
					self.out.write('\n')
			elif tag == 'td':
				if self.tdIndex == 0:
					self.out.write(self.tdtext.lstrip('0'))
				elif self.tdIndex == 2:
					self.out.write('\t%s' % self.tdtext)
				elif self.tdIndex == 3:
					self.out.write('\t%s' % self.tdtext[:-8])
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
