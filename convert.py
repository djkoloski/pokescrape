from pk import *
import parse
from move import *

xy = []
xyLevels = []
oras = []
orasLevels = []
tmhm = []
egg = []
tutor = []
special = []
evolve = []
transfer = []

def main():
	parse.Init()
	
	source = open('learn_in.txt', 'r')
	
	mode = None
	
	for line in source:
		line = line.strip()
		if line == 'level:':
			mode = 'level'
		elif line == 'levelsplit:':
			mode = 'levelsplit'
		elif line == 'tmhm:':
			mode = 'tmhm'
		elif line == 'egg:':
			mode = 'egg'
		elif line == 'tutor:':
			mode = 'tutor'
		elif line == 'special:':
			mode = 'special'
		elif line == 'evolve:':
			mode = 'evolve'
		elif line == 'transfer:':
			mode = 'transfer'
		else:
			pieces = line.split('\t')
			if mode == 'level':
				if pieces[0] == 'Start':
					xyLevels.append(0)
					orasLevels.append(0)
				else:
					xyLevels.append(int(pieces[0]))
					orasLevels.append(int(pieces[0]))
				name = pieces[1].strip().lower()
				xy.append(moves_map[name])
				oras.append(moves_map[name])
			elif mode == 'levelsplit':
				name = pieces[2].strip().lower()
				if pieces[0] == 'Start':
					xyLevels.append(0)
					xy.append(moves_map[name])
				elif pieces[0] != 'N/A':
					xyLevels.append(int(pieces[0]))
					xy.append(moves_map[name])
				if pieces[1] == 'Start':
					orasLevels.append(0)
					oras.append(moves_map[name])
				elif pieces[1] != 'N/A':
					orasLevels.append(int(pieces[1]))
					oras.append(moves_map[name])
			elif mode == 'tmhm':
				tmhm.append(moves_map[pieces[2].strip().lower()])
			elif mode == 'egg':
				egg.append(moves_map[pieces[1].strip().rstrip('*').lower()])
			elif mode == 'tutor':
				tutor.append(moves_map[pieces[4].strip().lower()])
			elif mode == 'evolve':
				evolve.append(moves_map[pieces[1].strip().lower()])
			else:
				print('Not implemented!')
	
	source.close()
	
	out = open('learn_out.txt', 'w')
	
	out.write('''"xy":%s,
"xyLevels":%s,
"oras":%s,
"orasLevels":%s,
"tmhm":%s,
"egg":%s,
"tutor":%s,
"special":%s,
"evolve":%s,
"transfer":%s''' % (
		str(xy),
		str(xyLevels),
		str(oras),
		str(orasLevels),
		str(tmhm),
		str(egg),
		str(tutor),
		str(special),
		str(evolve),
		str(transfer)))
	
	out.close()

main()
