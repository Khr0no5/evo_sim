from brains.seek_logic import find_closest_food, move_toward
import math

class brain:
    def __init__(self, agent):
        self.agent = agent

    def tick(self, vegetation_list, corpse_list, watersources):
        # Step 1: Hard water boundary check
        for water in watersources:
            if water.is_inside_inner_boundary(self.agent.position):
                # Find closest blob inside the water to escape from
                closest_blob = min(
                    water.blobs,
                    key=lambda b: (self.agent.position[0] - b["pos"][0]) ** 2 +
                                  (self.agent.position[1] - b["pos"][1]) ** 2
                )

                dx = self.agent.position[0] - closest_blob["pos"][0]
                dy = self.agent.position[1] - closest_blob["pos"][1]
                dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)

                self.agent.angle = math.atan2(dy, dx)
                self.agent.current_speed = self.agent.max_speed
                return  # Water escape is priority this tick

        # Step 2: Seek food if hungry
        if self.agent.energy < 80:
            target = find_closest_food(self.agent, vegetation_list, corpse_list)
            if target:
                move_toward(self.agent, target)
                return

        # Step 3: Wander
        self.agent.current_speed = self.agent.max_speed * 0.6
