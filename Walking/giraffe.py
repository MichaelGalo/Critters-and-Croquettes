from datetime import date


class Giraffe:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


giraffe = Giraffe("Geoffrey", "Giraffa camelopardalis")
giraffe.walking = True
print(giraffe)
