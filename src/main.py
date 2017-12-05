import world
import player

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

def printHelp():
	print("")
	print("Commands:")
	print("	go	[exit]")
	print("	l/look")
	print("	l/look	[item/npc]")
	print("	a/attack[npc]")
	print("	get	[item]")
	print("	use 	[item]")
	print("	wield	[weapon]")
	print("	i/inv")
	print("	status")
	print("	m/map")
	print("	help")
	print("	quit")

def go(arg):
	if arg == "":
		print("Go where?")
	else:
		world_obj.move(arg)

def look(arg):
	if arg == "":
		world_obj.displayRoom()
	else:
		world_obj.look(arg, player_obj)

def attack(arg):
	if arg == "":
		print("Attack what?")
	else:
		world_obj.startFight(player_obj, arg)

def get(arg):
	if arg == "":
		print("Get what?")
	else:
		player_obj.pickUpItem(arg)

def use(arg):
	if arg == "":
		print("Use what?")
	else:
		player_obj.use(arg)

def wield(arg):
	if arg == "":
		print("Wield what?")
	else:
		player_obj.wield(arg)

def quit():
	print('Goodbye!')
	exit()

def parseLookup(onCommand, arg=""):
	
	for exit in world_obj.curRoom.exits:
		exitList = exit['localName'].split()
		exitParse = ""
		numWords = len(exitList)
		i = 0
		while (i < numWords) and (len(exitList[i]) > 1):
			exitParse = exitParse + exitList[i][0] + exitList[i][1]
			i = i+1
		if (i == numWords-1 ) and (len(exitList[i]) == 1):
			exitParse = exitParse + exitList[i][0]
		if onCommand == "go":
			if arg == exitParse.lower():
				go(exit['localName'].lower())
				checkstop = 1
				return checkstop
		elif onCommand == exitParse.lower():
			go(exit['localName'].lower())
			checkstop = 1
			return checkstop

def parseCommand(command, arg=""):

	finishedParsing = parseLookup(command, arg)
	if finishedParsing !=1:
		if command == "go": go(arg)
		elif command == "n": go("north")
		elif command == "s": go("south")
		elif command == "e": go("east")
		elif command == "w": go("west")
		elif command == "nw": go ("north west")
		elif command == "ne": go ("north east")
		elif command == "sw": go ("south west")
		elif command == "se": go ("south east")
	
		elif (command == "l") or (command == "look"): look(arg)
		elif (command == "a") or (command == "attack"): attack(arg)

		elif command == "get": get(arg)
		elif command == "use": use(arg)
		elif (command == "wie") or (command == "wield"): wield(arg)
		elif (command == "unw") or (command == "unwield"): player_obj.unequipWeapon()

		elif (command == "i") or (command == "inv"): player_obj.displayInventory()
		elif (command == "stat") or (command == "status"): player_obj.status()
		elif (command == "m") or (command == "map"): world_obj.printMap()
		elif command == "help": printHelp()
	
		elif command == "quit": quit()

		else:
			print("...")


def restart():
	global name
	global world_obj
	global player_obj

	name = input("Please enter your name: ")
	world_obj = world.World()
	player_obj = player.Player(world_obj, name)

name = input("Please enter your name: ")
world_obj = world.World()
player_obj = player.Player(world_obj, name)

print("")
print("Greetings, " + name + "!")
print("Type 'help' for help.")

while(True):
	print("")

	command = input(player_obj.getPrompt()).split(" ",1)
	if len(command) == 2:
		parseCommand(command[0], command[1])
	else:
		parseCommand(command[0])

	player_obj.checkAlive()
	if world_obj.victoryCheck():
		response = input("Play again? ")
		if response.lower() == "y" or response.lower() == "yes":
			restart()
		else:
			exit()
