class Item(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def use(self, player):
		raise NotImplementedError(str(type(self)) + " does not implement use().")

	def printDescription(self):
		print(self.description)

class Weapon(Item):
	def __init__(self, name, damage, description):
		super(Weapon, self).__init__(name, description)
		self.damage = damage

	def use(self, player):
		print("You can't use that.")

	def printDescription(self):
		print(self.description)
		print("Increases strength by " + str(self.damage) + ".")

class Healing(Item):
	def __init__(self, name, health, description):
		super(Healing, self).__init__(name, description)
		self.health = health

	def use(self, player):
		player.removeItem(self)
		player.recoverHealth(self.health)
		print("The " + self.name + " recovers " + str(self.health) + " health.")
		
	def printDescription(self):
		print(self.description)
		print("Restores " + str(self.health) + " health.")


class Axe(Weapon):
	def __init__(self):
		super(Axe, self).__init__("axe", 3, "A small axe useful for chopping up zombies.")

class HealthPotion(Healing):
	def __init__(self):
		super(HealthPotion, self).__init__("healing potion", 10, "A red potion that smells of cherries.")
