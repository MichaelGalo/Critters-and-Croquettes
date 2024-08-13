from datetime import date


class Tiger:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


tiger = Tiger("Shere Khan", "Panthera tigris", "Evening")
tiger.walking = True
