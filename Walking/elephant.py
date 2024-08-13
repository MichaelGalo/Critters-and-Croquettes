from datetime import date


class Elephant:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


elephant = Elephant("Dumbo", "Loxodonta", "Morning")
elephant.walking = True
