from datetime import date


class Zebra:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


zebra = Zebra("Marty", "Equus zebra")
zebra.walking = True
print(zebra)
