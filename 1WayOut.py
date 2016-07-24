#! /usr/bin/env python
import sys
sys.path.append('Classes')
import world
import player

world_obj = world.World()
player_obj = player.Player()

def printHelp():
	print("Commands:")
	print("	go	[exit]")
	print("	get	[item]")
	print("	l/look")
	print("    *	l/look	[item/npc]")
	print("    *	wield	[weapon]")
	print("    *	join	[person]")
	print("    *	k/kill	[npc]")
	print("    *	i/inv")
	print("	m/map")
	print("	quit")
	print("	help")
	print("")
	print("  * Not yet implemented.")
	print("")

def parseCommand(command, arg=""):
	if command == "go":
		if arg == "":
			print("Go where?")
		else:
			world_obj.move(arg)
	elif command == "n":
		world_obj.move("North")
	elif command == "s":
		world_obj.move("South")
	elif command == "e":
		world_obj.move("East")
	elif command == "w":
		world_obj.move("West")

	elif (command == "l") or (command == "look"):
		if arg == "":
			world_obj.displayRoom()
	elif (command == "m") or (command == "map"):
		world_obj.printMap()

	elif command == "get":
		player_obj.getItem(arg, world_obj)
	elif (command == "i") or (command == "inv"):
		player_obj.displayInventory()

	elif command == "help":
		printHelp()
	elif command == "quit":
		print("Goodbye!")
		return 1
	else:
		print("...")


while(True):
	command = raw_input(">> ").split(" ")
	if len(command) == 2:
		rv = parseCommand(command[0], command[1])
		if rv == 1:
			exit()
	else:
		rv = parseCommand(command[0])
		if rv == 1:
			exit()

