from typing import NamedTuple

from simpleobjects import Coordinates


class fear_state(NamedTuple):
    stress_trigger: int
    state: str


STATES = ("normal", "alert", "frightened", "fear", "terror")


class Animal:
    __counter = 0

    def __init__(
        self,
        species: str,
        state: int | None,
        injuries: dict | None,
        init_position: Coordinates = Coordinates(0, 0),
    ) -> None:
        self.__class__.__counter += 1
        self._ordinal = self.__counter
        self.species = species
        self._injuries = injuries
        self._position = init_position
        self._state = state or 0
        self._stress_level = self._state * 10 if self._state > 0 else 0

    def __str__(self):
        return f"<Animal(Species={self.species})>"

    def __repr__(self):
        return f"<Animal#{self._ordinal}>"

    # Movement Functions
    def move(self, x_translation: int, y_translation: int) -> None:
        x_result = self._position.x + x_translation
        y_result = self._position.y + y_translation
        self._position = Coordinates(x_result, y_result)

    # Injury Functions

    # Stress Functions
    def add_stress(self, stress: int) -> None:
        self._stress_level += stress
        self._set_state()

    def remove_stress(self, stress: int) -> None:
        self._stress_level -= stress
        self._set_state()

    # Properties
    @property
    def get_position(self) -> Coordinates:
        return self._position

    @property
    def injuries(self) -> dict:
        return self._injuries

    @property
    def ordinal(self) -> int:
        return self._ordinal

    @property
    def state(self) -> str:
        return STATES[self._state]

    @property
    def stress_level(self) -> int:
        return self._stress_level

    # Internal Class Functions
    def _set_state(self) -> None:
        _state = int(round(self.stress_level / 10, 0))
        if _state > len(STATES) - 1:
            self._state = len(STATES) - 1
        elif _state < 0:
            self._state = 0
        else:
            self._state = _state
