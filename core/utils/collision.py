"""utility functions for circular collision detection."""

def circle_collision(pos1, radius1, pos2, radius2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    distance_squared = dx * dx + dy * dy
    combined_radius = radius1 + radius2
    return distance_squared < combined_radius * combined_radius
