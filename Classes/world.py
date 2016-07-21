
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
		north = self.Room()
		south = self.Room()
		east = self.Room()
		west = self.Room()
		center = self.Room()

		north.name = "North"
		north.desc = "The north room."
		north.exits.append(center)

		south.name = "South"
		south.desc = "The south room."
		south.exits.append(center)

		east.name = "East"
		east.desc = "The east room."
		east.exits.append(center)

		west.name = "West"
		west.desc = "The west room."
		west.exits.append(center)

		center.name = "Center"
		center.desc = "The center room."
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

		self.curRoom = center

		def move(self, newRoom):
			for i in self.curRoom.exits
				if i.name = newRoom
					self.curRoom = newRoom

					

