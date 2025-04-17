"""handles initialization and rendering of water sources."""
from entities.watersource import watersource
from core import config

def init_watersources():
    return [watersource() for _ in range(config.initial_watersource_count)]

def draw_watersources(surface, watersource_list):
    for water in watersource_list:
        water.draw(surface)
