import pygame
from player import Player
from constants import *

color = (0,0,0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(color=color)
        player.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000























if __name__ == '__main__':
    main()