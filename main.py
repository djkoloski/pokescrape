import parse
from pk import *
from move import *
from ability import *

# XXX Hacks around bugs in Serebii's HTML is marked with a comment beginning with XXX
# TODO Some moves may be missing from the source I got the moves file from (esp. ones that do nothing)
# TODO Scrape hatch counter from another source, serebii is unreliable and may not include it
# TODO Scrape base exp yields, body style, and color from another source, serebii does not have it

# These pages have all of the information for each of the forms, they'll have to be put in manually
# Deoxys
# Wormadam
# Giratina
# Shaymin
# Basculin (page not updated from BW)
# Darmanitan
# Tornadus
# Thundurus
# Landorus
# Kyurem
# Keldeo (page not update from BW)
# Meloetta
# Floette
# Aegislash
# Pumpkaboo
# Gourgeist
# Hoopa
problematic_pokemon = [386, 413, 487, 492, 550, 555, 641, 642, 645, 646, 647, 648, 670, 681, 710, 711, 720]

def main():
	parse.Init()
	
	out = open('data/pokedex.json', 'w')
	
	out.write('{\n')
	
	out.write('"moves":[\n')
	
	for i in range(0, len(moves)):
		m = moves[i]
		
		out.write("""{
	"name":"%s",
	"type":%i,
	"pp":%i,
	"power":%i,
	"accuracy":%i,
	"category":%i,
	"damage":%i,
	"description":"%s"
}%s
""" % (
			m.name,
			m.type,
			m.pp,
			m.power,
			m.accuracy,
			m.category,
			m.damage,
			m.description.replace('"', '\\"'),
			',' if i != len(moves) - 1 else ''
		))
	
	out.write('],\n')
	
	out.write('"abilities":[\n')
	
	for i in range(0, len(abilities)):
		a = abilities[i]
		
		out.write("""{
	"name":"%s",
	"description":"%s"
}%s
""" % (
			a.name,
			a.description.replace('"', '\\"'),
			',' if i != len(abilities) - 1 else ''
		))
	
	out.write('],\n')
	
	out.write('"pokemon":[\n')
	
	for i in range(1, num_pokemon + 1):
		if i in problematic_pokemon:
			continue
		
		p = parse.GetAndParse(i)
		
		out.write("""{
	"number":%i,
	"name":"%s",
	"species":"%s",
	"types":[%i,%i],
	"abilities":[%i,%i,%i],
	"genderThreshold":%i,
	"catchRate":%i,
	"eggGroups":[%i,%i],
	"hatchCounter":%i,
	"height":%f,
	"weight":%f,
	"baseExpYield":%i,
	"baseFriendship":%i,
	"expGroup":%i,
	"evYield":[%i,%i,%i,%i,%i,%i],
	"bodyStyle":%i,
	"color":%i,
	"baseStats":[%i,%i,%i,%i,%i,%i],
	"pokedexX":"%s",
	"pokedexY":"%s",
	"pokedexOR":"%s",
	"pokedexAS":"%s",
	"learnset":
	{
		"xy":%s,
		"xyLevels":%s,
		"oras":%s,
		"orasLevels":%s,
		"tmhm":%s,
		"egg":%s,
		"tutor":%s,
		"special":%s,
		"evolve":%s,
		"transfer":%s,
	}
}%s
""" % (
			p.national_dex_number,
			p.name,
			p.species,
			p.types[0], p.types[1],
			p.abilities[0], p.abilities[1], p.abilities[2],
			p.gender_threshold,
			p.catch_rate,
			p.egg_groups[0], p.egg_groups[1],
			p.hatch_counter,
			p.height,
			p.weight,
			p.base_exp_yield,
			p.base_friendship,
			p.exp_group,
			p.ev_yield[0], p.ev_yield[1], p.ev_yield[2], p.ev_yield[3], p.ev_yield[4], p.ev_yield[5],
			p.body_style,
			p.color,
			p.base_stats[0], p.base_stats[1], p.base_stats[2], p.base_stats[3], p.base_stats[4], p.base_stats[5],
			p.pokedex_x.replace('"', '\\"'),
			p.pokedex_y.replace('"', '\\"'),
			p.pokedex_or.replace('"', '\\"'),
			p.pokedex_as.replace('"', '\\"'),
			str([i[1] for i in p.learnset_level_xy]),
			str([i[0] for i in p.learnset_level_xy]),
			str([i[1] for i in p.learnset_level_oras]),
			str([i[0] for i in p.learnset_level_oras]),
			str(p.learnset_machine),
			str(p.learnset_egg_move),
			str(p.learnset_tutor),
			str(p.learnset_special),
			str(p.learnset_evolve),
			str(p.learnset_transfer),
			',' if i < num_pokemon - 1 else ''
		))
		
		
	
	out.write(']\n')
	
	out.write('}')
	
	out.close()

main()
