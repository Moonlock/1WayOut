class Player:

	def __init__(self):
		self.name = raw_input("Please enter your name: ")	
						# Incompatible with Python 3.
		print("")
		print("Greetings, " + self.name + "!")
		print("Welcome to 1 Way Out.")
		print("Type 'help' for help.")
		print("")
		self.initPlayer()

	class weapons:
		def __init__(self):
			self.equip = False
			self.name = "Bar of soap and a sock"
			self.damage = 2 

	class statss:
		def __init__(self):
			self.health = 5
			self.strength = 1

	def initPlayer(self):
		w1 = self.weapons()
		p1Stats = self.statss()

		self.weapon = w1
		self.stats = p1Stats