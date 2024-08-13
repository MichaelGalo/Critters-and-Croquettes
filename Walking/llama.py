from datetime import date


class Llama:
    def __init__(self, name, species, shift, food):
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


miss_fuzz = Llama(
    "Miss Fuzz", "domestic llama", "Midday", "Maccu Piccu Crumbs from Tourists"
)
miss_fuzz.walking = True
print(miss_fuzz)
