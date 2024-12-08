# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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

    # Assigning groups
    Player.containers = (updateable, drawable)

    # Initialize player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Infinte game loop
    while True:
        # Quit when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Black background
        screen.fill(color="black", rect=None, special_flags=0)
        # Updating positions
        for x in updateable:
            x.update(dt)
        # Drawing at new positions
        for y in drawable:
            x.draw(screen)
        # Refresh screen, wait on clock, setting FPS limit
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
