import os.path
import fetch
import pkspecies
import pktypes
import pkabilities

if os.path.exists('cache') == False:
	os.makedirs('cache')
if os.path.exists('data') == False:
	os.makedirs('data')

fetch.GetAndParse('Species', 'cache/species.html', 'data/species.txt', pkspecies.Parser())
fetch.GetAndParse('List_of_Pokemon_by_National_Pokedex_number', 'cache/type.html', 'data/type.txt', pktypes.Parser())
fetch.GetAndParse('List_of_Pokemon_by_abilities', 'cache/ability.html', 'data/ability.txt', pkabilities.Parser())

