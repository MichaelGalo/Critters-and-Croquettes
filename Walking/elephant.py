from datetime import date


class Elephant:
    def __init__(self, name, species, shift, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {self.date_added}")


elephant = Elephant("Dumbo", "Loxodonta", "Morning", "Whole Ass Pumpkin")
elephant.walking = True
