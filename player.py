from constants import *
from circleshape import *
from bullet import *

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.cooldown = 0

	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def draw(self, screen):
		pygame.draw.polygon(screen, pygame.Color('White'), self.triangle(), 2)

	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.cooldown += dt

		if keys[pygame.K_a]:
			self.rotate(-1 * dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-1 * dt)
		if keys[pygame.K_SPACE]:
			if self.cooldown > PLAYER_SHOOT_COOLDOWN:
				self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		self.cooldown = 0
		bullet = Shot(self.position.x, self.position.y)
		bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
