import modules.html_starter as hs

def menu():
	print("\n - - - - - Programming Starter Kit - - - - - \n")
	print("Select the template you want to generate\n\n")
	print("1) HTML")
	print("2) CSS")
	print("3) C++")
	print("4) PUG")
	print("5) SASS")
	print("6) EXIT")
	selection = int(input("> "))

	if selection == 1:
		username = input("Name/Username: ")
		title = input("Title for page: ")
		jquery = input("Include jQuery? [y/n]: ")
		if jquery == "y":
			html = hs.html_parser(username, title, True)
		else:
			html = hs.html_parser(username, title, False)

		with open("./outputs/basic.html", "w") as f:
			f.write(html)

		print("HTML file generated!")
	
if __name__ == "__main__":
	menu()