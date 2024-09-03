import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()
    print(SCREEN_HEIGHT)
    print(SCREEN_WIDTH)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    starting_player_x = SCREEN_WIDTH / 2
    starting_player_y = SCREEN_HEIGHT / 2
    player = Player(starting_player_x, starting_player_y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
