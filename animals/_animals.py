from typing import NamedTuple


class fear_state(NamedTuple):
    stress_trigger: int
    state: str


STATES = ("normal", "alert", "frightened", "fear", "terror")


class Animal:
    __counter = 0

    def __init__(self, species: str, state: int | None, injuries: dict | None) -> None:
        self.__class__.__counter += 1
        self.__ordinal = self.__counter
        self.species = species
        self._state = state or 0
        self._injuries = injuries
        self._stress_level = self._state * 10 if self._state > 0 else 0

    def __str__(self):
        return f"<Animal(Species={self.species})>"

    def __repr__(self):
        return f"<Animal#{self.__ordinal}>"

    def add_stress(self, stress: int) -> None:
        self._stress_level += stress
        self._set_state()

    def remove_stress(self, stress: int) -> None:
        self._stress_level -= stress
        self._set_state()

    @property
    def ordinal(self) -> int:
        return self.__ordinal

    @property
    def state(self) -> str:
        return STATES[self._state]

    @property
    def injuries(self) -> dict:
        return self._injuries

    @property
    def stress_level(self) -> int:
        return self._stress_level

    def _set_state(self) -> None:
        _state = int(round(self.stress_level / 10, 0))
        if _state > len(STATES) - 1:
            self._state = len(STATES) - 1
        elif _state < 0:
            self._state = 0
        else:
            self._state = _state
