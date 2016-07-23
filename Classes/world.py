
from __future__ import print_function

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
		for exit in self.curRoom.exits:
			print(exit['localName'] + ", ", end="")
		print("\n")


	def createRooms(self):
		north = self.Room()
		south = self.Room()
		east = self.Room()
		west = self.Room()
		center = self.Room()

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

		north.items.append("item")

		self.rooms.append(north)
		self.rooms.append(south)
		self.rooms.append(east)
		self.rooms.append(west)
		self.rooms.append(center)

		self.curRoom = center

					

