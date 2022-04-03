import pytest
from animals import Animal, Dog
from animals._animals import STATES


@pytest.fixture
def base_animal():
    return Animal(species="test", state=None, injuries=None)


@pytest.fixture
def base_dog():
    return Dog(name="Frankie")


@pytest.fixture
def injured_dog():
    return Dog(name="Frankie", state=1, injuries={"ear": {"left": "nicked"}})


def test_should_create_base_animal(base_animal):
    assert base_animal is not None


def test_should_create_base_dog_as_instance_of_animal(base_dog):
    assert isinstance(base_dog, Animal)


def test_should_compare_unequal_animal_and_dog(base_animal, base_dog):
    assert base_animal != base_dog


def test_should_compare_unequal_two_dogs_with_same_name(base_dog):
    other = Dog(name=base_dog.name)
    assert base_dog != other
    assert base_dog is not other


def test_should_compare_unequal_str_repr_for_animal(base_animal):
    assert str(base_animal) != repr(base_animal)


def test_should_compare_unequal_repr_of_two_instances_of_animal(base_animal):
    other = Animal(species="rabbit", state=None, injuries=None)
    assert repr(base_animal) != other


def test_should_report_a_dogs_state(base_dog):
    assert base_dog.state in STATES


def test_should_report_should_report_base_dogs_injuries_as_none(base_dog):
    assert base_dog.injuries is None


def test_should_create_dog_in_non_default_state_with_injuries():
    injured_dog = Dog(name="Frankie", state=2, injuries={"ear": {"left": "nicked"}})
    assert injured_dog.state == "frightened"
    assert injured_dog.injuries == {"ear": {"left": "nicked"}}


def test_should_report_dogs_stress_level(base_dog):
    assert base_dog.stress_level == 0


def test_should_increase_dogs_state_by_adding_stress(base_dog):
    assert base_dog.stress_level == 0
    assert base_dog.state == STATES[0]

    base_dog.add_stress(10)

    assert base_dog.stress_level == 10
    assert base_dog.state == STATES[1]


def test_should_decrease_dogs_state_by_subtracting_stress(injured_dog):
    assert injured_dog.stress_level == 10
    assert injured_dog.state == STATES[1]

    injured_dog.remove_stress(10)

    assert injured_dog.stress_level == 0
    assert injured_dog.state == STATES[0]


def test_should_catch_state_out_of_bounds(base_dog):
    assert base_dog.stress_level == 0
    assert base_dog.state == STATES[0]

    base_dog.add_stress(1000)

    assert base_dog.stress_level == 1000
    assert base_dog.state == STATES[-1]

    base_dog.remove_stress(2000)

    assert base_dog.stress_level == -1000
    assert base_dog.state == STATES[0]
