# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize clock
    clock = pygame.time.Clock()
    dt = 0

    # Creating groups for more structured calling
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assigning groups
    Player.containers = (updateable, drawable)
    Asteroids.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    # Initialize player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Initialize AsteroidField
    asteroidField = AsteroidField()

    # Infinte game loop
    while True:
        # Quit when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Black background
        screen.fill(color="black", rect=None, special_flags=0)
        # Updating positions
        for u in updateable:
            u.update(dt)
        for a in asteroids:
            # Check for Asteroid destruction
            for s in shots:
                if s.check_collision(a):
                    a.split()
                    s.kill()
            # Check for Player death
            if a.check_collision(player):
                print("Game over!")
                sys.exit()
            
        # Drawing at new positions
        for d in drawable:
            d.draw(screen)
        # Refresh screen, wait on clock, setting FPS limit
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
