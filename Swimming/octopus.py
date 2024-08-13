from datetime import date


class Octopus:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


octopus = Octopus("Otto", "Octopus vulgaris")
octopus.swimming = True
