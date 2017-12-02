import random

import zombie
import items

class Room:
	def __init__(self):
		self.name = ""
		self.desc = ""
		self.exits = []
		self.npcs = []
		self.items = []

def createWorld(world):
	terranceCrs_0 = Room()
	terranceCrs_1 = Room()
	terranceCrs_2 = Room()
	terranceCrs_3 = Room()
	terranceCrs_4 = Room()
	terranceCrs_5 = Room()
	terranceCrs_6 = Room()
	terranceCrs_7 = Room()
	floydAve_0 = Room()
	floydAve_1 = Room()
	floydAve_2 = Room()
	floydAve_3 = Room()
	intfloydZirrila = Room()
	mainSt_0 = Room()
	mainSt_1 = Room()
	mainSt_2 = Room()
	mainSt_3 = Room()
	mainSt_4 = Room()
	mainSt_5 = Room()
	mainSt_6 = Room()
	mainSt_7 = Room()
	mainSt_8 = Room()
	mainSt_9 = Room()
	carlAve_0 = Room()
	carlAve_1 = Room()
	carlAve_2 = Room()
	carlAve_3 = Room()
	carlAve_4 = Room()
	quintenAve_0 = Room()
	quintenAve_1 = Room()
	quintenAve_2 = Room()
	quintenAve_3 = Room()
	terentinoSt_0 = Room()
	terentinoSt_1 = Room()
	terentinoSt_2 = Room()
	newtonAve_0 = Room()
	mozenSt_0 = Room()
	mozenSt_1 = Room()
	mozenSt_2 = Room()
	mozenSt_3 = Room()
	zirrilaSt_0 = Room()
	zirrilaSt_1 = Room()
	zirrilaSt_2 = Room()	
	zirrilaSt_3 = Room()
	monroeSt_0 = Room()
	monroeSt_1 = Room()	
	monroeSt_2 = Room()
	monroeSt_3 = Room()

	hardware_0 = Room()
	hardwareAisle_0 = Room()
	hardwareAisle_1 = Room()
	hardwareAisle_2 = Room()
	hardwareWashroom_0 = Room()
	hardwareCashierTill_0 = Room()

	gasStation_0 = Room()

	restaurant_0 = Room()

	hotel_0 = Room()

	townHall_0 = Room()

	park_0 = Room()

	school_0 = Room()

	pharmacy_0 = Room()

	house_0 = Room()

	house_1 = Room()

	terranceCrs_0.name = "Terrance Crescent"
	terranceCrs_0.desc = ""
	terranceCrs_0.exits.append({"room" : terranceCrs_1, "localName" : "north" })
	terranceCrs_0.exits.append({"room" : carlAve_4, "localName" : "west" })
	terranceCrs_0.exits.append({"room" : zirrilaSt_0, "localName" : "east" })

	terranceCrs_1.name = "Terrance Crescent"
	terranceCrs_1.desc = ""
	terranceCrs_1.exits.append({"room" : terranceCrs_2, "localName" : "north east" })
	terranceCrs_1.exits.append({"room" : terranceCrs_0, "localName" : "south" })	
	terranceCrs_1.exits.append({"room" : monroeSt_0, "localName" : "east" })

	terranceCrs_2.name = "Terrance Crescent"
	terranceCrs_2.desc = ""
	terranceCrs_2.exits.append({"room" : terranceCrs_3, "localName" : "east" })
	terranceCrs_2.exits.append({"room" : terranceCrs_1, "localName" : "south west" })	

	terranceCrs_3.name = "Terrance Crescent"
	terranceCrs_3.desc = ""
	terranceCrs_3.exits.append({"room" : terranceCrs_4, "localName" : "east" })
	terranceCrs_3.exits.append({"room" : terranceCrs_2, "localName" : "west" })	

	terranceCrs_4.name = "Terrance Crescent"
	terranceCrs_4.desc = ""
	terranceCrs_4.exits.append({"room" : terranceCrs_5, "localName" : "east" })
	terranceCrs_4.exits.append({"room" : terranceCrs_3, "localName" : "west" })

	terranceCrs_5.name = "Terrance Crescent"
	terranceCrs_5.desc = ""
	terranceCrs_5.exits.append({"room" : terranceCrs_6, "localName" : "south east" })
	terranceCrs_5.exits.append({"room" : terranceCrs_4, "localName" : "west" })

	terranceCrs_6.name = "Terrance Crescent"
	terranceCrs_6.desc = ""
	terranceCrs_6.exits.append({"room" : terranceCrs_7, "localName" : "south east" })
	terranceCrs_6.exits.append({"room" : terranceCrs_5, "localName" : "north west" })	
	terranceCrs_6.exits.append({"room" : monroeSt_3, "localName" : "west" })

	terranceCrs_7.name = "Terrance Crescent"
	terranceCrs_7.desc = ""
	terranceCrs_7.exits.append({"room" : quintenAve_3, "localName" : "south east" })
	terranceCrs_7.exits.append({"room" : zirrilaSt_3, "localName" : "west" })

	floydAve_0.name = "Floyd Avenue"
	floydAve_0.desc = ""
	floydAve_0.exits.append({"room" : floydAve_1, "localName" : "north" })
	floydAve_0.exits.append({"room" : mainSt_5, "localName" : "south" })

	floydAve_1.name = "Floyd Avenue"
	floydAve_1.desc = ""
	floydAve_1.exits.append({"room" : floydAve_2, "localName" : "north" })
	floydAve_1.exits.append({"room" : floydAve_0, "localName" : "south" })	
	floydAve_1.exits.append({"room" : mozenSt_3, "localName" : "west" })

	floydAve_2.name = "Floyd Avenue"
	floydAve_2.desc = ""
	floydAve_2.exits.append({"room" : floydAve_3, "localName" : "north" })
	floydAve_2.exits.append({"room" : floydAve_1, "localName" : "south" })
	floydAve_2.exits.append({"room" : terentinoSt_0, "localName" : "east" })	

	floydAve_3.name = "Floyd Avenue"
	floydAve_3.desc = ""
	floydAve_3.exits.append({"room" : intfloydZirrila, "localName" : "north" })
	floydAve_3.exits.append({"room" : floydAve_2, "localName" : "south" })	

	intfloydZirrila.name = "Floyd/Zirrila Intersection"
	intfloydZirrila.desc = ""
	intfloydZirrila.exits.append({"room" : monroeSt_2, "localName" : "north" })	
	intfloydZirrila.exits.append({"room" : zirrilaSt_2, "localName" : "east" })		
	intfloydZirrila.exits.append({"room" : zirrilaSt_1, "localName" : "west" })
	intfloydZirrila.exits.append({"room" : floydAve_3, "localName" : "south" })		

	mainSt_0.name = "Main Street"
	mainSt_0.desc = ""
	mainSt_0.exits.append({"room" : carlAve_0, "localName" : "north" })
	mainSt_0.exits.append({"room" : mainSt_1, "localName" : "east" })

	mainSt_1.name = "Main Street"
	mainSt_1.desc = ""
	mainSt_1.exits.append({"room" : mainSt_2, "localName" : "east" })
	mainSt_1.exits.append({"room" : mainSt_0, "localName" : "west" })

	mainSt_2.name = "Main Street"
	mainSt_2.desc = ""
	mainSt_2.exits.append({"room" : mainSt_3, "localName" : "east" })
	mainSt_2.exits.append({"room" : mainSt_1, "localName" : "west" })

	mainSt_3.name = "Main Street"
	mainSt_3.desc = ""
	mainSt_3.exits.append({"room" : mainSt_4, "localName" : "east" })
	mainSt_3.exits.append({"room" : mainSt_2, "localName" : "west" })
	mainSt_3.exits.append({"room" : newtonAve_0, "localName" : "north" })		

	mainSt_4.name = "Main Street"
	mainSt_4.desc = ""
	mainSt_4.exits.append({"room" : mainSt_5, "localName" : "east" })
	mainSt_4.exits.append({"room" : mainSt_3, "localName" : "west" })

	mainSt_5.name = "Main Street"
	mainSt_5.desc = ""
	mainSt_5.exits.append({"room" : mainSt_6, "localName" : "east" })
	mainSt_5.exits.append({"room" : mainSt_4, "localName" : "west" })
	mainSt_5.exits.append({"room" : floydAve_0, "localName" : "north" })	

	mainSt_6.name = "Main Street"
	mainSt_6.desc = ""
	mainSt_6.exits.append({"room" : mainSt_7, "localName" : "east" })
	mainSt_6.exits.append({"room" : mainSt_5, "localName" : "west" })

	mainSt_7.name = "Main Street"
	mainSt_7.desc = ""
	mainSt_7.exits.append({"room" : mainSt_8, "localName" : "east" })
	mainSt_7.exits.append({"room" : mainSt_6, "localName" : "west" })

	mainSt_8.name = "Main Street"
	mainSt_8.desc = ""
	mainSt_8.exits.append({"room" : mainSt_9, "localName" : "east" })
	mainSt_8.exits.append({"room" : mainSt_7, "localName" : "west" })
	mainSt_8.exits.append({"room" : hardware_0, "localName" : "Hardware Store" })	

	mainSt_9.name = "Main Street"
	mainSt_9.desc = ""
	mainSt_9.exits.append({"room" : mainSt_8, "localName" : "west" })
	mainSt_9.exits.append({"room" : quintenAve_0, "localName" : "north" })	

	carlAve_0.name = "Carl Avenue"
	carlAve_0.desc = ""
	carlAve_0.exits.append({"room" : carlAve_1, "localName" : "north" })
	carlAve_0.exits.append({"room" : mainSt_0, "localName" : "south" })

	carlAve_1.name = "Carl Avenue"
	carlAve_1.desc = ""
	carlAve_1.exits.append({"room" : carlAve_2, "localName" : "north" })
	carlAve_1.exits.append({"room" : carlAve_0, "localName" : "south" })
	carlAve_1.exits.append({"room" : mozenSt_0, "localName" : "east" })	

	carlAve_2.name = "Carl Avenue"
	carlAve_2.desc = ""
	carlAve_2.exits.append({"room" : carlAve_3, "localName" : "north" })
	carlAve_2.exits.append({"room" : carlAve_1, "localName" : "south" })

	carlAve_3.name = "Carl Avenue"
	carlAve_3.desc = ""
	carlAve_3.exits.append({"room" : carlAve_4, "localName" : "north east" })
	carlAve_3.exits.append({"room" : carlAve_2, "localName" : "south" })

	carlAve_4.name = "Carl Avenue"
	carlAve_4.desc = ""
	carlAve_4.exits.append({"room" : carlAve_3, "localName" : "south west" })
	carlAve_4.exits.append({"room" : terranceCrs_0, "localName" : "east" })	

	quintenAve_0.name = "Quinten Avenue"
	quintenAve_0.desc = ""
	quintenAve_0.exits.append({"room" : quintenAve_1, "localName" : "north" })
	quintenAve_0.exits.append({"room" : mainSt_9, "localName" : "south" })		

	quintenAve_1.name = "Quinten Avenue"
	quintenAve_1.desc = ""
	quintenAve_1.exits.append({"room" : quintenAve_2, "localName" : "north" })
	quintenAve_1.exits.append({"room" : quintenAve_0, "localName" : "south" })	

	quintenAve_2.name = "Quinten Avenue"
	quintenAve_2.desc = ""
	quintenAve_2.exits.append({"room" : quintenAve_3, "localName" : "north" })
	quintenAve_2.exits.append({"room" : quintenAve_1, "localName" : "south" })	
	quintenAve_2.exits.append({"room" : terentinoSt_2, "localName" : "west" })		

	quintenAve_3.name = "Quinten Avenue"
	quintenAve_3.desc = ""
	quintenAve_3.exits.append({"room" : terranceCrs_7, "localName" : "north west" })
	quintenAve_3.exits.append({"room" : quintenAve_2, "localName" : "south" })	

	terentinoSt_0.name = "Terentino Street"
	terentinoSt_0.desc = ""
	terentinoSt_0.exits.append({"room" : terentinoSt_1, "localName" : "east" })
	terentinoSt_0.exits.append({"room" : floydAve_2, "localName" : "west" })

	terentinoSt_1.name = "Terentino Street"
	terentinoSt_1.desc = ""
	terentinoSt_1.exits.append({"room" : terentinoSt_2, "localName" : "east" })
	terentinoSt_1.exits.append({"room" : terentinoSt_0, "localName" : "west" })	

	terentinoSt_2.name = "Terentino Street"
	terentinoSt_2.desc = ""
	terentinoSt_2.exits.append({"room" : quintenAve_2, "localName" : "east" })
	terentinoSt_2.exits.append({"room" : terentinoSt_1, "localName" : "west" })

	newtonAve_0.name = "Newton Avenue"
	newtonAve_0.desc = ""
	newtonAve_0.exits.append({"room" : mozenSt_2, "localName" : "north" })
	newtonAve_0.exits.append({"room" : mainSt_3, "localName" : "south" })

	mozenSt_0.name = "Mozen Street"
	mozenSt_0.desc = ""
	mozenSt_0.exits.append({"room" : mozenSt_1, "localName" : "east" })
	mozenSt_0.exits.append({"room" : carlAve_1, "localName" : "west" })	

	mozenSt_1.name = "Mozen Street"
	mozenSt_1.desc = ""
	mozenSt_1.exits.append({"room" : mozenSt_2, "localName" : "east" })
	mozenSt_1.exits.append({"room" : mozenSt_0, "localName" : "west" })		

	mozenSt_2.name = "Mozen Street"
	mozenSt_2.desc = ""
	mozenSt_2.exits.append({"room" : mozenSt_3, "localName" : "east" })
	mozenSt_2.exits.append({"room" : mozenSt_1, "localName" : "west" })	
	mozenSt_2.exits.append({"room" : newtonAve_0, "localName" : "south" })		

	mozenSt_3.name = "Mozen Street"
	mozenSt_3.desc = ""
	mozenSt_3.exits.append({"room" : floydAve_1, "localName" : "east" })
	mozenSt_3.exits.append({"room" : mozenSt_2, "localName" : "west" })	

	zirrilaSt_0.name = "Zirrila Street"
	zirrilaSt_0.desc = ""
	zirrilaSt_0.exits.append({"room" : zirrilaSt_1, "localName" : "east" })
	zirrilaSt_0.exits.append({"room" : terranceCrs_0, "localName" : "west" })

	zirrilaSt_1.name = "Zirrila Street"
	zirrilaSt_1.desc = ""
	zirrilaSt_1.exits.append({"room" : intfloydZirrila, "localName" : "east" })
	zirrilaSt_1.exits.append({"room" : zirrilaSt_0, "localName" : "west" })

	zirrilaSt_2.name = "Zirrila Street"
	zirrilaSt_2.desc = ""
	zirrilaSt_2.exits.append({"room" : zirrilaSt_3, "localName" : "east" })
	zirrilaSt_2.exits.append({"room" : intfloydZirrila, "localName" : "west" })

	zirrilaSt_3.name = "Zirrila Street"
	zirrilaSt_3.desc = ""
	zirrilaSt_3.exits.append({"room" : terranceCrs_7, "localName" : "east" })
	zirrilaSt_3.exits.append({"room" : zirrilaSt_2, "localName" : "west" })	

	monroeSt_0.name = "Monroe Street"
	monroeSt_0.desc = ""
	monroeSt_0.exits.append({"room" : monroeSt_1, "localName" : "east" })
	monroeSt_0.exits.append({"room" : terranceCrs_1, "localName" : "west" })

	monroeSt_1.name = "Monroe Street"
	monroeSt_1.desc = ""
	monroeSt_1.exits.append({"room" : monroeSt_2, "localName" : "east" })
	monroeSt_1.exits.append({"room" : monroeSt_0, "localName" : "west" })	

	monroeSt_2.name = "Monroe Street"
	monroeSt_2.desc = ""
	monroeSt_2.exits.append({"room" : monroeSt_3, "localName" : "east" })
	monroeSt_2.exits.append({"room" : monroeSt_1, "localName" : "west" })
	monroeSt_2.exits.append({"room" : intfloydZirrila, "localName" : "south" })	

	monroeSt_3.name = "Monroe Street"
	monroeSt_3.desc = ""
	monroeSt_3.exits.append({"room" : terranceCrs_6, "localName" : "east" })
	monroeSt_3.exits.append({"room" : monroeSt_2, "localName" : "west" })

	hardware_0.name = "Hardware Store"
	hardware_0.desc = ""
	hardware_0.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardware_0.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })
	hardware_0.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })	
	hardware_0.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardware_0.exits.append({"room" : hardwareWashroom_0, "localName" : "washroom" })	
	hardware_0.exits.append({"room" : hardwareCashierTill_0, "localName" : "cashier till" })
	hardwareAisle_0.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_0.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })	
	hardwareAisle_0.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareAisle_0.exits.append({"room" : hardwareWashroom_0, "localName" : "washroom" })	
	hardwareAisle_0.exits.append({"room" : hardwareCashierTill_0, "localName" : "cashier till" })
	hardwareAisle_1.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_1.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareAisle_1.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareAisle_1.exits.append({"room" : hardwareWashroom_0, "localName" : "washroom" })	
	hardwareAisle_1.exits.append({"room" : hardwareCashierTill_0, "localName" : "cashier till" })
	hardwareAisle_2.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_2.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareAisle_2.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareAisle_2.exits.append({"room" : hardwareWashroom_0, "localName" : "washroom" })	
	hardwareAisle_2.exits.append({"room" : hardwareCashierTill_0, "localName" : "cashier till" })
	hardwareWashroom_0.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareWashroom_0.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareWashroom_0.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareWashroom_0.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })	
	hardwareWashroom_0.exits.append({"room" : hardwareCashierTill_0, "localName" : "cashier till" })	
	hardwareCashierTill_0.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareCashierTill_0.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareCashierTill_0.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareCashierTill_0.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareCashierTill_0.exits.append({"room" : hardwareWashroom_0, "localName" : "washroom" })	

	zom0 = zombie.Zombie("zombie", 5, 1, "Brains....", world)
	zom1 = zombie.Zombie("super zombie", 20, 3, "He looks pretty tough.", world)

	if (int)(random.random()*2):
		hardwareAisle_1.items.append(items.Axe())
	else:
		hardwareWashroom_0.items.append(items.DumbAxe())

	if (int)(random.random()*2):
		floydAve_0.items.append(items.HealthPotion())
	else:
		floydAve_0.items.append(items.DeathJuice())

	if (int)(random.random()*2):
		quintenAve_2.npcs.append(zom0)
		world.remainingZombies += 1
	else: 
		mozenSt_0.npcs.append(zom1)
		world.remainingZombies += 1

	if (int)(random.random()*2):
		newtonAve_0.npcs.append(zom0)
		world.remainingZombies += 1
	else: 
		zirrilaSt_1.npcs.append(zom1)
		world.remainingZombies += 1

	if (int)(random.random()*2):
		carlAve_4.items.append(items.HammerTime())
	else:
		terranceCrs_7.items.append(items.Chainsaw())

	mainSt_7.npcs.append(zom1)

	world.rooms.append(terranceCrs_0)
	world.rooms.append(terranceCrs_1)
	world.rooms.append(terranceCrs_2)
	world.rooms.append(terranceCrs_3)
	world.rooms.append(terranceCrs_4)
	world.rooms.append(terranceCrs_5)
	world.rooms.append(terranceCrs_6)
	world.rooms.append(terranceCrs_7)
	world.rooms.append(floydAve_0)
	world.rooms.append(floydAve_1)
	world.rooms.append(floydAve_2)
	world.rooms.append(floydAve_3)
	world.rooms.append(intfloydZirrila)
	world.rooms.append(mainSt_0)
	world.rooms.append(mainSt_1)
	world.rooms.append(mainSt_2)
	world.rooms.append(mainSt_3)
	world.rooms.append(mainSt_4)
	world.rooms.append(mainSt_5)
	world.rooms.append(mainSt_6)
	world.rooms.append(mainSt_7)
	world.rooms.append(mainSt_8)
	world.rooms.append(mainSt_9)
	world.rooms.append(carlAve_0)
	world.rooms.append(carlAve_1)
	world.rooms.append(carlAve_2)
	world.rooms.append(carlAve_3)
	world.rooms.append(carlAve_4)
	world.rooms.append(quintenAve_0)
	world.rooms.append(quintenAve_1)
	world.rooms.append(quintenAve_2)
	world.rooms.append(quintenAve_3)
	world.rooms.append(terentinoSt_0)
	world.rooms.append(terentinoSt_1)
	world.rooms.append(terentinoSt_2)
	world.rooms.append(newtonAve_0)
	world.rooms.append(mozenSt_0)
	world.rooms.append(mozenSt_1)
	world.rooms.append(mozenSt_2)
	world.rooms.append(mozenSt_3)
	world.rooms.append(zirrilaSt_0)
	world.rooms.append(zirrilaSt_1)
	world.rooms.append(zirrilaSt_2)	
	world.rooms.append(zirrilaSt_3)
	world.rooms.append(monroeSt_0)
	world.rooms.append(monroeSt_1)	
	world.rooms.append(monroeSt_2)
	world.rooms.append(monroeSt_3)

	world.rooms.append(hardware_0)
	world.rooms.append(hardwareAisle_0)
	world.rooms.append(hardwareAisle_1)
	world.rooms.append(hardwareAisle_2)
	world.rooms.append(hardwareWashroom_0)
	world.rooms.append(hardwareCashierTill_0)

	world.curRoom = mainSt_0
