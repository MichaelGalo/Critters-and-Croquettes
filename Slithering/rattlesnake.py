from datetime import date


class Rattlesnake:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


snek = Rattlesnake("Sneaky Snek", "Pigmy")
snek.slithering = True
