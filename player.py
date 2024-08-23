from circleshape import *
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__class__.containers[0].add(self)  # adds to 'updatable'
        self.__class__.containers[1].add(self)  # adds to 'drawable'
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def movement(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.movement(dt)
        if keys[pygame.K_s]:
            self.movement(-dt)



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)