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
					print("You can't use that, dick.")
					return
			
		print("Hey asshole, you don't have that.")
		return






