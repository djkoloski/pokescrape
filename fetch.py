import os.path
import urllib
import urllib.request

def GetWikiPage(uri, path, force = False):
	if force == True or os.path.isfile(path) == False:
		url = 'http://bulbapedia.bulbagarden.net/wiki/%s' % uri
		print('Fetching \'%s\' to \'%s\'' % (url, path))
		data = urllib.request.urlopen(url)
		out = open(path, 'wb')
		out.write(data.read())
	else:
		print('Using already-fetched file \'%s\'' % path)

def ParseFile(source, parser, dest):
	infile = open(source, 'r')
	outfile = open(dest, 'w')
	print('Parsing \'%s\' to \'%s\'' % (source, dest))
	parser.out = outfile
	parser.feed(infile.read())
	print('Done parsing \'%s\'' % source)

def GetAndParse(uri, interim, out, parser, force = False):
	GetWikiPage(uri, interim, force)
	ParseFile(interim, parser, out)
