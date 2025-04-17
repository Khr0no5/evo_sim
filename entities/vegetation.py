import random
import pygame
from utils.collision import circle_collision

class vegetation:
    def __init__(self, position=None, radius=4, color=(0, 200, 0)):
        self.radius = radius
        self.color = color
        self.position = position or [random.randint(0, 1200), random.randint(0, 1200)]
        self.velocity = [0, 0]  # add basic drift velocity
        self.nutrition = 10  # static energy value for now
        self.eaten = False #flag for despawn and respawn characteristic

    def update(self):
        # apply velocity to position (simple drift)
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # apply slight decay to slow it over time
        self.velocity[0] *= 0.95
        self.velocity[1] *= 0.95

    def avoid_water(self, watersources):
        for water in watersources:
            for blob in water.blobs:
                if circle_collision(self.position, self.radius, blob["pos"], blob["radius"]):
                    dx = self.position[0] - water.position[0]
                    dy = self.position[1] - water.position[1]
                    dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)
                    self.nudge(dx / dist * 0.5, dy / dist * 0.5)

    def nudge(self, dx, dy):
        self.velocity[0] += dx
        self.velocity[1] += dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)
