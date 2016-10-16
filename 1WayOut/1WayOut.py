#! /usr/bin/env python
import sys
import world
import player

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

world_obj = world.World()
player_obj = player.Player(world_obj)

def printHelp():
	print("Commands:")
	print("	go	[exit]")
	print("	l/look")
	print("	l/look	[item/npc]")
	print("	get		[item]")
	print("	drop 	[item]")
	print("	i/inv")
	print("	use 	[item]")
	print("	wield	[weapon]")
	print(" unequip	[weapon]")
	print("	status")
	print("	a/attack[npc]")
	print("	m/map")
	print("	quit")
	print("	help")

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
		else:
			world_obj.look(arg, player_obj)
	elif (command == "m") or (command == "map"):
		world_obj.printMap()
	elif (command == "stat") or (command == "status"):
		player_obj.status()

	elif (command == "a") or (command == "attack"):
		if arg == "":
			print("Attack what?")
		else:
			world_obj.startFight(player_obj, arg)

	elif command == "get":
		if arg == "":
			print("Get what?")
		else:
			player_obj.pickUpItem(arg)

	elif command =="drop":
		if arg == "":
			print "Drop what?"
		else:
			player_obj.dropItem(arg)

	elif (command == "i") or (command == "inv"):
		player_obj.displayInventory()
	
	elif command == "use":
		if arg == "":
			print("Use what?")
		else:
			player_obj.use(arg)
	elif (command == "wie") or (command == "wield"):
		if arg == "":
			print("Wield what?")
		else:
			player_obj.wield(arg)

	elif (command == "unequip") or (command == "uneq"):
		if arg == "":
			print("Unequip what?")
		else:
			player_obj.unequip(arg)


	elif command == "help":
		printHelp()
	elif command == "quit":
		print("Goodbye!")
		return 1
	else:
		print("...")


while(True):
	print("")

	command = input(player_obj.getPrompt()).split(" ")
	if len(command) == 2:
		rv = parseCommand(command[0], command[1])
	else:
		rv = parseCommand(command[0])
	
	if rv == 1:
		exit()

	world_obj.victoryCheck()

