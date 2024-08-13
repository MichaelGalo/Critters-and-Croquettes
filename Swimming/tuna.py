from datetime import date


class Tuna:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


tuna = Tuna("Gilly", "Blue Fin")
tuna.swimming = True
print(tuna)
