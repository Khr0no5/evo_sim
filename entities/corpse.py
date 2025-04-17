import pygame
from core.metabolism.nutrition import calculate_corpse_nutrition

class Corpse:
    def __init__(self, position, radius=8, color=(100, 0, 0), energy=100):
        self.position = position.copy()
        self.radius = radius
        self.color = color
        self.velocity = [0, 0]
        self.drift_decay = 0.95
        self.nutrition = calculate_corpse_nutrition(energy)


    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[0] *= self.drift_decay
        self.velocity[1] *= self.drift_decay

        self.position[0] %= 1200
        self.position[1] %= 1200

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.position[0]), int(self.position[1])),
            self.radius
        )

    def nudge(self, dx, dy):
        self.velocity[0] += dx
        self.velocity[1] += dy
