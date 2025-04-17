import math

def distance(a, b):
    """Calculate Euclidean distance between two 2D positions."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find_closest_food(agent, vegetation_list, corpse_list):
    """
    Return the closest edible object to the agent,
    respecting their dietary preference from genes.
    """
    diet = agent.genes.get("diet_type", "omnivore")  # herbivore, carnivore, or omnivore

    closest_food = None
    min_distance = float('inf')

    if diet in ("herbivore", "omnivore"):
        for food in vegetation_list:
            if getattr(food, "eaten", False):
                continue
            d = distance(agent.position, food.position)
            if d < min_distance:
                min_distance = d
                closest_food = food

    if diet in ("carnivore", "omnivore"):
        for corpse in corpse_list:
            d = distance(agent.position, corpse.position)
            if d < min_distance:
                min_distance = d
                closest_food = corpse

    return closest_food



def move_toward(agent, target, speed=1.0):
    """Adjust agent's direction and speed to move toward a target object."""
    dx = target.position[0] - agent.position[0]
    dy = target.position[1] - agent.position[1]
    dist = math.hypot(dx, dy)

    if dist == 0:
        return  # Already at target

    # Normalize direction
    dx /= dist
    dy /= dist

    # Update agent heading and speed
    agent.angle = math.atan2(dy, dx)
    agent.current_speed = min(agent.max_speed, speed)
