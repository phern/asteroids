import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

color = (0,0,0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        for object in updatable:
            object.update(dt)

        screen.fill(color=color)

        for object in drawable:
            object.draw(screen)  

        pygame.display.flip()
        for object in asteroids:
            if player.collides(object):
                print('Game over!')
                exit()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()