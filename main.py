import parse

tests = [717, 669, 610, 560, 430, 250, 243, 150, 133, 1]

def main():
	for i in tests:
		print(parse.GetAndParse(i))
		print()

main()
