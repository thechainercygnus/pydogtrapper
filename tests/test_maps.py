import os

import pytest
from animals import Animal, Dog
from maps import Map
from maps._maps import MAX_SIZE
from simpleobjects import Coordinates, Dimensions


@pytest.fixture
def base_map_fixed_size():
    return Map(size=MAX_SIZE)


@pytest.fixture
def base_map_random_size():
    return Map()


@pytest.fixture
def single_animal():
    return Animal(species="test", state=0, injuries={None})


@pytest.fixture
def multiple_animals():
    return [
        Animal(species="test", state=0, injuries={None}),
        Dog(name="Frankie", state=0, injuries={None}),
    ]


def test_should_create_map_object_with_fixed_size(base_map_fixed_size):
    assert base_map_fixed_size.size == Dimensions(MAX_SIZE, MAX_SIZE)


def test_should_create_map_object_with_random_size(base_map_random_size):
    map_dimensions = base_map_random_size.size
    assert map_dimensions.width >= 10 and map_dimensions.width <= MAX_SIZE
    assert map_dimensions.height >= 10 and map_dimensions.height <= MAX_SIZE


def test_map_tileset_path_should_exist(base_map_random_size):
    assert os.path.exists(base_map_random_size.TILESET_ROOT)


def test_map_tileset_contents_can_be_loaded(base_map_random_size):
    assert base_map_random_size.load_tileset()


def test_should_add_animal_to_map(base_map_fixed_size, single_animal):
    base_map_fixed_size.spawn_animals(single_animal)
    assert isinstance(base_map_fixed_size.animals[0], Animal)


def test_should_add_multiple_animals_to_map(base_map_fixed_size, multiple_animals):
    base_map_fixed_size.spawn_animals(multiple_animals)
    for animal in base_map_fixed_size.animals:
        assert isinstance(animal, Animal)


def test_should_move_animal_on_map(base_map_fixed_size, single_animal):
    base_map_fixed_size.spawn_animals(single_animal)
    assert base_map_fixed_size.animals[0].get_position == Coordinates(0, 0)
    base_map_fixed_size.animals[0].move(1, 1)
    base_map_fixed_size.update_animal_positions()
    assert base_map_fixed_size.matrix.matrix[1][1] == base_map_fixed_size.animals[0]
    assert base_map_fixed_size.matrix.matrix[0][0] is None


def test_map_matrix_matches_set_dimensions(base_map_fixed_size, base_map_random_size):
    assert (
        base_map_fixed_size.matrix.size.height,
        base_map_fixed_size.matrix.size.width,
    ) == (
        MAX_SIZE,
        MAX_SIZE,
    )
    for i in range(10):
        rand_map = base_map_random_size
        assert rand_map.matrix.size.height
        assert rand_map.matrix.size.width


def test_get_animal_map_should_return_reference_to_parent_map(
    base_map_fixed_size, single_animal
):
    base_map_fixed_size.spawn_animals(single_animal)
    assert single_animal.map is base_map_fixed_size
