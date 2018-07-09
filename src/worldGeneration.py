import random

import npc
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

	hardware = Room()
	hardwareAisle_0 = Room()
	hardwareAisle_1 = Room()
	hardwareAisle_2 = Room()
	hardwareWashroom = Room()
	hardwareCashierTill = Room()

	gasStation = Room()
	gasStationCashierTill = Room()
	gasStationWashroom = Room()
	gasStationShop = Room()
	gasStationPumps = Room()

	restaurant = Room()
	restaurantTables = Room()
	restaurantKitchen = Room()
	restaurantWashroom = Room()
	restaurantCashierTill = Room()

	hotel = Room()
	hotelRoom_0 = Room()
	hotelRoom_1 = Room()
	hotelRoom_2 = Room()
	hotelLobby = Room()
	hotelWashroom = Room()
	hotelCashierTill = Room()
	hotelStairs = Room()
	hotelRoom_3 = Room()
	hotelRoom_4 = Room()
	hotelRoom_5 = Room()

	townHall = Room()
	townHallLobby = Room()
	townHallWashroom = Room()
	townHallOffice = Room()
	townHallMeetingRoom = Room()

	park = Room()
	parkPlayGround = Room()
	parkFields = Room()
	parkPicnicTables = Room()
	parkWaterPark = Room()
	parkMaintanceHouse = Room()

	school = Room()
	schoolClassroom_0 = Room()
	schoolClassroom_1 = Room()
	schoolClassroom_2 = Room()
	schoolClassroom_3 = Room()
	schoolOffice = Room()
	schoolGym = Room()
	schoolWashroom = Room()
	schoolComputerRoom = Room()

	pharmacy = Room()
	pharmacyCashierTill = Room()
	pharmacyStorage = Room()
	pharmacyAisles = Room()
	pharmacyCooler = Room()
	pharmacyWashroom = Room()

	house_0 = Room()
	house_0LivingRoom = Room()
	house_0Kitchen = Room()
	house_0Washroom = Room()
	house_0Garage = Room()
	house_0Bedroom = Room()
	house_0Basement = Room()

	house_1 = Room()
	house_1LivingRoom = Room()
	house_1Kitchen = Room()
	house_1Washroom_0 = Room()
	house_1Garage = Room()
	house_1Bedroom_0 = Room()
	house_1Basement = Room()
	house_1Stairs = Room()
	house_1Bedroom_1 = Room()
	house_1Bedroom_2 = Room()
	house_1Washroom_1 = Room()
	house_1RecreationRoom = Room()

	terranceCrs_0.name = "Terrance Crescent"
	terranceCrs_0.desc = ""
	terranceCrs_0.exits.append({"room" : terranceCrs_1, "localName" : "north" })
	terranceCrs_0.exits.append({"room" : carlAve_4, "localName" : "west" })
	terranceCrs_0.exits.append({"room" : zirrilaSt_0, "localName" : "east" })
	terranceCrs_0.exits.append({"room" : park, "localName" : "Park" })

	terranceCrs_1.name = "Terrance Crescent"
	terranceCrs_1.desc = ""
	terranceCrs_1.exits.append({"room" : terranceCrs_2, "localName" : "northeast" })
	terranceCrs_1.exits.append({"room" : terranceCrs_0, "localName" : "south" })	
	terranceCrs_1.exits.append({"room" : monroeSt_0, "localName" : "east" })

	terranceCrs_2.name = "Terrance Crescent"
	terranceCrs_2.desc = ""
	terranceCrs_2.exits.append({"room" : terranceCrs_3, "localName" : "east" })
	terranceCrs_2.exits.append({"room" : terranceCrs_1, "localName" : "southwest" })	

	terranceCrs_3.name = "Terrance Crescent"
	terranceCrs_3.desc = ""
	terranceCrs_3.exits.append({"room" : terranceCrs_4, "localName" : "east" })
	terranceCrs_3.exits.append({"room" : terranceCrs_2, "localName" : "west" })	
	terranceCrs_3.exits.append({"room" : house_1, "localName" : "House 383" })		

	terranceCrs_4.name = "Terrance Crescent"
	terranceCrs_4.desc = ""
	terranceCrs_4.exits.append({"room" : terranceCrs_5, "localName" : "east" })
	terranceCrs_4.exits.append({"room" : terranceCrs_3, "localName" : "west" })

	terranceCrs_5.name = "Terrance Crescent"
	terranceCrs_5.desc = ""
	terranceCrs_5.exits.append({"room" : terranceCrs_6, "localName" : "southeast" })
	terranceCrs_5.exits.append({"room" : terranceCrs_4, "localName" : "west" })

	terranceCrs_6.name = "Terrance Crescent"
	terranceCrs_6.desc = ""
	terranceCrs_6.exits.append({"room" : terranceCrs_7, "localName" : "southeast" })
	terranceCrs_6.exits.append({"room" : terranceCrs_5, "localName" : "northwest" })	
	terranceCrs_6.exits.append({"room" : monroeSt_3, "localName" : "west" })

	terranceCrs_7.name = "Terrance Crescent"
	terranceCrs_7.desc = ""
	terranceCrs_7.exits.append({"room" : quintenAve_3, "localName" : "southeast" })
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
	floydAve_3.exits.append({"room" : school, "localName" : "School" })

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
	mainSt_2.exits.append({"room" : restaurant, "localName" : "Restaurant" })	

	mainSt_3.name = "Main Street"
	mainSt_3.desc = ""
	mainSt_3.exits.append({"room" : mainSt_4, "localName" : "east" })
	mainSt_3.exits.append({"room" : mainSt_2, "localName" : "west" })
	mainSt_3.exits.append({"room" : newtonAve_0, "localName" : "north" })		

	mainSt_4.name = "Main Street"
	mainSt_4.desc = ""
	mainSt_4.exits.append({"room" : mainSt_5, "localName" : "east" })
	mainSt_4.exits.append({"room" : mainSt_3, "localName" : "west" })
	mainSt_4.exits.append({"room" : hotel, "localName" : "Hotel" })

	mainSt_5.name = "Main Street"
	mainSt_5.desc = ""
	mainSt_5.exits.append({"room" : mainSt_6, "localName" : "east" })
	mainSt_5.exits.append({"room" : mainSt_4, "localName" : "west" })
	mainSt_5.exits.append({"room" : floydAve_0, "localName" : "north" })	

	mainSt_6.name = "Main Street"
	mainSt_6.desc = ""
	mainSt_6.exits.append({"room" : mainSt_7, "localName" : "east" })
	mainSt_6.exits.append({"room" : mainSt_5, "localName" : "west" })
	mainSt_6.exits.append({"room" : gasStation, "localName" : "Gas Station" })

	mainSt_7.name = "Main Street"
	mainSt_7.desc = ""
	mainSt_7.exits.append({"room" : mainSt_8, "localName" : "east" })
	mainSt_7.exits.append({"room" : mainSt_6, "localName" : "west" })

	mainSt_8.name = "Main Street"
	mainSt_8.desc = ""
	mainSt_8.exits.append({"room" : mainSt_9, "localName" : "east" })
	mainSt_8.exits.append({"room" : mainSt_7, "localName" : "west" })
	mainSt_8.exits.append({"room" : hardware, "localName" : "Hardware Store" })	

	mainSt_9.name = "Main Street"
	mainSt_9.desc = ""
	mainSt_9.exits.append({"room" : mainSt_8, "localName" : "west" })
	mainSt_9.exits.append({"room" : quintenAve_0, "localName" : "north" })	

	carlAve_0.name = "Carl Avenue"
	carlAve_0.desc = ""
	carlAve_0.exits.append({"room" : carlAve_1, "localName" : "north" })
	carlAve_0.exits.append({"room" : mainSt_0, "localName" : "south" })
	carlAve_0.exits.append({"room" : pharmacy, "localName" : "Pharmacy" })

	carlAve_1.name = "Carl Avenue"
	carlAve_1.desc = ""
	carlAve_1.exits.append({"room" : carlAve_2, "localName" : "north" })
	carlAve_1.exits.append({"room" : carlAve_0, "localName" : "south" })
	carlAve_1.exits.append({"room" : mozenSt_0, "localName" : "east" })	

	carlAve_2.name = "Carl Avenue"
	carlAve_2.desc = ""
	carlAve_2.exits.append({"room" : carlAve_3, "localName" : "north" })
	carlAve_2.exits.append({"room" : carlAve_1, "localName" : "south" })
	carlAve_2.exits.append({"room" : park, "localName" : "Park" })

	carlAve_3.name = "Carl Avenue"
	carlAve_3.desc = ""
	carlAve_3.exits.append({"room" : carlAve_4, "localName" : "northeast" })
	carlAve_3.exits.append({"room" : carlAve_2, "localName" : "south" })

	carlAve_4.name = "Carl Avenue"
	carlAve_4.desc = ""
	carlAve_4.exits.append({"room" : carlAve_3, "localName" : "southwest" })
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
	quintenAve_3.exits.append({"room" : terranceCrs_7, "localName" : "northwest" })
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
	mozenSt_0.exits.append({"room" : park, "localName" : "Park" })	

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
	mozenSt_3.exits.append({"room" : townHall, "localName" : "Town Hall" })

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
	monroeSt_1.exits.append({"room" : house_0, "localName" : "House 502" })

	monroeSt_2.name = "Monroe Street"
	monroeSt_2.desc = ""
	monroeSt_2.exits.append({"room" : monroeSt_3, "localName" : "east" })
	monroeSt_2.exits.append({"room" : monroeSt_1, "localName" : "west" })
	monroeSt_2.exits.append({"room" : intfloydZirrila, "localName" : "south" })	

	monroeSt_3.name = "Monroe Street"
	monroeSt_3.desc = ""
	monroeSt_3.exits.append({"room" : terranceCrs_6, "localName" : "east" })
	monroeSt_3.exits.append({"room" : monroeSt_2, "localName" : "west" })

	hardware.name = "Hardware Store"
	hardware.desc = ""
	hardware.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardware.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })
	hardware.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })	
	hardware.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardware.exits.append({"room" : hardwareWashroom, "localName" : "washroom" })	
	hardware.exits.append({"room" : hardwareCashierTill, "localName" : "cashier till" })
	hardwareAisle_0.name = "Hardware Store - aisle 1"
	hardwareAisle_0.desc = ""
	hardwareAisle_0.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_0.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })	
	hardwareAisle_0.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareAisle_0.exits.append({"room" : hardwareWashroom, "localName" : "washroom" })	
	hardwareAisle_0.exits.append({"room" : hardwareCashierTill, "localName" : "cashier till" })
	hardwareAisle_1.name = "Hardware Store - aisle 2"
	hardwareAisle_1.desc = ""
	hardwareAisle_1.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_1.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareAisle_1.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareAisle_1.exits.append({"room" : hardwareWashroom, "localName" : "washroom" })	
	hardwareAisle_1.exits.append({"room" : hardwareCashierTill, "localName" : "cashier till" })
	hardwareAisle_2.name = "Hardware Store - aisle 3"
	hardwareAisle_2.desc = ""
	hardwareAisle_2.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareAisle_2.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareAisle_2.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareAisle_2.exits.append({"room" : hardwareWashroom, "localName" : "washroom" })	
	hardwareAisle_2.exits.append({"room" : hardwareCashierTill, "localName" : "cashier till" })
	hardwareWashroom.name = "Hardware Store - washroom"
	hardwareWashroom.desc = ""
	hardwareWashroom.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareWashroom.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareWashroom.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareWashroom.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })	
	hardwareWashroom.exits.append({"room" : hardwareCashierTill, "localName" : "cashier till" })
	hardwareCashierTill.name = "Hardware Store - cashier till"
	hardwareCashierTill.desc = ""
	hardwareCashierTill.exits.append({"room" : mainSt_8, "localName" : "front door" })
	hardwareCashierTill.exits.append({"room" : hardwareAisle_0, "localName" : "aisle 1" })	
	hardwareCashierTill.exits.append({"room" : hardwareAisle_1, "localName" : "aisle 2" })
	hardwareCashierTill.exits.append({"room" : hardwareAisle_2, "localName" : "aisle 3" })
	hardwareCashierTill.exits.append({"room" : hardwareWashroom, "localName" : "washroom" })

	gasStation.name = "Gas Station"
	gasStation.desc = ""
	gasStation.exits.append({"room" : mainSt_6, "localName" : "front door" })
	gasStation.exits.append({"room" : gasStationCashierTill, "localName" : "cashier till" })	
	gasStation.exits.append({"room" : gasStationWashroom, "localName" : "washroom" })
	gasStation.exits.append({"room" : gasStationShop, "localName" : "shop" })
	gasStation.exits.append({"room" : gasStationPumps, "localName" : "pumps" })
	gasStationCashierTill.name = "Gas Station - cashier"
	gasStationCashierTill.desc = ""
	gasStationCashierTill.exits.append({"room" : mainSt_6, "localName" : "front door" })
	gasStationCashierTill.exits.append({"room" : gasStationWashroom, "localName" : "washroom" })
	gasStationCashierTill.exits.append({"room" : gasStationShop, "localName" : "shop" })
	gasStationCashierTill.exits.append({"room" : gasStationPumps, "localName" : "pumps" })
	gasStationWashroom.name = "Gas Station - washroom"
	gasStationWashroom.desc = ""
	gasStationWashroom.exits.append({"room" : mainSt_6, "localName" : "front door" })
	gasStationWashroom.exits.append({"room" : gasStationCashierTill, "localName" : "cashier till" })	
	gasStationWashroom.exits.append({"room" : gasStationShop, "localName" : "shop" })
	gasStationWashroom.exits.append({"room" : gasStationPumps, "localName" : "pumps" })
	gasStationShop.name = "Gas Station - shop"
	gasStationShop.desc = ""
	gasStationShop.exits.append({"room" : mainSt_6, "localName" : "front door" })
	gasStationShop.exits.append({"room" : gasStationCashierTill, "localName" : "cashier till" })	
	gasStationShop.exits.append({"room" : gasStationWashroom, "localName" : "washroom" })
	gasStationShop.exits.append({"room" : gasStationPumps, "localName" : "pumps" })	
	gasStationPumps.name = "Gas Station - pumps"
	gasStationPumps.desc = ""
	gasStationPumps.exits.append({"room" : mainSt_6, "localName" : "front door" })
	gasStationPumps.exits.append({"room" : gasStationCashierTill, "localName" : "cashier till" })	
	gasStationPumps.exits.append({"room" : gasStationWashroom, "localName" : "washroom" })
	gasStationPumps.exits.append({"room" : gasStationShop, "localName" : "shop" })

	restaurant.name = "Restaurant"
	restaurant.desc = ""
	restaurant.exits.append({"room" : mainSt_2, "localName" : "front door" })
	restaurant.exits.append({"room" : restaurantTables, "localName" : "tables" })	
	restaurant.exits.append({"room" : restaurantKitchen, "localName" : "kitchen" })
	restaurant.exits.append({"room" : restaurantWashroom, "localName" : "washroom" })
	restaurant.exits.append({"room" : restaurantCashierTill, "localName" : "cashier till" })
	restaurantTables.name = "Restaurant - tables"
	restaurantTables.desc = ""
	restaurantTables.exits.append({"room" : mainSt_2, "localName" : "front door" })
	restaurantTables.exits.append({"room" : restaurantCashierTill, "localName" : "cashier till" })
	restaurantTables.exits.append({"room" : restaurantKitchen, "localName" : "kitchen" })
	restaurantTables.exits.append({"room" : restaurantWashroom, "localName" : "washroom" })
	restaurantKitchen.name = "Restaurant - kitchen"
	restaurantKitchen.desc = ""
	restaurantKitchen.exits.append({"room" : mainSt_2, "localName" : "front door" })
	restaurantKitchen.exits.append({"room" : restaurantTables, "localName" : "tables" })	
	restaurantKitchen.exits.append({"room" : restaurantCashierTill, "localName" : "cashier till" })
	restaurantKitchen.exits.append({"room" : restaurantWashroom, "localName" : "washroom" })
	restaurantWashroom.name = "Restaurant - washroom"
	restaurantWashroom.desc = ""
	restaurantWashroom.exits.append({"room" : mainSt_2, "localName" : "front door" })
	restaurantWashroom.exits.append({"room" : restaurantTables, "localName" : "tables" })	
	restaurantWashroom.exits.append({"room" : restaurantCashierTill, "localName" : "cashier till" })
	restaurantWashroom.exits.append({"room" : restaurantKitchen, "localName" : "kitchen" })	
	restaurantCashierTill.name = "Restaurant - till"
	restaurantCashierTill.desc = ""
	restaurantCashierTill.exits.append({"room" : mainSt_2, "localName" : "front door" })
	restaurantCashierTill.exits.append({"room" : restaurantTables, "localName" : "tables" })	
	restaurantCashierTill.exits.append({"room" : restaurantKitchen, "localName" : "kitchen" })
	restaurantCashierTill.exits.append({"room" : restaurantWashroom, "localName" : "washroom" })

	hotel.name = "Hotel"
	hotel.desc = ""
	hotel.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotel.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotel.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotel.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotel.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotel.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotel.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotel.exits.append({"room" : hotelStairs, "localName" : "stairs" })	
	hotelRoom_0.name = "Hotel - room 11"
	hotelRoom_0.desc = ""
	hotelRoom_0.exits.append({"room" : mainSt_4, "localName" : "front door" })	
	hotelRoom_0.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotelRoom_0.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotelRoom_0.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotelRoom_0.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotelRoom_0.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotelRoom_0.exits.append({"room" : hotelStairs, "localName" : "stairs" })
	hotelRoom_1.name = "Hotel - room 12"
	hotelRoom_1.desc = ""	
	hotelRoom_1.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotelRoom_1.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotelRoom_1.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotelRoom_1.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotelRoom_1.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotelRoom_1.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotelRoom_1.exits.append({"room" : hotelStairs, "localName" : "stairs" })
	hotelRoom_2.name = "Hotel - room 13"
	hotelRoom_2.desc = ""	
	hotelRoom_2.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotelRoom_2.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotelRoom_2.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotelRoom_2.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotelRoom_2.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotelRoom_2.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotelRoom_2.exits.append({"room" : hotelStairs, "localName" : "stairs" })
	hotelLobby.name = "Hotel - lobby"
	hotelLobby.desc = ""	
	hotelLobby.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotelLobby.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotelLobby.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotelLobby.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotelLobby.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotelLobby.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotelLobby.exits.append({"room" : hotelStairs, "localName" : "stairs" })	
	hotelWashroom.name = "Hotel - washroom"
	hotelWashroom.desc = ""
	hotelWashroom.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotelWashroom.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotelWashroom.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotelWashroom.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotelWashroom.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotelWashroom.exits.append({"room" : hotelCashierTill, "localName" : "cashier till" })
	hotelWashroom.exits.append({"room" : hotelStairs, "localName" : "stairs" })	
	hotelCashierTill.name = "Hotel - cashier till"
	hotelCashierTill.desc = ""
	hotelCashierTill.exits.append({"room" : mainSt_4, "localName" : "front door" })
	hotelCashierTill.exits.append({"room" : hotelRoom_0, "localName" : "room 11" })	
	hotelCashierTill.exits.append({"room" : hotelRoom_1, "localName" : "room 12" })
	hotelCashierTill.exits.append({"room" : hotelRoom_2, "localName" : "room 13" })
	hotelCashierTill.exits.append({"room" : hotelLobby, "localName" : "lobby" })
	hotelCashierTill.exits.append({"room" : hotelWashroom, "localName" : "washroom" })
	hotelCashierTill.exits.append({"room" : hotelStairs, "localName" : "stairs" })
	hotelStairs.name = "Hotel - top floor"
	hotelStairs.desc = ""	
	hotelStairs.exits.append({"room" : hotel, "localName" : "down stairs" })	
	hotelStairs.exits.append({"room" : hotelRoom_3, "localName" : "room 21" })
	hotelStairs.exits.append({"room" : hotelRoom_4, "localName" : "room 22" })
	hotelStairs.exits.append({"room" : hotelRoom_5, "localName" : "room 23" })
	hotelRoom_3.name = "Hotel - room 21"
	hotelRoom_3.desc = ""
	hotelRoom_3.exits.append({"room" : hotel, "localName" : "down stairs" })	
	hotelRoom_3.exits.append({"room" : hotelRoom_4, "localName" : "room 22" })
	hotelRoom_3.exits.append({"room" : hotelRoom_5, "localName" : "room 23" })
	hotelRoom_4.name = "Hotel - room 22"
	hotelRoom_4.desc = ""
	hotelRoom_4.exits.append({"room" : hotel, "localName" : "down stairs" })
	hotelRoom_4.exits.append({"room" : hotelRoom_3, "localName" : "room 21" })
	hotelRoom_4.exits.append({"room" : hotelRoom_5, "localName" : "room 23" })
	hotelRoom_5.name = "Hotel - room 23"
	hotelRoom_5.desc = ""
	hotelRoom_5.exits.append({"room" : hotel, "localName" : "down stairs" })
	hotelRoom_5.exits.append({"room" : hotelRoom_3, "localName" : "room 21" })
	hotelRoom_5.exits.append({"room" : hotelRoom_4, "localName" : "room 22" })
	
	townHall.name = "Town Hall"
	townHall.desc = ""
	townHall.exits.append({"room" : mozenSt_3, "localName" : "front door" })
	townHall.exits.append({"room" : townHallLobby, "localName" : "lobby" })
	townHall.exits.append({"room" : townHallWashroom, "localName" : "washroom" })
	townHall.exits.append({"room" : townHallOffice, "localName" : "office" })
	townHall.exits.append({"room" : townHallMeetingRoom, "localName" : "meeting room" })
	townHallLobby.name = "Town Hall - lobby"
	townHallLobby.desc = ""
	townHallLobby.exits.append({"room" : mozenSt_3, "localName" : "front door" })
	townHallLobby.exits.append({"room" : townHallWashroom, "localName" : "washroom" })
	townHallLobby.exits.append({"room" : townHallOffice, "localName" : "office" })
	townHallLobby.exits.append({"room" : townHallMeetingRoom, "localName" : "meeting room" })
	townHallWashroom.name = "Town Hall - washroom"
	townHallWashroom.desc = ""
	townHallWashroom.exits.append({"room" : mozenSt_3, "localName" : "front door" })
	townHallWashroom.exits.append({"room" : townHallLobby, "localName" : "lobby" })
	townHallWashroom.exits.append({"room" : townHallOffice, "localName" : "office" })
	townHallWashroom.exits.append({"room" : townHallMeetingRoom, "localName" : "meeting room" })
	townHallOffice.name = "Town Hall - office"
	townHallOffice.desc = ""
	townHallOffice.exits.append({"room" : mozenSt_3, "localName" : "front door" })
	townHallOffice.exits.append({"room" : townHallLobby, "localName" : "lobby" })
	townHallOffice.exits.append({"room" : townHallWashroom, "localName" : "washroom" })
	townHallOffice.exits.append({"room" : townHallMeetingRoom, "localName" : "meeting room" })
	townHallMeetingRoom.name = "Town Hall - meeting room"
	townHallMeetingRoom.desc = ""
	townHallMeetingRoom.exits.append({"room" : mozenSt_3, "localName" : "front door" })
	townHallMeetingRoom.exits.append({"room" : townHallLobby, "localName" : "lobby" })
	townHallMeetingRoom.exits.append({"room" : townHallWashroom, "localName" : "washroom" })
	townHallMeetingRoom.exits.append({"room" : townHallOffice, "localName" : "office" })

	park.name = "Park"
	park.desc = ""
	park.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })
	park.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	park.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	park.exits.append({"room" : parkPlayGround, "localName" : "playground" })
	park.exits.append({"room" : parkFields, "localName" : "field" })
	park.exits.append({"room" : parkPicnicTables, "localName" : "picnic tables" })
	park.exits.append({"room" : parkWaterPark, "localName" : "water park" })
	park.exits.append({"room" : parkMaintanceHouse, "localName" : "maintance house" })
	parkPlayGround.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })    
	parkPlayGround.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	parkPlayGround.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	parkPlayGround.exits.append({"room" : parkFields, "localName" : "field" })
	parkPlayGround.exits.append({"room" : parkPicnicTables, "localName" : "picnic tables" })
	parkPlayGround.exits.append({"room" : parkWaterPark, "localName" : "water park" })
	parkPlayGround.exits.append({"room" : parkMaintanceHouse, "localName" : "maintance house" })
	parkFields.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })    
	parkFields.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	parkFields.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	parkFields.exits.append({"room" : parkPlayGround, "localName" : "playground" })
	parkFields.exits.append({"room" : parkPicnicTables, "localName" : "picnic tables" })
	parkFields.exits.append({"room" : parkWaterPark, "localName" : "water park" })
	parkFields.exits.append({"room" : parkMaintanceHouse, "localName" : "maintance house" })
	parkPicnicTables.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })    
	parkPicnicTables.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	parkPicnicTables.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	parkPicnicTables.exits.append({"room" : parkPlayGround, "localName" : "playground" })
	parkPicnicTables.exits.append({"room" : parkFields, "localName" : "field" })
	parkPicnicTables.exits.append({"room" : parkWaterPark, "localName" : "water park" })
	parkPicnicTables.exits.append({"room" : parkMaintanceHouse, "localName" : "maintance house" })
	parkWaterPark.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })    
	parkWaterPark.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	parkWaterPark.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	parkWaterPark.exits.append({"room" : parkPlayGround, "localName" : "playground" })
	parkWaterPark.exits.append({"room" : parkFields, "localName" : "field" })
	parkWaterPark.exits.append({"room" : parkPicnicTables, "localName" : "picnic tables" })
	parkWaterPark.exits.append({"room" : parkMaintanceHouse, "localName" : "maintance house" })
	parkMaintanceHouse.exits.append({"room" : mozenSt_0, "localName" : "Mozen Street" })    
	parkMaintanceHouse.exits.append({"room" : carlAve_2, "localName" : "Carl Avenue" })
	parkMaintanceHouse.exits.append({"room" : terranceCrs_0, "localName" : "Terrance Crescent" })
	parkMaintanceHouse.exits.append({"room" : parkPlayGround, "localName" : "playground" })
	parkMaintanceHouse.exits.append({"room" : parkFields, "localName" : "field" })
	parkMaintanceHouse.exits.append({"room" : parkPicnicTables, "localName" : "picnic tables" })
	parkMaintanceHouse.exits.append({"room" : parkWaterPark, "localName" : "water park" })

	school.name = "School"
	school.desc = ""
	school.exits.append({"room" : floydAve_3, "localName" : "front door"})
	school.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	school.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	school.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	school.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	school.exits.append({"room" : schoolOffice, "localName" : "office" })
	school.exits.append({"room" : schoolGym, "localName" : "gym" })
	school.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	school.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolClassroom_0.exits.append({"room" : floydAve_3, "localName" : "front door"})  
	schoolClassroom_0.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolClassroom_0.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolClassroom_0.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolClassroom_0.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolClassroom_0.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolClassroom_0.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolClassroom_0.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolClassroom_1.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolClassroom_1.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolClassroom_1.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolClassroom_1.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolClassroom_1.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolClassroom_1.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolClassroom_1.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolClassroom_1.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolClassroom_2.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolClassroom_2.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolClassroom_2.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolClassroom_2.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolClassroom_2.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolClassroom_2.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolClassroom_2.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolClassroom_2.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolClassroom_3.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolClassroom_3.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolClassroom_3.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolClassroom_3.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolClassroom_3.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolClassroom_3.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolClassroom_3.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolClassroom_3.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolOffice.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolOffice.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolOffice.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolOffice.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolOffice.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolOffice.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolOffice.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolOffice.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolGym.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolGym.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolGym.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolGym.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolGym.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolGym.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolGym.exits.append({"room" : schoolWashroom, "localName" : "washroom" })
	schoolGym.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })	
	schoolWashroom.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolWashroom.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolWashroom.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolWashroom.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolWashroom.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolWashroom.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolWashroom.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolWashroom.exits.append({"room" : schoolComputerRoom, "localName" : "computer room" })
	schoolComputerRoom.exits.append({"room" : floydAve_3, "localName" : "front door"})
	schoolComputerRoom.exits.append({"room" : schoolClassroom_0, "localName" : "classroom A" })    
	schoolComputerRoom.exits.append({"room" : schoolClassroom_1, "localName" : "classroom B" })
	schoolComputerRoom.exits.append({"room" : schoolClassroom_2, "localName" : "classroom C" })
	schoolComputerRoom.exits.append({"room" : schoolClassroom_3, "localName" : "classroom D" })
	schoolComputerRoom.exits.append({"room" : schoolOffice, "localName" : "office" })
	schoolComputerRoom.exits.append({"room" : schoolGym, "localName" : "gym" })
	schoolComputerRoom.exits.append({"room" : schoolWashroom, "localName" : "washroom" })

	pharmacy.name = "Pharmacy"
	pharmacy.desc = ""
	pharmacy.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacy.exits.append({"room" : pharmacyCashierTill, "localName" : "cashier till" })    
	pharmacy.exits.append({"room" : pharmacyStorage, "localName" : "storage" })
	pharmacy.exits.append({"room" : pharmacyAisles, "localName" : "aisles" })
	pharmacy.exits.append({"room" : pharmacyCooler, "localName" : "cooler" })
	pharmacy.exits.append({"room" : pharmacyWashroom, "localName" : "washroom" })
	pharmacyCashierTill.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacyCashierTill.exits.append({"room" : pharmacyStorage, "localName" : "storage" })
	pharmacyCashierTill.exits.append({"room" : pharmacyAisles, "localName" : "aisles" })
	pharmacyCashierTill.exits.append({"room" : pharmacyCooler, "localName" : "cooler" })
	pharmacyCashierTill.exits.append({"room" : pharmacyWashroom, "localName" : "washroom" })
	pharmacyStorage.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacyStorage.exits.append({"room" : pharmacyCashierTill, "localName" : "cashier till" })    
	pharmacyStorage.exits.append({"room" : pharmacyAisles, "localName" : "aisles" })
	pharmacyStorage.exits.append({"room" : pharmacyCooler, "localName" : "cooler" })
	pharmacyStorage.exits.append({"room" : pharmacyWashroom, "localName" : "washroom" })
	pharmacyAisles.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacyAisles.exits.append({"room" : pharmacyCashierTill, "localName" : "cashier till" })    
	pharmacyAisles.exits.append({"room" : pharmacyStorage, "localName" : "storage" })
	pharmacyAisles.exits.append({"room" : pharmacyCooler, "localName" : "cooler" })
	pharmacyAisles.exits.append({"room" : pharmacyWashroom, "localName" : "washroom" })
	pharmacyCooler.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacyCooler.exits.append({"room" : pharmacyCashierTill, "localName" : "cashier till" })    
	pharmacyCooler.exits.append({"room" : pharmacyStorage, "localName" : "storage" })
	pharmacyCooler.exits.append({"room" : pharmacyAisles, "localName" : "aisles" })
	pharmacyCooler.exits.append({"room" : pharmacyWashroom, "localName" : "washroom" })
	pharmacyWashroom.exits.append({"room" : carlAve_0, "localName" : "front door"})
	pharmacyWashroom.exits.append({"room" : pharmacyCashierTill, "localName" : "cashier till" })    
	pharmacyWashroom.exits.append({"room" : pharmacyStorage, "localName" : "storage" })
	pharmacyWashroom.exits.append({"room" : pharmacyAisles, "localName" : "aisles" })
	pharmacyWashroom.exits.append({"room" : pharmacyCooler, "localName" : "cooler" })

	house_0.name = "House 502"
	house_0.desc = ""
	house_0.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })
	house_0.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0LivingRoom.exits.append({"room" : floydAve_3, "localName" : "front door"})  
	house_0LivingRoom.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0LivingRoom.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0LivingRoom.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0LivingRoom.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })
	house_0LivingRoom.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0Kitchen.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0Kitchen.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0Kitchen.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0Kitchen.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0Kitchen.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })
	house_0Kitchen.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0Washroom.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0Washroom.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0Washroom.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0Washroom.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0Washroom.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })
	house_0Washroom.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0Garage.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0Garage.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0Garage.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0Garage.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0Garage.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })
	house_0Garage.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0Bedroom.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0Bedroom.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0Bedroom.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0Bedroom.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0Bedroom.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0Bedroom.exits.append({"room" : house_0Basement, "localName" : "basement" })
	house_0Basement.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_0Basement.exits.append({"room" : house_0LivingRoom, "localName" : "living room" })    
	house_0Basement.exits.append({"room" : house_0Kitchen, "localName" : "kitchen" })
	house_0Basement.exits.append({"room" : house_0Washroom, "localName" : "washroom" })
	house_0Basement.exits.append({"room" : house_0Garage, "localName" : "garage" })
	house_0Basement.exits.append({"room" : house_0Bedroom, "localName" : "bedroom" })

	house_1.name = "House 383"
	house_1.desc = ""
	house_1.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_1.exits.append({"room" : house_1LivingRoom, "localName" : "living room" })    
	house_1.exits.append({"room" : house_1Kitchen, "localName" : "kitchen" })
	house_1.exits.append({"room" : house_1Washroom_0, "localName" : "washroom" })
	house_1.exits.append({"room" : house_1Garage, "localName" : "garage" })
	house_1.exits.append({"room" : house_1Bedroom_0, "localName" : "bedroom" })
	house_1.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1LivingRoom.exits.append({"room" : floydAve_3, "localName" : "front door"})   
	house_1LivingRoom.exits.append({"room" : house_1Kitchen, "localName" : "kitchen" })
	house_1LivingRoom.exits.append({"room" : house_1Washroom_0, "localName" : "washroom" })
	house_1LivingRoom.exits.append({"room" : house_1Garage, "localName" : "garage" })
	house_1LivingRoom.exits.append({"room" : house_1Bedroom_0, "localName" : "bedroom" })
	house_1LivingRoom.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1LivingRoom.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1Kitchen.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_1Kitchen.exits.append({"room" : house_1LivingRoom, "localName" : "living room" })    
	house_1Kitchen.exits.append({"room" : house_1Washroom_0, "localName" : "washroom" })
	house_1Kitchen.exits.append({"room" : house_1Garage, "localName" : "garage" })
	house_1Kitchen.exits.append({"room" : house_1Bedroom_0, "localName" : "bedroom" })
	house_1Kitchen.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1Kitchen.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1Washroom_0.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_1Washroom_0.exits.append({"room" : house_1LivingRoom, "localName" : "living room" })    
	house_1Washroom_0.exits.append({"room" : house_1Kitchen, "localName" : "kitchen" })
	house_1Washroom_0.exits.append({"room" : house_1Garage, "localName" : "garage" })
	house_1Washroom_0.exits.append({"room" : house_1Bedroom_0, "localName" : "bedroom" })
	house_1Washroom_0.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1Washroom_0.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1Garage.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_1Garage.exits.append({"room" : house_1LivingRoom, "localName" : "living room" })    
	house_1Garage.exits.append({"room" : house_1Kitchen, "localName" : "kitchen" })
	house_1Garage.exits.append({"room" : house_1Washroom_0, "localName" : "washroom" })
	house_1Garage.exits.append({"room" : house_1Bedroom_0, "localName" : "bedroom" })
	house_1Garage.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1Garage.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1.exits.append({"room" : floydAve_3, "localName" : "front door"})
	house_1Bedroom_0.exits.append({"room" : house_1LivingRoom, "localName" : "living room" })    
	house_1Bedroom_0.exits.append({"room" : house_1Kitchen, "localName" : "kitchen" })
	house_1Bedroom_0.exits.append({"room" : house_1Washroom_0, "localName" : "washroom" })
	house_1Bedroom_0.exits.append({"room" : house_1Garage, "localName" : "garage" })
	house_1Bedroom_0.exits.append({"room" : house_1Basement, "localName" : "basement" })
	house_1Bedroom_0.exits.append({"room" : house_1Stairs, "localName" : "stairs" })
	house_1Basement.exits.append({"room" : house_1, "localName" : "up stairs" })
	house_1Stairs.exits.append({"room" : house_1, "localName" : "down stairs" })
	house_1Stairs.exits.append({"room" : house_1Bedroom_1, "localName" : "Braden's room" })
	house_1Stairs.exits.append({"room" : house_1Bedroom_2, "localName" : "Bedroom"}) 
	house_1Stairs.exits.append({"room" : house_1Washroom_1, "localName" : "washroom"}) 
	house_1Stairs.exits.append({"room" : house_1RecreationRoom, "localName" : "rec room"})
	house_1Bedroom_1.exits.append({"room" : house_1, "localName" : "down stairs" })
	house_1Bedroom_1.exits.append({"room" : house_1Bedroom_2, "localName" : "Bedroom"}) 
	house_1Bedroom_1.exits.append({"room" : house_1Washroom_1, "localName" : "washroom"}) 
	house_1Bedroom_1.exits.append({"room" : house_1RecreationRoom, "localName" : "rec room"})
	house_1Bedroom_2.exits.append({"room" : house_1, "localName" : "down stairs" })
	house_1Bedroom_2.exits.append({"room" : house_1Bedroom_1, "localName" : "Braden's room" })
	house_1Bedroom_2.exits.append({"room" : house_1Washroom_1, "localName" : "washroom"}) 
	house_1Bedroom_2.exits.append({"room" : house_1RecreationRoom, "localName" : "rec room"})
	house_1Washroom_1.exits.append({"room" : house_1, "localName" : "down stairs" })
	house_1Washroom_1.exits.append({"room" : house_1Bedroom_1, "localName" : "Braden's room" })
	house_1Washroom_1.exits.append({"room" : house_1Bedroom_2, "localName" : "Bedroom"})  
	house_1Washroom_1.exits.append({"room" : house_1RecreationRoom, "localName" : "rec room"})
	house_1RecreationRoom.exits.append({"room" : house_1, "localName" : "down stairs" })
	house_1RecreationRoom.exits.append({"room" : house_1Bedroom_1, "localName" : "Braden's room" })
	house_1RecreationRoom.exits.append({"room" : house_1Bedroom_2, "localName" : "Bedroom"}) 
	house_1RecreationRoom.exits.append({"room" : house_1Washroom_1, "localName" : "washroom"}) 

	
	zom0 = npc.Npc("zombie", 5, 1, "Brains....", world)
	zom1 = npc.Npc("super zombie", 20, 3, "He looks pretty tough.", world)

	if (int)(random.random()*2):
		hardwareAisle_1.items.append(items.Axe())
	else:
		hardwareWashroom.items.append(items.DumbAxe())

	if (int)(random.random()*2):
		floydAve_0.items.append(items.HealthPotion())
	else:
		floydAve_0.items.append(items.DeathJuice())

	if (int)(random.random()*2):
		quintenAve_2.npcs.append(zom0)
	else: 
		mozenSt_0.npcs.append(zom1)

	if (int)(random.random()*2):
		newtonAve_0.npcs.append(zom0)
	else: 
		zirrilaSt_1.npcs.append(zom1)

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

	world.rooms.append(hardware)
	world.rooms.append(hardwareAisle_0)
	world.rooms.append(hardwareAisle_1)
	world.rooms.append(hardwareAisle_2)
	world.rooms.append(hardwareWashroom)
	world.rooms.append(hardwareCashierTill)

	world.rooms.append(gasStation)
	world.rooms.append(gasStationCashierTill)
	world.rooms.append(gasStationWashroom)
	world.rooms.append(gasStationShop)
	world.rooms.append(gasStationPumps)

	world.rooms.append(restaurant)
	world.rooms.append(restaurantTables)
	world.rooms.append(restaurantKitchen)
	world.rooms.append(restaurantWashroom)
	world.rooms.append(restaurantCashierTill)

	world.rooms.append(hotel)
	world.rooms.append(hotelRoom_0)
	world.rooms.append(hotelRoom_1)
	world.rooms.append(hotelRoom_2)
	world.rooms.append(hotelLobby)
	world.rooms.append(hotelWashroom)
	world.rooms.append(hotelCashierTill)
	world.rooms.append(hotelStairs)
	world.rooms.append(hotelRoom_3)
	world.rooms.append(hotelRoom_4)
	world.rooms.append(hotelRoom_5)

	world.rooms.append(townHall)
	world.rooms.append(townHallLobby)
	world.rooms.append(townHallWashroom)
	world.rooms.append(townHallOffice)
	world.rooms.append(townHallMeetingRoom)

	world.rooms.append(park)
	world.rooms.append(parkPlayGround)
	world.rooms.append(parkFields)
	world.rooms.append(parkPicnicTables)
	world.rooms.append(parkWaterPark)
	world.rooms.append(parkMaintanceHouse)

	world.rooms.append(school)
	world.rooms.append(schoolClassroom_0)
	world.rooms.append(schoolClassroom_1)
	world.rooms.append(schoolClassroom_2)
	world.rooms.append(schoolClassroom_3)
	world.rooms.append(schoolOffice)
	world.rooms.append(schoolGym)
	world.rooms.append(schoolWashroom)
	world.rooms.append(schoolComputerRoom)

	world.rooms.append(pharmacy)
	world.rooms.append(pharmacyCashierTill)
	world.rooms.append(pharmacyStorage)
	world.rooms.append(pharmacyAisles)
	world.rooms.append(pharmacyCooler)
	world.rooms.append(pharmacyWashroom)

	world.rooms.append(house_0)
	world.rooms.append(house_0LivingRoom)
	world.rooms.append(house_0Kitchen)
	world.rooms.append(house_0Washroom)
	world.rooms.append(house_0Garage)
	world.rooms.append(house_0Bedroom)
	world.rooms.append(house_0Basement)

	world.rooms.append(house_1)
	world.rooms.append(house_1LivingRoom)
	world.rooms.append(house_1Kitchen)
	world.rooms.append(house_1Washroom_0)
	world.rooms.append(house_1Garage)
	world.rooms.append(house_1Bedroom_0)
	world.rooms.append(house_1Basement)
	world.rooms.append(house_1Stairs)
	world.rooms.append(house_1Bedroom_1)
	world.rooms.append(house_1Bedroom_2)
	world.rooms.append(house_1Washroom_1)
	world.rooms.append(house_1RecreationRoom)

	world.curRoom = mainSt_0
