import pygame
import random

class watersource:
    def __init__(self, position=None, blob_count=3, radius_range=(15, 35), color=(0, 150, 255)):
        self.position = position or [random.randint(0, 1200), random.randint(0, 1200)]
        self.color = color
        self.blobs = []
        self.edge_buffer = 10  # how far from center is “too close”

        for _ in range(blob_count):
            offset_x = random.randint(-30, 30)
            offset_y = random.randint(-30, 30)
            radius = random.randint(*radius_range)
            blob = {
                "pos": [self.position[0] + offset_x, self.position[1] + offset_y],
                "radius": radius
            }
            self.blobs.append(blob)

    def draw(self, surface):
        # Create a transparent surface the size of the screen
        water_surface = pygame.Surface((1200, 1200), pygame.SRCALPHA)

        for blob in self.blobs:
            # Outer soft water zone (lighter blue)
            pygame.draw.circle(
                water_surface,
                (*self.color, 100),  # Light blue, soft transparency
                blob["pos"],
                blob["radius"]
            )

            # Inner danger zone (darker, deeper water)
            pygame.draw.circle(
                water_surface,
                (0, 100, 180, 180),  # Darker blue, more opaque
                blob["pos"],
                blob["radius"] - 10  # Matches the edge_buffer for is_inside_inner_boundary
            )

        # Blit the transparent water overlay to the main screen
        surface.blit(water_surface, (0, 0))

    def contains_point(self, point):
        for blob in self.blobs:
            dx = blob["pos"][0] - point[0]
            dy = blob["pos"][1] - point[1]
            if dx * dx + dy * dy < blob["radius"] ** 2:
                return True
        return False

    def is_inside(self, point):
        # deeper than just the edge—like stepping too far in
        for blob in self.blobs:
            dx = blob["pos"][0] - point[0]
            dy = blob["pos"][1] - point[1]
            if dx * dx + dy * dy < (blob["radius"] - 3) ** 2:
                return True
        return False

    def is_inside_inner_boundary(self, pos, edge_buffer=20):
        for blob in self.blobs:
            dx = pos[0] - blob["pos"][0]
            dy = pos[1] - blob["pos"][1]
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < (blob["radius"] - edge_buffer):
                return True  # Agent is too deep inside
        return False

    def is_near_edge(self, point, edge_buffer=5):
        for blob in self.blobs:
            dx = blob["pos"][0] - point[0]
            dy = blob["pos"][1] - point[1]
            dist_sq = dx * dx + dy * dy
            outer = blob["radius"] ** 2
            inner = (blob["radius"] - edge_buffer) ** 2
            if inner < dist_sq <= outer:
                return True
        return False

    def is_blocking(self, point):
        return self.is_inside(point)
