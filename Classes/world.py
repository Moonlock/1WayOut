class Room:
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.exits = []
		self.npcs = []
		self.items = []

class World:
	def __init__(self):
		self.rooms = []
		self.createRooms()

	def printMap(self):
		print("	         ___ 			")
		print("	        |   |			")
		print("	        |___| 			")
		print("	   ___   _|_   ___		")
		print("	  |   |-|   |-|   |     ")
		print("	  |___| |___| |___|		")
		print("	         _|_			")
		print("	        |   |			")
		print("	        |___|			")

	def createRooms(self):
		north = Room("North", "The north room.")
		south = Room("South", "The south room.")
		east = Room("East", "The east room.")
		west = Room("West", "The west room.")
		center = Room("Center", "The center room.")

		north.exits.append(center)
		south.exits.append(center)
		east.exits.append(center)
		west.exits.append(center)
		center.exits.append(south)
		center.exits.append(north)
		center.exits.append(west)
		center.exits.append(east)

		north.items.append("item")

		self.rooms.append(north)
		self.rooms.append(south)
		self.rooms.append(east)
		self.rooms.append(west)
		self.rooms.append(center)

















