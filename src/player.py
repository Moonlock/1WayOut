from __future__ import print_function
import string

from items import Weapon, Healing

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class Player:

	def __init__(self, world, name):
		self.world = world
		self.name = name

		self.items = []
		self.wielded = None
		self.health = 20
		self.maxHealth = 20
		self.strength = 1
		self.incompetence = 0

	def getPrompt(self):
		return "%02d" % self.health + "/" + str(self.maxHealth) + " > "

	def status(self):
		print("")
		print(self.name)
		print("\tHealth: " + str(self.health) + "/" + str(self.maxHealth))
		print("\tStrength: " + str(self.strength))
		print("\tWielded: " + ("None" if (self.wielded == None) else str(self.wielded.name)))

	def displayInventory(self):
		if not self.items:
			print("You have no items.")
			return

		print("You have: ", end="")
		for item in self.items[:-1]:
			print(item.name + ", ", end="")
		print(self.items[-1].name + ".")

	def pickUpItem(self, itemName):
		item = self.world.getItem(itemName)
		if item is not None:
			self.items.append(item)
			self.items = sorted(self.items, key=lambda k: k.name)
			self.world.removeItem(item)
			print("You pick up the " + item.name + ".")
		else:
			print("That is not here.")

	def use(self, itemName):
		item = self.getItem(itemName)
		if item is None:
			print("You don't have that.")
			return

		item.useOn(self)

	def recoverHealth(self, health):
		self.health += health
		if self.health > self.maxHealth:
			self.health = self.maxHealth

	# Attempt to wield an item that may not be a weapon.
	def wield(self, weaponName):
		weapon = self.getItem(weaponName)
		if weapon is None:
			print("You don't have that.")
			return
	
		weapon.equipTo(self)

	# Wield an item that is definitely a weapon.
	def wieldWeapon(self, weapon):
		self.items.remove(weapon)
		self.wielded = weapon
		self.strength += weapon.damage
		self.incompetence = weapon.incompetence
		print("You wield the " + weapon.name + ".")

	def unequipWeapon(self):
		weapon = self.wielded

		if weapon is not None:
			print("You unequip the " + weapon.name + ".")
			self.strength -= weapon.damage
			self.items.append(weapon)
			self.wielded = None
			self.incompetence = 0

	def getItem(self, itemName):
		for item in self.items:
			if string.find(item.name, itemName) == 0:
				return item
		return None

	def removeItem(self, item):
		self.items.remove(item)

	def lookWielded(self, weaponName):
		if self.wielded is None:
			return False

		if string.find(self.wielded.name, weaponName) == 0:
			self.wielded.printDescription()
			return True
		return False

	def lookInventory(self, itemName):
		item = self.getItem(itemName)
		if item is not None:
			item.printDescription()
			return True
		return False
			
	def takeTurn(self, opponent):
		print("OPTIONS:")
		print("	Attack")
		print("	Run")
		print("")

		command = input(self.getPrompt())
		if (command == "a") or (command == "attack"):
			self.attack(opponent)
		elif command == "run":
			opponent.takeTurn(self)
			self.world.flee()
		else:
			print("That is not an option.")
			self.takeTurn(opponent)

	def attack(self, opponent):
		print("You hit " + opponent.name + " for " + str(self.strength) + " damage.")
		opponent.takeDamage(self.strength)
		if (self.incompetence > 0):
			print("You hurt yourself "+ str(self.incompetence) +" damage, dummy")
			self.takeDamage(self.incompetence)

	def takeDamage(self, damage):
		self.health -= damage
		print("You are hit for " + str(damage) + " damage.")

	def die(self):
		print("You have died.")
		exit()

	def checkAlive(self):
		if self.health > 0:
			return True
		self.die()
