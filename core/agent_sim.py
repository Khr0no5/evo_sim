from agents.agent import agent
from core import config
from utils.collision import circle_collision
from core.metabolism.metabolic_system import Metabolism
from brains.seek_logic import find_closest_food, move_toward
from brains.eat_logic import attempt_eating
from entities.corpse import Corpse

def init_agents():
    return [agent() for _ in range(config.initial_agent_count)]

def update_agents(agent_list, watersources, vegetation_list, corpse_list, corpse_output):
    for a in agent_list:
        if a.alive:
            Metabolism(a).tick()

            if a.energy < 80:
                target = find_closest_food(a, vegetation_list, corpse_list)
                if target:
                    move_toward(a, target)

            a.brain.tick(vegetation_list, corpse_list, watersources)
            a.update()

            # Push vegetation when colliding
            for veg in vegetation_list:
                if circle_collision(a.position, a.radius, veg.position, veg.radius):
                    dx = veg.position[0] - a.position[0]
                    dy = veg.position[1] - a.position[1]
                    dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)

                    veg.nudge(dx / dist * 0.3, dy / dist * 0.3)
                    a.velocity[0] -= dx / dist * 0.05
                    a.velocity[1] -= dy / dist * 0.05

            # Try to eat something
            attempt_eating(a, vegetation_list, corpse_list)

        elif not a.dead:
            a.dead = True
            corpse_output.append(Corpse(a.position, a.radius, energy=a.energy))

def draw_agents(surface, agent_list):
    for a in agent_list:
        a.draw(surface)
