import logging
import os
from random import randint

from animals import Animal
from dotenv import load_dotenv
from simpleobjects import Dimensions, Matrix

load_dotenv()

try:
    MAX_SIZE = os.environ["MAPSIZE"] or 64
except KeyError:
    MAX_SIZE = 64

logger = logging.getLogger("pdt.maps")


class Map:
    TILESET_ROOT = "./tilesets/"
    TILESET = {}
    animals = []

    def __init__(self, size: int = None):
        self.size = Dimensions(
            size or randint(10, MAX_SIZE), size or randint(10, MAX_SIZE)
        )
        self._set_matrix()

    # Tileset Functions
    def load_tileset(self) -> bool:
        """Returns bool of tileset load success"""
        try:
            for tileset in os.listdir(self.TILESET_ROOT):
                tileset_path = os.path.join(self.TILESET_ROOT, tileset)
                self.TILESET[tileset] = {
                    "path": tileset_path,
                    "files": os.listdir(tileset_path),
                }
            return True
        except FileNotFoundError:
            return False

    # Animal Functions
    def spawn_animals(self, animals: Animal | list[Animal]) -> bool:
        try:
            if isinstance(animals, list):
                for animal in animals:
                    self.animals.append(animal)
                    self.matrix.matrix[animal.get_position.y][
                        animal.get_position.x
                    ] = animal
                    animal.map = self
                return True
            else:
                self.animals.append(animals)
                self.matrix.matrix[animals.get_position.y][
                    animals.get_position.x
                ] = animals
                animals.map = self
                return True
        except Exception as e:  # Will narrow as issues arise
            logger.error(e)
            return False

    def update_animal_positions(self):
        for animal in self.animals:
            self.matrix.matrix[animal.get_position.y][animal.get_position.x] = animal
            self.matrix.matrix[animal.last_position.y][animal.last_position.x] = None

    # Internal Class Functions
    def _set_matrix(self) -> None:
        """Initializes the map matrix of self.size.width and self.size.height"""
        _matrix = [
            [[None] for i in range(self.size.width)] for _ in range(self.size.height)
        ]
        self.matrix = Matrix(size=self.size, matrix=_matrix)
