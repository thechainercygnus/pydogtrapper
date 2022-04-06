from typing import NamedTuple


class Coordinates(NamedTuple):
    x: int
    y: int


class Dimensions(NamedTuple):
    width: int
    height: int


class Conditions(NamedTuple):
    temperature: float
    humidity: float
    cloud_cover: float
    precipitation_chance: float


class Matrix(NamedTuple):
    matrix: list[list]
    size: Dimensions
