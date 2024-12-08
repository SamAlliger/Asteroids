from circleshape import *
from constants import *

class Shot(CircleShape):
    # Create Asteroids
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    # Draw Asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)
    
    # Calculating new Asteroid position
    def update(self, dt):
        self.position += self.velocity * dt