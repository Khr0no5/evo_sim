def calculate_agent_nutrition(agent):
    # Base it on current or max energy, size, or other factors
    return max(10, int(agent.energy * 0.75))

def calculate_corpse_nutrition(energy_at_death):
    return max(15, int(energy_at_death * 0.6))
