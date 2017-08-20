class Item(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def useOn(self, player):
		raise NotImplementedError(str(type(self)) + " does not implement use().")

	def equipTo(self, player):
		raise NotImplementedError(str(type(self)) + " does not implement equipTo().")

	def printDescription(self):
		print(self.description)


class Weapon(Item):
	def __init__(self, name, damage, description):
		super(Weapon, self).__init__(name, description)
		self.damage = damage

	def useOn(self, player):
		print("You can't use that.")

	def equipTo(self, player):
		player.unequipWeapon()
		player.wieldWeapon(self)

	def printDescription(self):
		print(self.description)
		print("Increases strength by " + str(self.damage) + ".")

class Healing(Item):
	def __init__(self, name, health, description):
		super(Healing, self).__init__(name, description)
		self.health = health

	def useOn(self, player):
		player.removeItem(self)
		player.recoverHealth(self.health)
		print("The " + self.name + " recovers " + str(self.health) + " health.")

	def equipTo(self, player):
		print("That is not a weapon.")
		
	def printDescription(self):
		print(self.description)
		print("Restores " + str(self.health) + " health.")


class Axe(Weapon):
	def __init__(self):
		super(Axe, self).__init__("axe", 3, "A small axe useful for chopping up zombies.")

class DumbAxe(Weapon):
	def __init__(self):
		super(DumbAxe, self).__init__("dumb axe", -2, "A small axe that inflicts pain.")

class DeathJuice(Healing):
	def __init__(self):
		super(DeathJuice, self). __init__("death juice", -20, "A tasty potion that definitely won't kill you.")

class HealthPotion(Healing):
	def __init__(self):
		super(HealthPotion, self).__init__("healing potion", 10, "A red potion that smells of cherries.")



