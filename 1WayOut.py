#!/usr/bin/env python
import sys
sys.path.append('Classes')
import world
import player
import combat

p1 = player.Player()
gameWorld = world.World()

print("Survive the zombie horde.")
print('')

i = True
while (i == True):
	
	if gameWorld.curRoom.npcs != []:
		if gameWorld.curRoom.npcs[0].stats.name == "Zombie":
			combat.Combat(p1,gameWorld.curRoom.npcs[0])

	usercmd = raw_input('')
	if usercmd == 'n':
		gameWorld.move('North')
	elif usercmd == 's':
		gameWorld.move('South')
	elif usercmd == 'w':
		gameWorld.move('West')
	elif usercmd == 'e':
		gameWorld.move('East')
	elif usercmd == 'c':
		gameWorld.move('Center')
	elif usercmd == 'map':
		gameWorld.printMap()
	elif usercmd == 'quit':
		i = False
	elif usercmd == 'help':
		print('n - Go North.')
		print('s - Go South.')
		print('w - Go West.')
		print('e - Go East.')
		print('c - Go to the Center.')
		print('map - Open game map.')
		print('quit - Quit 1WayOut.')
	else:
		print("That is not a valid command.")
		print("Type 'help' for help.")






