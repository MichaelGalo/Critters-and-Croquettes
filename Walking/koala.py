from datetime import date


class Koala:
    def __init__(self, name, species, shift) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


koala = Koala("Kenny", "Phascolarctos cinereus", "Midday")
koala.walking = True
