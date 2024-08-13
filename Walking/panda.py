from datetime import date


class Panda:
    def __init__(self, name, species, shift, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


panda = Panda("Po", "Ailuropoda melanoleuca", "Evening", "Bamboo")
panda.walking = True
