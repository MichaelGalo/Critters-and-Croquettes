from datetime import date


class Kangaroo:
    def __init__(self, name, species, shift, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


kangaroo = Kangaroo("Kanga", "Macropus", "Evening", "Shrimp-on-the-Barbie")
kangaroo.walking = True
