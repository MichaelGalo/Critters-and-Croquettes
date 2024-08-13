from datetime import date


class Elephant:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


elephant = Elephant("Dumbo", "Loxodonta")
elephant.walking = True
print(elephant)
