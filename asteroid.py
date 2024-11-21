import circleshape
import random
from constants import *
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            self.r_angle = random.uniform(20, 50)
            self.r_vector = self.velocity.rotate(self.r_angle)
            self.r_vector2 = self.velocity.rotate(-abs(self.r_angle))
            self.new_rad = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position[0], self.position[1], self.new_rad)
            split_2 = Asteroid(self.position[0], self.position[1], self.new_rad)
            split_1.velocity = self.r_vector
            split_2.velocity = self.r_vector2
            
