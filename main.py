import parse

tests = [717, 669, 610, 560, 430, 250, 243, 150, 133, 25, 1]

# TODO Hacks around bugs in Serebii's HTML is marked with a comment beginning with XXX
# TODO Scrape hatch counter from another source, serebii is unreliable and may not include it
# TODO Scrape base exp yields, body style, and color from another source, serebii does not have it

def main():
	for i in tests:
		print(parse.GetAndParse(i))
		print()

main()
