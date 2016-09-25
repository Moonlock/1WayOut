
from __future__ import print_function
import string

import items
import zombie

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
		if newRoom.lower() == "n":
			newRoom = "North"
		elif newRoom.lower() == "s":
			newRoom = "South"
		elif newRoom.lower() == "e":
			newRoom = "East"
		elif newRoom.lower() == "s":
			newRoom = "South"

		for exit in self.curRoom.exits:
			if exit['localName'].lower() == newRoom.lower():
				self.curRoom = exit['room']
				self.displayRoom()
				return
		print("You can't go that way.")

	def displayRoom(self):
		print("")
		print(self.curRoom.name)
		print(self.curRoom.desc)

		print("Exits: ", end="")
		self.displayList(self.curRoom.exits, "localName")

		if self.curRoom.items != []:
			print("Items: ", end="")
			self.displayList(self.curRoom.items, "name")

		if self.curRoom.npcs != []:
			print("You see: ", end="")
			#self.displayList(self.curRoom.npcs, "name")
			print(self.curRoom.npcs[0].name)

		print("")

	def displayList(self, myList, name):
		i = 1

		for element in myList:
			if i < len(myList):
				print(element[name] + ", ", end="")
			else:
				print(element[name] + ".")
			i += 1

	def getItem(self, itemName):
		for item in self.curRoom.items:
			if string.find(item['name'], itemName, 0) != -1:
				return item
		return None

	def removeItem(self, item):
		self.curRoom.items.remove(item)

	def removeNpc(self, npc):
		self.curRoom.npcs.remove(npc)

	def startFight(self, player, target):
		opponent = self.getNpc(target)
		if opponent != None:
			print("You attack " + opponent.name + ".")
			self.fight(player, opponent)
		else:
			print("That is not here.")

	def fight(self, attacker, defender):
		while (attacker.health > 0) and (defender.health > 0):
			attacker.takeTurn(defender)
			if defender.health > 0:
				defender.takeTurn(attacker)
			else:
				self.removeNpc(defender)

	def getNpc(self, npcName):
		for npc in self.curRoom.npcs:
			if string.find(npc.name, npcName, 0) != -1:
				return npc
		return None

	def createRooms(self):
		north = self.Room()
		south = self.Room()
		east = self.Room()
		west = self.Room()
		center = self.Room()

		zom = zombie.Zombie("zombie")

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

		center.name = "Center"
		center.desc = "The center room."
		center.exits.append({"room": north, "localName": "North"})
		center.exits.append({"room": south, "localName": "South"})
		center.exits.append({"room": east, "localName": "East"})
		center.exits.append({"room": west, "localName": "West"})

		north.items.append(items.createAxe())
		west.items.append(items.createHealthPotion())
		east.items.append(items.createHealthPotion())
		south.npcs.append(zom)

		self.rooms.append(north)
		self.rooms.append(south)
		self.rooms.append(east)
		self.rooms.append(west)
		self.rooms.append(center)

		self.curRoom = center

					

