import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()    
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    asteroid_field = AsteroidField(updatable, drawable, asteroids_group)
    updatable.add(asteroid_field)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    initial_velocity = pygame.Vector2(50, 50)
    
    # Create the asteroid with the initial velocity
    asteroid = Asteroid(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 20, initial_velocity)
    
    # Add the asteroid to the respective groups
    asteroids_group.add(asteroid)
    updatable.add(asteroid)
    drawable.add(asteroid)

    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
   

if __name__ == "__main__":
    main()
