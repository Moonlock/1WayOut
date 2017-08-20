from __future__ import print_function
import string
import random

import items
import zombie
from random import random

class World:

	class Room:
		def __init__(self):
			self.name = ""
			self.desc = ""
			self.exits = []
			self.npcs = []
			self.items = []

	def __init__(self):
		self.rooms = []
		self.remainingZombies = 2
		self.createRooms()

	def printMap(self):
		# Mark the current room with an x.
		print("	         ___ 			")

		if self.curRoom.name == "North":
			print("	        | x |			")
		else:
			print("	        |   |			")

		print("	        |___| 			")
		print("	   ___   _|_   ___		")

		if self.curRoom.name == "West":
			print("	  | x |-|   |-|   |     ")
		elif self.curRoom.name == "Center":
			print("	  |   |-| x |-|   |     ")
		elif self.curRoom.name == "East":
			print("	  |   |-|   |-| x |     ")
		else:
			print("	  |   |-|   |-|   |     ")

		print("	  |___| |___| |___|		")
		print("	         _|_			")

		if self.curRoom.name == "South":
			print("	        | x |			")
		else:
			print("	        |   |			")
			
		print("	        |___|			")

	def move(self, newRoom):
		for exit in self.curRoom.exits:
			if string.find(exit['localName'].lower(), newRoom.lower()) == 0:
				self.curRoom = exit['room']
				self.displayRoom()
				return
		print("You can't go that way.")

	def displayRoom(self):
		print("")
		print(self.curRoom.name)
		print(self.curRoom.desc)

		self.displayExits()
		self.displayItems()
		self.displayNpcs()

	def displayExits(self):
		print("Exits: ", end="")
		for exit in self.curRoom.exits[:-1]:
			print(exit['localName'] + ", ", end="")
		print(self.curRoom.exits[-1]['localName'] + ".")

	def displayItems(self):
		if not self.curRoom.items:
			return

		print("Items: ", end="")
		self.displayList(self.curRoom.items)

	def displayNpcs(self):
		if not self.curRoom.npcs:
			return

		print("You see: ", end="")
		self.displayList(self.curRoom.npcs)

	def displayList(self, myList):
		for element in myList[:-1]:
			print(element.name + ", ", end="")
		print(myList[-1].name + ".")

	def look(self, targetName, player):
		if self.lookNpc(targetName) == True:
			return
		if self.lookGround(targetName) == True:
			return
		if player.lookInventory(targetName) == True:
			return
		if player.lookWielded(targetName) == True:
			return

		print("That is not here.")

	def lookNpc(self, npcName):
		npc = self.getNpc(npcName)
		if npc != None:
			npc.printDescription()
			return True
		return False

	def lookGround(self, itemName):
		item = self.getItem(itemName)
		if item != None:
			item.printDescription()
			return True
		return False

	def getItem(self, itemName):
		for item in self.curRoom.items:
			if string.find(item.name, itemName) == 0:
				return item
		return None

	def removeItem(self, item):
		self.curRoom.items.remove(item)

	def getNpc(self, npcName):
		for npc in self.curRoom.npcs:
			if string.find(npc.name, npcName) == 0:
				return npc
		return None

	def removeNpc(self, npc):
		self.curRoom.npcs.remove(npc)

	def startFight(self, player, target):
		opponent = self.getNpc(target)
		if opponent == None:
			print("That is not here.")
			return

		print("You attack " + opponent.name + ".")
		opponent.becomeHostile()
		self.fight(player, opponent)

	def fight(self, attacker, defender):
		while self.fightIsOngoing(attacker):
			attacker.takeTurn(defender)
			if self.fightIsOngoing(attacker):
				defender.takeTurn(attacker)
			print("")

	def fightIsOngoing(self, player):
		hostilesExist = False
		for npc in self.curRoom.npcs:
			if npc.isHostile:
				hostilesExist = True
		return player.isAlive() and hostilesExist

	def flee(self):
		print("You run like a chicken.")
		self.curRoom = random.choice(self.curRoom.exits)['room']

	def victoryCheck(self):
		if self.remainingZombies == 0:
			print("You win!")
			exit()

	def createRooms(self):
		north = self.Room()
		south = self.Room()
		east = self.Room()
		west = self.Room()
		center = self.Room()
		wester = self.Room()
		westest = self.Room()

		zom0 = zombie.Zombie("zombie", 5, 1, "Brains....", self)
		zom1 = zombie.Zombie("super zombie", 20, 3, "He looks pretty tough.", self)

		north.name = "North"
		north.desc = "The north room."
		north.exits.append({"room": center, "localName": "South"})

		south.name = "South"
		south.desc = "The south room."
		south.exits.append({"room": center, "localName": "North"})

		east.name = "East"
		east.desc = "The east room."
		east.exits.append({"room": center, "localName": "West"})

		west.name = "West"
		west.desc = "The west room."
		west.exits.append({"room": center, "localName": "East"})
		west.exits.append({"room": wester, "localName": "West"})

		wester.name = "Wester"
		wester.desc = "The wester room."
		wester.exits.append({"room": west, "localName": "East"})
		wester.exits.append({"room": westest, "localName": "West"})

		westest.name = "Westest"
		westest.desc = "The westest room."
		westest.exits.append({"room": wester, "localName": "East"})


		center.name = "Center"
		center.desc = "The center room."
		center.exits.append({"room": north, "localName": "North"})
		center.exits.append({"room": south, "localName": "South"})
		center.exits.append({"room": east, "localName": "East"})
		center.exits.append({"room": west, "localName": "West"})


		rand = random()
		print(rand)
		if (int)(rand*2):
			west.items.append(items.Axe())
		else:
			west.items.append(items.DumbAxe())

		rond = random()
		print(rond)
		if (int)(rond*2):
			east.items.append(items.HealthPotion())
		else:
			east.items.append(items.DeathJuice())

		rind = random()
		if (int)(rind*2):
			north.npcs.append(zom0)
		else: 
			north.npcs.append(zom1)

		rund = random()
		if (int)(rund*2):
			south.npcs.append(zom0)
		else: 
			south.npcs.append(zom1)

		wester.items.append(items.HealthPotion())
		westest.npcs.append(zom1)

		self.rooms.append(north)
		self.rooms.append(south)
		self.rooms.append(east)
		self.rooms.append(west)
		self.rooms.append(center)

		self.curRoom = center
