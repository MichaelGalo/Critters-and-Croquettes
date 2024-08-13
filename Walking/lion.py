from datetime import date


class Lion:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


lion = Lion("Simba", "Panthera leo", "Morning")
lion.walking = True
