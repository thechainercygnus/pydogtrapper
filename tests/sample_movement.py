import maps
import animals
import pprint as pp

a1 = animals.Animal(species="test", state=0, injuries={None})
m1 = maps.Map(size=5)
m1.spawn_animals(a1)
pp.pprint(m1.matrix.matrix)
a1.move(1, 1)
m1.update_animal_positions()
pp.pprint(m1.matrix.matrix)
