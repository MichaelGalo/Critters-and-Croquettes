from datetime import date


class Rattlesnake:
    def __init__(self, name, species, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


snek = Rattlesnake("Sneaky Snek", "Pigmy Rattlesnake", "Mouse")
snek.slithering = True
print(snek)
