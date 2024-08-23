import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)  # Optionally call parent constructor
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = pygame.Vector2(velocity)  # Initialize velocity as a vector

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius, 2)
    
    def update(self, dt):
        # Adjust the position based on velocity and delta time (dt)
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt