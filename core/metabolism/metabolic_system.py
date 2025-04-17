class Metabolism:
    def __init__(self, agent):
        self.agent = agent

    def tick(self): #tick based arguments for the base level of metabolic cost for 'existing'
                    #later modifiable by gene expression or logic in the brains
        genes = self.agent.genes

        base_loss = genes.get("base_metabolism", 0.1)
        move_factor = genes.get("movement_cost_factor", 0.05)
        attack_cost = genes.get("attack_cost", 1.5) if self.agent.is_attacking else 0
        breeding_cost = genes.get("breeding_cost", 5.0) if self.agent.is_breeding else 0

        movement_loss = self.agent.current_speed * move_factor

        total_loss = base_loss + movement_loss + attack_cost + breeding_cost
        self.agent.energy -= total_loss

        if self.agent.energy <= 0:
            self.agent.alive = False
            self.agent.dead = True

        print(f"Agent energy: {self.agent.energy:.2f}")


def can_breed(self):
    return self.agent.energy >= self.agent.genes.get("min_breeding_energy", 20)

    def take_damage(self, amount):
        self.agent.energy -= amount
