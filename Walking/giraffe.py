from datetime import date


class Giraffe:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


giraffe = Giraffe("Geoffrey", "Giraffa camelopardalis", "Midday")
giraffe.walking = True
