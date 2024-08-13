from datetime import date


class Koala:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


koala = Koala("Kenny", "Phascolarctos cinereus")
koala.walking = True
print(koala)
