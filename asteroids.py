import random
from circleshape import *
from constants import *

class Asteroids(CircleShape):
    # Create Asteroids
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw Asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)
    
    # Calculating new Asteroid position
    def update(self, dt):
        self.position += self.velocity * dt

    # Splitting Asteroids when they are hit
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        new1 = self.velocity.rotate(split_angle)
        new2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new1 * 1.2
        asteroid2.velocity = new2 * 1.2