class Player:

	def __init__(self):
		self.name = raw_input("Please enter your name: ")	
						# Incompatible with Python 3.
		print("")
		print("Greetings, " + self.name + "!")
		print("Type 'help' for help.")
		print("")
