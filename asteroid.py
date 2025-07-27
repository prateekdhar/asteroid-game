import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return []
        else:
            r=self.radius-ASTEROID_MIN_RADIUS
        random_angle=random.uniform(20,50)
        new_asteroid_1=Asteroid(self.position.x,self.position.y,r)
        new_asteroid_2=Asteroid(self.position.x,self.position.y,r)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_asteroid_1.velocity = vel1
        new_asteroid_2.velocity = vel2
        return [new_asteroid_1,new_asteroid_2]