import os
from random import randint

from dotenv import load_dotenv
from simpleobjects import Dimensions, Matrix

load_dotenv()

try:
    MAX_SIZE = os.environ["MAPSIZE"] or 64
except KeyError:
    MAX_SIZE = 64


class Map:
    TILESET_ROOT = "./tilesets/"
    TILESET = {}

    def __init__(self, size: int = None):
        self.size = Dimensions(
            size or randint(10, MAX_SIZE), size or randint(10, MAX_SIZE)
        )
        self._set_matrix()

    def load_tileset(self) -> bool:
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

    def _set_matrix(self) -> None:
        _matrix = [
            [[None] for i in range(self.size.width)] for _ in range(self.size.height)
        ]
        self.matrix = Matrix(size=self.size, matrix=_matrix)
