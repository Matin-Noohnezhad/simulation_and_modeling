from actions.wolf_sheep_grass.die import Die
from actions.wolf_sheep_grass.eat_grass import EatGrass
from actions.wolf_sheep_grass.eat_sheep import EatSheep
from actions.wolf_sheep_grass.eight_way_random_walk import EightWayRandomWalk
from actions.wolf_sheep_grass.grass_grow import GrassGrow
from actions.wolf_sheep_grass.reproduce import Reproduce

E1 = 3  # energy_decrease of wolf after walking
E2 = 30  # energy_increase of wolf after eating sheep
E3 = 3  # energy_decrease of sheep after walking
E4 = 30  # energy_increase of sheep after eating grass

# create actions
reproduce = Reproduce()
die = Die()
eat_sheep = EatSheep()
eat_grass = EatGrass()
grass_grow = GrassGrow()
random_walk = EightWayRandomWalk()


