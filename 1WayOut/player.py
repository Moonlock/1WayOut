from __future__ import print_function
import string

class Player:

	def __init__(self, world):
		self.world = world
		self.name = raw_input("Please enter your name: ")	
						# Incompatible with Python 3.
		print("")
		print("Greetings, " + self.name + "!")
		print("Type 'help' for help.")
		print("")

		self.items = []
		self.wielded = None
		self.health = 20
		self.maxHealth = 20
		self.strength = 1

	def status(self):
		print("")
		print(self.name)
		print("\tHealth: " + str(self.health) + "/" + str(self.maxHealth))
		print("\tStrength: " + str(self.strength))
		print("\tWielded: " + ("None" if (self.wielded == None) else str(self.wielded['name'])))
		print("")

	def look(self, itemName):
		item = self.getItem(itemName)
		if item != None:
			print(item['desc'])
			return

		if self.wielded != None:
			if string.find(self.wielded['name'], itemName) == 0:
				print(self.wielded['desc'])
				return

		print("That is not here.")

	def getItem(self, itemName):
		for item in self.items:
			if string.find(item['name'], itemName) == 0:
				return item
		return None

	def pickUpItem(self, itemName):
		item = self.world.getItem(itemName)
		if item != None:
			self.items.append(item)
			self.items = sorted(self.items, key=lambda k: k['name'])
			self.world.removeItem(item)
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
			if string.find(item['name'], itemName) == 0:
				if item["type"] == "healing":
					self.items.remove(item)
					self.health += item['value']
					if self.health > self.maxHealth:
						self.health = self.maxHealth
					print("The " + item['name'] + " recovers " + str(item['value']) + " health.")
					return
				else:
					print("You can't use that.")
					return
			
		print("You don't have that.")
		return

	def wield(self, weaponName):
		for weapon in self.items:
			if string.find(weapon['name'], weaponName) == 0:
				if weapon["type"] == "weapon":
					if self.wielded != None:
						print("You're already wielding something.")
						return
					self.items.remove(weapon)
					self.wielded = weapon
					self.strength += weapon['value']
					print("You wield the " + weapon['name'] + ".")
					return
				else:
					print("You can't wield that.")
					return
			
		print("You don't have that.")
		return

	def takeTurn(self, opponent):
		print("OPTIONS:")
		print("	Attack")
		print("	Run")

		command = raw_input(str(self.health) + "> ")
		if (command == "a") or (command == "attack"):
			self.attack(opponent)
		elif command == "run":
			self.world.flee()
		else:
			print("That is not an option.")
			self.takeTurn(opponent)

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

	def isAlive(self):
		return self.health > 0



