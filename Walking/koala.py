from datetime import date


class Koala:
    def __init__(self, name, species, shift, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


koala = Koala("Kenny", "Phascolarctos cinereus", "Midday", "Eucalyptus Leaves")
koala.walking = True
print(koala)
