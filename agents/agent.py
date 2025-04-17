import pygame
import random
import math
from utils.collision import circle_collision
from brains.brain import brain

class agent:
    def __init__(self, position=None, radius=6, color=(245, 245, 245)): #color beige to start
        self.position = position or [
            random.uniform(0, 1200),
            random.uniform(0, 1200)
        ]
        self.velocity = [
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]
        self.radius = radius
        self.color = color
        self.max_speed = 1.5
        self.current_speed = self.max_speed  # Start at full speed for now
        self.acceleration = 0.05
        self.angle = random.uniform(0, 2 * math.pi)
        self.brain = brain(self)
        self.energy = 100.0 #(baseline 100)
        self.base_metabolism = 0.1
        self.movement_cost_factor = 0.05
        self.is_attacking = False
        self.is_breeding = False
        self.alive = True
        self.dead = False

        # Gene-based metabolic traits (modifiable in the future)
        self.genes = {
            "base_metabolism": 0.1,  # passive energy drain per tick (baseline 0.1)
            "movement_cost_factor": 0.05,  # energy per speed unit (baseline 0.05)
            "attack_cost": 1.5,  # energy drain per attack
            "breeding_cost": 5.0,  # energy drain per reproduction attempt
            "diet_type": random.choice(["herbivore", "carnivore", "omnivore"])
        }

    def update(self):
        if self.dead:
            return  # No movement or rotation if dead

        # apply slight angle change for wandering behavior
        self.angle += random.uniform(-0.1, 0.1)

        # calculate target velocity from angle
        target_velocity = [
            math.cos(self.angle) * self.current_speed,
            math.sin(self.angle) * self.current_speed
        ]

        # smooth velocity curve toward new direction
        self.velocity[0] += (target_velocity[0] - self.velocity[0]) * self.acceleration
        self.velocity[1] += (target_velocity[1] - self.velocity[1]) * self.acceleration

        # apply velocity to position
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # screen wrapping behavior
        self.position[0] %= 1200
        self.position[1] %= 1200

    def draw(self, surface):
        draw_color = (100, 0, 0) if self.dead else self.color  # Dark maroon if dead
        pygame.draw.circle(
            surface,
            draw_color,
            (int(self.position[0]), int(self.position[1])),
            self.radius
        )

    def collides_with(self, other):
        return circle_collision(self.position, self.radius, other.position, other.radius)

    def avoid_water(self, watersources):
        for water in watersources:
            if water.is_inside(self.position):
                return True
        return False
