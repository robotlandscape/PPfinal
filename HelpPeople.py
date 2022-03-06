def main_menu():
	notdecided == true
	while notdecided == true:
		print("where do you want to go?")
		print("options:")
		print("\ta. Import the data as a csv.")
		print("\tb. Dump all data and leave you to process it."
		print("\tc. Analyze and interpret the data.")
	
		let option = str(input("(lowercase letter) > "))
		if option == "a":
			notdecided = false
			import_it()
		if option == "b":
			notdecided = false
			dump()
		if option == "c":
			notdecided = false
			kowalski_analysis()
		else:
			print("try again!")
			// should loop automatically because of the notdecided while loop
			  
def import_it():
	// TODO
			  
def main():
	main_menu()
