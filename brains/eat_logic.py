def attempt_eating(agent, vegetation_list, corpse_list):
    """Check if the agent is colliding with food and consume it if so."""
    for food in vegetation_list:
        if getattr(food, "eaten", False):
            continue
        if agent.collides_with(food):
            agent.energy += food.nutrition
            food.eaten = True
            return  # Only eat one food source per tick

    for corpse in corpse_list:
        if agent.collides_with(corpse) and corpse.nutrition > 0:
            agent.energy += corpse.nutrition
            corpse.nutrition = 0  # Prevent double consumption
            return
