import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updateable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for player in updateable:
            player.update(dt)
        
        screen.fill("black")

        for player in drawable:
            player.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
