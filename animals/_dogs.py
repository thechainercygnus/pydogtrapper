from animals import Animal


class Dog(Animal):
    def __init__(self, name: str, state: int = None, injuries: dict = None):
        super().__init__(species="canine", state=state, injuries=injuries)
        self.name = name
