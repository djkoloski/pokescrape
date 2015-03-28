import parse

tests = [717, 669, 610, 560, 430, 250, 243, 150, 133, 25, 1]

# XXX Hacks around bugs in Serebii's HTML is marked with a comment beginning with XXX
# TODO Some moves may be missing from the source I got the moves file from (esp. ones that do nothing)
# TODO Scrape hatch counter from another source, serebii is unreliable and may not include it
# TODO Scrape base exp yields, body style, and color from another source, serebii does not have it

def main():
	parse.Init()
	for i in tests:
		print(parse.GetAndParse(i))
		print()

main()
