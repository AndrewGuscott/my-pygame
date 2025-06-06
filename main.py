# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
#	print("Starting Asteroids!")
#	print(f"Screen width: {SCREEN_WIDTH}")
#	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()
	bullets = pygame.sprite.Group()
	Shot.containers = (bullets, updatable, drawable)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(pygame.Color('black'))
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collides(player):
				print("Game over!")
				return
			for shot in bullets:
				if asteroid.collides(shot):
					asteroid.split()
					shot.kill()
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
