from datetime import date


class Kangaroo:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


kangaroo = Kangaroo("Kanga", "Macropus", "Evening")
kangaroo.walking = True
