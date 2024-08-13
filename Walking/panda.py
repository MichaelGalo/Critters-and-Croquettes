from datetime import date


class Panda:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


panda = Panda("Po", "Ailuropoda melanoleuca")
panda.walking = True
print(panda)
