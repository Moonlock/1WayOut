def Combat(p1,enemy):
	 
	 print("You attack the zombie")

	 if p1.weapon.equip == True:
	 	p1Damage = p1.weapon.damage
	 else:
	 	p1Damage = p1.stats.strength
	 p1Health = p1.stats.health
	 enemyHealth = enemy.stats.health
	 enemyDamage = enemy.stats.damage
	 while (enemyHealth > 0 or p1Health > 0):
	 	enemyHealth = enemyHealth - p1Damage
	 	print("You attack the Zombie and deal" + " " +str(p1Damage) +" "+ " damage to it")
	 	if enemyHealth < 1:
	 		break
	 	p1Health = p1Health - enemyDamage
	 	print("The zombie hits you for" + " " +str(enemyDamage) + " " + "damage")
	 if enemyHealth < 1:
	 	enemy.stats.name = "deadZombie"
	 	print ("you killed the Zombie!")
	 elif p1Health < 1:
		print("The Zombie killed you!")
	 else:
	 	print("An error has occured")






    


