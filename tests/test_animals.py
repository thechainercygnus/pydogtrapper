import pytest
from animals import Animal, Dog
from animals._animals import STATES


@pytest.fixture
def base_animal():
    return Animal(species="test", state=None, injuries=None)


@pytest.fixture
def base_dog():
    return Dog(name="Frankie")


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
