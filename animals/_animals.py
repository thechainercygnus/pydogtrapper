STATES = ("normal", "alert", "frightened", "fear", "terror")


class Animal:
    __counter = 0

    def __init__(self, species: str, state: int | None, injuries: dict | None) -> None:
        self.__class__.__counter += 1
        self.__ordinal = self.__counter
        self.species = species
        self._state = state or 0
        self._injuries = injuries

    def __str__(self):
        return f"<Animal(Species={self.species})>"

    def __repr__(self):
        return f"<Animal#{self.__ordinal}>"

    @property
    def ordinal(self):
        return self.__ordinal

    @property
    def state(self):
        return STATES[self._state]

    @property
    def injuries(self):
        return self._injuries
