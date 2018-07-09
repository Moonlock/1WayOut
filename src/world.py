from __future__ import print_function
import worldGeneration
import string
import random

import items
import npc

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class World:

	def __init__(self):
		self.rooms = []
		worldGeneration.createWorld(self)

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
		player.checkAlive()
		return hostilesExist

	def flee(self):
		print("You run like a chicken.")
		self.curRoom = random.choice(self.curRoom.exits)['room']

	def victoryCheck(self):
		return False
