from datetime import date


class Tiger:
    def __init__(self, name, species, shift, food) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


tiger = Tiger("Shere Khan", "Panthera tigris", "Evening", "Meat from Mike Tyson")
tiger.walking = True
