import csv as csv # idk why I needed "as csv" but for some reason it doesn't work without it

def main():
	notdecided = True
	while notdecided == True:
		print("Where do you want to go?")
		print("Options:")
		print("\ta. Dump all data and leave you to process it.")
		print("\tb. Analyze and interpret the data.")
	
		option = str(input("(lowercase letter) > "))

		if option == "a":
			dump()
			notdecided = False

		if option == "b":
			kowalski_analysis()
			notdecided = False

		else:
			print("try again!")
			# should loop automatically because of the notdecided while loop
			

def dump():
	raw_data = open("data.csv", "r")
	address = csv.reader(raw_data)
	for row in address:
		print(": ".join(row))

def kowalski_analysis():
	raw_data = open("data.csv", "r") # opens data
	address = csv.DictReader(raw_data) # turns it into a json-like format.
	# There's a bug in this process which I don't think is my fault where numbers automatically get turned
	# into strings, and are then sorted alphabetically later (not numerically)

	dictionary = [] # creates new dictionary
	for row in address:
		row["Population"] = int(row["Population"])
		dictionary.append(row) # fills the dictionary

	def sort(e):
		return e['Population'] # the criteria that we sort the data by
	
	dictionary.sort(key=sort)

	for i in range(58): # adjust number for a greater quantity of data
		print(dictionary[i])

main()
