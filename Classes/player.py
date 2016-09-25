from __future__ import print_function
import string

class Player:

	def __init__(self):
		self.name = raw_input("Please enter your name: ")	
						# Incompatible with Python 3.
		print("")
		print("Greetings, " + self.name + "!")
		print("Type 'help' for help.")
		print("")

		self.items = []
		self.health = 20
		self.strength = 2

	def getItem(self, itemName, world):
		item = world.getItem(itemName)
		if item != None:
			self.items.append(item)
			self.items.sort()
			world.removeItem(item)
		else:
			print("That is not here.")

	def displayInventory(self):
		i = 1
		
		for item in self.items:
			if i < len(self.items):
				print(item["name"] + ", ", end="")
			else:
				print(item["name"] + ".")
			i += 1

	def use(self, itemName):
		for item in self.items:
			if string.find(item['name'], itemName, 0) != -1:
				if item["type"] == "healing":
					self.items.remove(item)
					return
				else:
					print("You can't use that.")
					return
			
		print("You don't have that.")
		return

	def takeTurn(self, opponent):
		print("OPTIONS:")
		print("	Attack")
		print("	Run")

		command = raw_input(">> ")
		if (command == "a") or (command == "attack"):
			self.attack(opponent)
		elif command == "run":
			print("This hasn't been implemented yet.")
		else:
			print("That is not an option.")

	def attack(self, opponent):
		print("You hit " + opponent.name + " for " + str(self.strength) + " damage.")
		opponent.takeDamage(self.strength)

	def takeDamage(self, damage):
		self.health -= damage
		print("You are hit for " + str(damage) + " damage.")
		if self.health <= 0:
			self.die()

	def die(self):
		print("You have died.")
		exit()






