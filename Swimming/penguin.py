from datetime import date


class Penguin:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


penguin = Penguin("Pingu", "Aptenodytes forsteri")
penguin.swimming = True
