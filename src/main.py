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

def parseCommand(command, arg=""):
	if command == "go": go(arg)
	elif command == "n": go("north")
	elif command == "s": go("south")
	elif command == "e": go("east")
	elif command == "w": go("west")

	elif (command == "l") or (command == "look"): look(arg)
	elif (command == "a") or (command == "attack"): attack(arg)

	elif command == "get": get(arg)
	elif command == "use": use(arg)
	elif (command == "wie") or (command == "wield"): wield(arg)
	elif command == "unw" or command == "unwield": player_obj.unequipWeapon()

	elif (command == "i") or (command == "inv"): player_obj.displayInventory()
	elif (command == "stat") or (command == "status"): player_obj.status()
	elif (command == "m") or (command == "map"): world_obj.printMap()
	elif command == "help": printHelp()
	
	elif command == "quit": quit()
	else:
		print("...")


name = input("Please enter your name: ")
world_obj = world.World()
player_obj = player.Player(world_obj, name)

print("")
print("Greetings, " + name + "!")
print("Type 'help' for help.")

while(True):
	print("")

	command = input(player_obj.getPrompt()).split(" ")
	if len(command) == 2:
		parseCommand(command[0], command[1])
	else:
		parseCommand(command[0])

	world_obj.victoryCheck()
