class Zombie:

	def __init__(self, name, health, strength, description, world):
		self.name = name
		self.health = health
		self.strength = strength
		self.desc = description
		self.world = world

	def takeTurn(self, opponent):
		self.attack(opponent)

	def attack(self, opponent):
		opponent.takeDamage(self.strength)

	def takeDamage(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		self.world.remainingZombies -= 1
		print(self.name + " has died.")

	def isAlive(self):
		return self.health > 0