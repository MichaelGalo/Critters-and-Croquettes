from datetime import date


class Whale:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


whale = Whale("Willy", "Balaenoptera musculus")
whale.swimming = True
print(whale)
