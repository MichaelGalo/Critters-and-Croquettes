from datetime import date


class Penguin:
    def __init__(self, name, species, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


penguin = Penguin("Pingu", "Aptenodytes forsteri", "Fish Popsicle")
penguin.swimming = True
