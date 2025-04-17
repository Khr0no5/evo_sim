# config.py
"""global configuration for the evo sim environment."""

# === display & world ===
screen_width = 1200
screen_height = 1200
fps = 30 #base is 60

logic_tick_rate = 60  # base is 60 ticks per second, regardless of rendering

background_color = (30, 30, 30)  # dark gray, petri dish style

# === world boundaries ===
wrap_edges = True  # if true, agents phase from one edge to the other (like bibites)

# === agent defaults ===
initial_agent_count = 25
default_agent_size = 8
default_agent_speed = 1.5
default_agent_vision = 100

# === resource spawn settings ===
initial_vegetation_count = 100
initial_producer_count = 20
initial_watersource_count = 5

# === corpse decay ===
corpse_lifespan = 5000  # in ticks/frames
corpse_nutrition = 50

# === mutation settings (can move to genetics if needed) ===
mutation_rate = 0.1
mutation_magnitude = 0.2

# === debug settings ===
debug_mode = False
show_fps = True
show_hitboxes = False

# === ui defaults ===
font_name = "arial"
font_size = 16
ui_padding = 10

