from datetime import date


class Panda:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


panda = Panda("Po", "Ailuropoda melanoleuca", "Evening")
panda.walking = True
