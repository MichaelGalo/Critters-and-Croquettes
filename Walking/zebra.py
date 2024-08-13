from datetime import date


class Zebra:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


zebra = Zebra("Marty", "Equus zebra", "Morning")
zebra.walking = True
