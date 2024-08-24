import pygame 

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    #  def check_collision(self, other_circle):
    #     distance =self.position.distance_to(other_circle.position)
    #     if distance < (self.radius + other_circle.radius):
    #         return True
    #     return False
    
    def collides_with(self, other_cirlce):
        return self.position.distance_to(other_cirlce.position) <= self.radius + other_cirlce.radius