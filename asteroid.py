from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
#		print(f'Asteroid.py: Asteroid Spawned at ({self.position.x}, {self.position.y}) with radius {self.radius}')

	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color('Red'), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
