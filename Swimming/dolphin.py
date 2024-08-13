from datetime import date


class Dolphin:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


dolphin = Dolphin("Flipper", "Delphinus delphis")
dolphin.swimming = True
