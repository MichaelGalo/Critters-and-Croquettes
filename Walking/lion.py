from datetime import date


class Lion:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


lion = Lion("Simba", "Panthera leo")
lion.walking = True
print(lion)
