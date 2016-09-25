class Zombie:

	def __init__(self, name):
		self.name = name
		self.health = 5
		self.strength = 1

	def takeTurn(self, opponent):
		self.attack(opponent)

	def attack(self, opponent):
		opponent.takeDamage(self.strength)

	def takeDamage(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.die()

	def die(self):
		print(self.name + " has died.")