from datetime import date


class Tiger:
    def __init__(self, name, species) -> None:
        self.date_added = date.today()
        self.name = name
        self.species = species


tiger = Tiger("Shere Khan", "Panthera tigris")
tiger.walking = True
print(tiger)
