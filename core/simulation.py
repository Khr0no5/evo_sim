"""main simulation loop and petri dish backdrop setup."""

import pygame
from core import config
from core.water_sim import init_watersources, draw_watersources
from core.vegetation_sim import init_vegetation, draw_vegetation
from core.vegetation_sim import update_vegetation
from core.agent_sim import init_agents, update_agents, draw_agents
from entities.corpse import Corpse
from core.metabolism.metabolic_system import Metabolism
from brains.seek_logic import find_closest_food, move_toward
from brains.eat_logic import attempt_eating




def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("evo sim")
    clock = pygame.time.Clock()

    tick_timer = 0  # time accumulator for logic
    running = True

    vegetation_blobs = init_vegetation()

    watersource_blobs = init_watersources()

    agent_blobs = init_agents()

    corpses = []

    while running:
        # time since last frame (in milliseconds)
        delta_time = clock.tick(config.fps)
        tick_timer += delta_time

        # handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update simulation logic based on tick rate
        while tick_timer >= (1000 / config.logic_tick_rate):
            # call update functions here (agents, food, etc.)
            update_vegetation(vegetation_blobs,watersource_blobs) #fully despawns interacted vegetation upon consumption.
            # update_agents()
            update_agents(agent_blobs, watersource_blobs, vegetation_blobs, corpses, corpses)


            # update_entities()
            tick_timer -= (1000 / config.logic_tick_rate)

        # draw world
        screen.fill(config.background_color)
        # draw entities here (food, water, agents, etc.)
        #draw agents
        draw_agents(screen, agent_blobs)
        #draw vegetation
        draw_vegetation(screen, vegetation_blobs)
        # update corpses
        for corpse in corpses:
            corpse.update()
        # draw corpses
        for corpse in corpses:
            corpse.draw(screen)
        #draw water
        draw_watersources(screen, watersource_blobs)



        # update display
        pygame.display.flip()



    pygame.quit()
