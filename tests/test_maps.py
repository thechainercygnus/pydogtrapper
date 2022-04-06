import os

import pytest
from maps import Map
from maps._maps import MAX_SIZE
from simpleobjects import Dimensions


@pytest.fixture
def base_map_fixed_size():
    return Map(size=MAX_SIZE)


@pytest.fixture
def base_map_random_size():
    return Map()


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
