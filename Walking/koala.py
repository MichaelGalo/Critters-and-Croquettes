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


koala = Koala("Kenny", "Phascolarctos cinereus", "Midday", "Eucalyptus Leaves")
koala.walking = True
