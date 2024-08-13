from datetime import date


class Shark:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


shark = Shark("Jaws", "Carcharodon carcharias")
shark.swimming = True
