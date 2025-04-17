from entities.vegetation import vegetation
from entities.watersource import watersource
from core import config

def init_vegetation():
    return [vegetation() for _ in range(config.initial_vegetation_count)]

def draw_vegetation(surface, vegetation_list):
    for blob in vegetation_list:
        blob.draw(surface)

def update_vegetation(vegetation_list, watersources): #for logic loop calling come use in future
    for v in vegetation_list:
        if not v.eaten:
            v.avoid_water(watersources) # ✅ this nudges them
            v.update() #applies drift motion when bumped into
    vegetation_list[:] = [v for v in vegetation_list if not v.eaten]

